# Proyecto 11 - Config Drift Detector

> **PC5 - Desarrollo de Software 2025-II**  
> Microservicio FastAPI que detecta **configuration drift** entre manifests K8s del repositorio (IaC) y el estado real del cluster.

---

##  Descripción

El equipo de plataforma necesita detectar configuration drift para mantener el cluster alineado con IaC. Este microservicio:

-  **Compara** manifests del repo (`k8s/`) con el estado real del cluster
-  **Detecta** diferencias en réplicas, labels, securityContext, NetworkPolicy
-  **Genera** reportes con evidencia en `.evidence/`
-  **Bloquea** deploys si hay drift crítico

---

##  Arquitectura

```
┌─────────────────────────────────────────────────────────┐
│                    GitHub Actions                        │
│  ┌────────────┬────────────────────┬──────────────────┐ │
│  │  ci.yml    │ build_scan_sbom.yml│ drift_check.yml  │ │
│  │ Lint+Tests │  Build+Scan+SBOM   │  Drift Detection │ │
│  └────────────┴────────────────────┴──────────────────┘ │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│              Config Drift Detector API                   │
│                    (FastAPI)                             │
│  ┌──────────────────────────────────────────────────┐   │
│  │  /health  │  /drift  │  /report  │  /            │   │
│  └──────────────────────────────────────────────────┘   │
│                                                           │
│  ┌────────────────────┐  ┌──────────────────────────┐   │
│  │ collect_desired    │  │ collect_actual           │   │
│  │ _state.py          │  │ _state.py                │   │
│  │ (lee k8s/)         │  │ (kubectl get ...)        │   │
│  └────────────────────┘  └──────────────────────────┘   │
│              │                       │                   │
│              └───────────┬───────────┘                   │
│                          ▼                               │
│              ┌───────────────────────┐                   │
│              │ compare_states.py     │                   │
│              │ (detecta drift)       │                   │
│              └───────────────────────┘                   │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                   .evidence/                             │
│  ├── ci-report.txt                                       │
│  ├── coverage.json                                       │
│  ├── drift-report.json                                   │
│  ├── build-log.txt                                       │
│  ├── trivy-report.json                                   │
│  └── sbom.json                                           │
└─────────────────────────────────────────────────────────┘
```

---

##  Quick Start

### Requisitos Previos
- Python 3.11+
- Docker y Docker Compose
- kubectl
- Minikube o kind (para cluster local)

### Instalación

```bash
# 1. Clonar repositorio
git clone https://github.com/USUARIO/REPO.git
cd pc5_desarrollo

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar tests
pytest tests/ -v --cov=app

# 4. Iniciar API
uvicorn app.main:app --reload
```

La API estará en: `http://localhost:8000`

### Con Docker

```bash
# Build y run
docker-compose up --build -d

# Health check
curl http://localhost:8000/health

# Drift check
curl http://localhost:8000/drift | jq

# Ver logs
docker-compose logs -f

# Detener
docker-compose down
```

---

##  API Endpoints

### `GET /health`
Health check del servicio

**Response:**
```json
{
  "status": "healthy",
  "service": "config-drift-detector",
  "timestamp": "2024-12-02T12:00:00Z"
}
```

### `GET /drift`
Ejecuta comparación y detecta drift

**Response:**
```json
{
  "has_drift": true,
  "drift_count": 2,
  "differences": [
    {
      "type": "DRIFT",
      "resource_type": "Deployment",
      "name": "nginx-app",
      "namespace": "default",
      "drifts": [
        {
          "field": "replicas",
          "desired": 3,
          "actual": 2,
          "message": "Replicas differ: manifest=3, cluster=2"
        }
      ],
      "severity": "HIGH"
    }
  ],
  "timestamp": "2024-12-02T12:00:00Z"
}
```

### `GET /report`
Genera reporte completo con estadísticas

**Response:**
```json
{
  "timestamp": "2024-12-02T12:00:00Z",
  "has_drift": true,
  "summary": {
    "total_drifts": 2,
    "by_type": {
      "DRIFT": 1,
      "MISSING": 1
    },
    "by_severity": {
      "HIGH": 1,
      "CRITICAL": 1
    }
  },
  "details": [...],
  "evidence_file": "/.evidence/drift-report.json"
}
```

---

##  Pipeline DevSecOps

### 1. CI Pipeline (`ci.yml`)

Se ejecuta automáticamente en cada push/PR:

```yaml
Triggers: push, pull_request (main, develop)
Jobs:
  - Lint (flake8)
  - Tests (pytest)
  - Coverage check (>70%)
  
Evidencias:
  .evidence/ci-report.txt
  .evidence/coverage.json
```

### 2. Build, Scan & SBOM (`build_scan_sbom.yml`)

Pipeline de seguridad:

```yaml
Triggers: push, pull_request, workflow_dispatch
Jobs:
  - Build Docker image
  - Scan con Trivy (vulnerabilities)
  - Generate SBOM con Syft
  - Check critical vulnerabilities
  
Evidencias:
  .evidence/build-log.txt
  .evidence/trivy-report.json
  .evidence/trivy-report.txt
  .evidence/sbom.json
  .evidence/sbom.txt
```

### 3. Drift Check (`drift_check.yml`)

Ejecutable bajo demanda o programado:

```yaml
Triggers: workflow_dispatch, schedule (cada 6h)
Runs on: self-hosted (requiere kubectl)
Jobs:
  - desired_state: lee k8s/
  - actual_state: consulta cluster
  - compare: ejecuta compare_states.py
  - fail_if_critical: bloquea si hay drift crítico
  
Evidencias:
  .evidence/drift-report.json
```

**IMPORTANTE**: Este workflow requiere:
- Self-hosted runner con Docker y kubectl
- Secret `KUBECONFIG` configurado en GitHub

---

##  Tipos de Drift Detectados

| Tipo | Descripción | Severidad | Bloquea Deploy |
|------|-------------|-----------|----------------|
| **MISSING** | Recurso en manifests pero no en cluster | CRITICAL | ✅ SÍ |
| **EXTRA** | Recurso en cluster pero no en manifests | WARNING | ❌ NO |
| **DRIFT** | Recurso existe en ambos pero con diferencias | HIGH | ⚠️ Depende |

### Campos Comparados

#### Deployments
-  Replicas
-  Labels (metadata)
-  SecurityContext
-  Resources (requests/limits)
-  Spec completo

#### Services, ConfigMaps, etc.
-  Labels
-  Spec

#### NetworkPolicy (Sprint 3)
-  Presencia/ausencia
-  Reglas de ingress/egress

---

##  Testing

### Ejecutar Tests Localmente

```bash
# Todos los tests
pytest tests/ -v

# Con coverage
pytest tests/ --cov=app --cov-report=term --cov-report=html

# Ver reporte HTML
open htmlcov/index.html
```

### Tests Incluidos

-  `test_health_endpoint`: Health check
-  `test_root_endpoint`: Root endpoint
-  `test_drift_endpoint_structure`: Estructura de /drift
-  `test_report_endpoint_structure`: Estructura de /report
-  `test_no_drift_when_states_match`: Sin drift cuando coinciden
-  `test_missing_resource_in_cluster`: Detecta MISSING
-  `test_extra_resource_in_cluster`: Detecta EXTRA
-  `test_replica_drift_detection`: Detecta drift en replicas
-  `test_label_drift_detection`: Detecta drift en labels
-  `test_replicas_difference`: Comparación de replicas
-  `test_missing_labels`: Detecta labels faltantes
-  `test_no_drift_when_identical`: Sin drift cuando son idénticos

**Coverage**: >70% (configurado en pytest.ini y ci.yml)

---

##  Stack Tecnológico

| Componente | Tecnología |
|------------|------------|
| Backend | FastAPI 0.104.1 |
| Tests | pytest 7.4.3, pytest-cov 4.1.0 |
| Lint | flake8 |
| Container | Docker, Docker Compose |
| Orchestration | Kubernetes (Minikube/kind) |
| CI/CD | GitHub Actions |
| Security Scan | Trivy |
| SBOM | Syft |
| IaC | YAML manifests |

---

##  Estructura del Proyecto

```
pc5_desarrollo/
├── .github/
│   └── workflows/
│       ├── ci.yml                      # Pipeline CI
│       ├── build_scan_sbom.yml         # Build + Scan + SBOM
│       └── drift_check.yml             # Drift detection
├── .evidence/                          # VERSIONADA en Git
│   ├── README.md
│   ├── ci-report.txt
│   ├── coverage.json
│   ├── build-log.txt
│   ├── trivy-report.json
│   ├── trivy-report.txt
│   ├── sbom.json
│   ├── sbom.txt
│   └── drift-report.json
├── app/
│   ├── __init__.py
│   ├── main.py                         # API FastAPI
│   └── scripts/
│       ├── __init__.py
│       ├── collect_desired_state.py    # Lee k8s/
│       ├── collect_actual_state.py     # kubectl get
│       └── compare_states.py           # Detecta drift
├── k8s/                                # Manifests de ejemplo
│   ├── deployment.yaml
│   ├── service.yaml
│   └── configmap.yaml
├── tests/
│   ├── __init__.py
│   └── test_drift_detector.py          # 12 tests
├── CODEOWNERS                          # Code owners
├── KANBAN.md                           # Tablero Kanban
├── SPRINT_VIDEOS.md                    # Guía de videos
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pytest.ini
├── .flake8
├── .gitignore
├── Makefile
├── check_drift.py                      # Script manual
└── README.md                           # Este archivo
```

---

##  Sprints y Entregas

### Sprint 1 (Días 1-2): Modelo + API Mínima
-  Estructura de datos
-  `compare_states.py` con lógica de comparación
- API `/drift` con mocks
-  CI pipeline (`ci.yml`)
-  Tests unitarios (12/12 passed)

**Evidencias**: `.evidence/ci-report.txt`, `coverage.json`

### Sprint 2 (Días 3-4): Manifests + Docker
-  `collect_desired_state.py` lee YAML
-  Dockerfile + docker-compose
-  `drift_check.yml` workflow
-  Endpoint `/report`

**Evidencias**: `.evidence/drift-report.json`, `build-log.txt`

### Sprint 3 (Días 5-6): Minikube + Política de Bloqueo
-  `collect_actual_state.py` con kubectl
-  Self-hosted runner configurado
-  Reglas de drift crítico
-  `build_scan_sbom.yml` pipeline
-  Detección de NetworkPolicy

**Evidencias**: `.evidence/trivy-report.json`, `sbom.json`, `drift-report.json` (real)

---

##  Tablero Kanban

**Herramienta**: GitHub Projects  

Ver [KANBAN.md](KANBAN.md) para detalles completos del tablero.

### Resumen de Tareas

| Sprint | Tareas Completadas | Estado |
|--------|--------------------|--------|
| Sprint 1 | 4/4 | ✅ Done |
| Sprint 2 | 4/4 | ✅ Done |
| Sprint 3 | 4/4 | ✅ Done |
| **Total** | **12/12** | ✅ **100%** |

---

##  Seguridad

### Dockerfile Hardening
-  Non-root user (`USER 1000`)
-  Python slim image
-  HEALTHCHECK configurado
-  Minimal dependencies

### Secrets Management
-  `KUBECONFIG` como GitHub Secret
-  NO usar PATs de GitHub
-  NO usar credenciales cloud (AWS/GCP/Azure)
-  Solo `GITHUB_TOKEN` implícito

### Scanning
-  Trivy scan de vulnerabilidades
-  SBOM generado con Syft
-  Check de vulnerabilidades críticas (fail si >10)

---

##  Troubleshooting

### Error: kubectl: command not found
```bash
# Instalar kubectl (Linux)
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```

### Error: Unable to connect to cluster
```bash
# Verificar kubeconfig
kubectl cluster-info

# Verificar contexto
kubectl config current-context

# Para desarrollo: usar kubeconfig de prueba
export KUBECONFIG=~/.kube/config
```

### No se detecta drift pero existe
1. Verificar manifests en `k8s/`
2. Confirmar recursos en cluster: `kubectl get all`
3. Revisar namespace correcto
4. Ver logs de API: `docker-compose logs -f`

### Tests fallan
```bash
# Reinstalar dependencias
pip install -r requirements.txt --force-reinstall

# Verificar PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# O usar pytest con -m
python -m pytest tests/ -v
```

---

##  Comandos Útiles

```bash
# Tests
make test                                  # Ejecutar tests
pytest tests/ --cov=app --cov-report=html # Coverage

# API
make run                                   # Iniciar API
curl http://localhost:8000/health          # Health check
curl http://localhost:8000/drift | jq     # Drift check

# Docker
make docker-up                             # Build + run
docker-compose logs -f                     # Ver logs
make docker-down                           # Detener

# Drift check manual
python check_drift.py                      # Script standalone

# Lint
flake8 app/ tests/                         # Lint manual

# Cluster
kubectl apply -f k8s/                      # Aplicar manifests
kubectl get all                            # Ver recursos
kubectl scale deployment nginx-app --replicas=2  # Modificar
```

---

##  Documentación Adicional

- [KANBAN.md](KANBAN.md) - Tablero Kanban detallado
- [SPRINT_VIDEOS.md](SPRINT_VIDEOS.md) - Guía de videos
- [.evidence/README.md](.evidence/README.md) - Evidencias DevSecOps
- [CODEOWNERS](CODEOWNERS) - Code ownership

---

##  Equipo

**Rol**: Backend / DevOps  
**Responsabilidades**:
- API FastAPI
- Scripts de drift detection
- Pipelines CI/CD
- Docker y K8s



---

##  Cumplimiento de Requisitos PC5

-  **Sprints**: 3 sprints de 2 días + Día 7
-  **Tablero Kanban**: GitHub Projects con Backlog/Doing/Review/Done
-  **Pull Requests**: Todo merge vía PR, prohibido merge directo
-  **GitHub Actions**: 3 workflows (CI, Build/Scan/SBOM, Drift Check)
-  **Self-hosted Runner**: Configurado para drift_check.yml
-  **Entorno Local**: 100% local (Docker, Minikube, kubectl)
-  **Carpeta .evidence/**: Versionada con 8 archivos
-  **Backend FastAPI**: No Flask, con type hints
-  **Videos**: Guía completa en SPRINT_VIDEOS.md
-  **Documentación**: Completa y profesional
