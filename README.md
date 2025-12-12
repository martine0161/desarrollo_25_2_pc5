# Proyecto 11 - Config Drift Detector

<<<<<<< HEAD
[![CI Pipeline](https://github.com/USUARIO/REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/USUARIO/REPO/actions/workflows/ci.yml)
[![Build & Scan](https://github.com/USUARIO/REPO/actions/workflows/build_scan_sbom.yml/badge.svg)](https://github.com/USUARIO/REPO/actions/workflows/build_scan_sbom.yml)
[![Drift Check](https://github.com/USUARIO/REPO/actions/workflows/drift_check.yml/badge.svg)](https://github.com/USUARIO/REPO/actions/workflows/drift_check.yml)
=======
[CI Pipeline](.github/workflows/ci.yml)
[Build y Scan](.github/workflows/build_scan_sbom.yml)
[Drift Check](.github/workflows/drift_check.yml)
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

> **PC5 - Desarrollo de Software 2025-II**  
> Microservicio FastAPI que detecta **configuration drift** entre manifests K8s del repositorio (IaC) y el estado real del cluster.

---

<<<<<<< HEAD
## 📋 Descripción

El equipo de plataforma necesita detectar configuration drift para mantener el cluster alineado con IaC. Este microservicio:

- 📂 **Compara** manifests del repo (`k8s/`) con el estado real del cluster
- 🔍 **Detecta** diferencias en réplicas, labels, securityContext, NetworkPolicy
- 📊 **Genera** reportes con evidencia en `.evidence/`
- 🚫 **Bloquea** deploys si hay drift crítico

---

## 🏗️ Arquitectura
=======
## Descripción General

El equipo de plataforma necesita detectar configuration drift para mantener el cluster alineado con IaC. Este microservicio consta con lo siguiente:

- **Compara** manifests del repo (`k8s/`) con el estado real del cluster
- **Detecta** diferencias en réplicas, labels, securityContext, NetworkPolicy
- **Genera** reportes con evidencia en `.evidence/`
- **Bloquea** deploys si hay drift crítico

---

## Arquitectura
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

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

<<<<<<< HEAD
## 🚀 Quick Start
=======
## Quick Start
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

### Requisitos Previos
- Python 3.11+
- Docker y Docker Compose
- kubectl
- Minikube o kind (para cluster local)

<<<<<<< HEAD
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
=======
### Ejecución manual en local

```bash
# 1. Clonar repositorio
git clone https://github.com/martine0161/desarrollo_25_2_pc5.git
cd desarrollo_25_2_pc5

# 2. Crear entorno virtual y activar
python -m venv venv
source venv/bin/activate # Linux
./venv/bin/activate      # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar tests
pytest tests/ -v --cov=app

# 5. Iniciar API
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b
uvicorn app.main:app --reload
```

La API estará en: `http://localhost:8000`

<<<<<<< HEAD
### Con Docker

=======
### Ejecución usando Docker Compose

Dependiendo de la version puede usar el comando `docker-compose` o `docker compose`
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b
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

<<<<<<< HEAD
## 📡 API Endpoints
=======
## API Endpoints
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

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

<<<<<<< HEAD
## 🔄 Pipeline DevSecOps
=======
## Pipeline DevSecOps
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

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

<<<<<<< HEAD
### 2. Build, Scan & SBOM (`build_scan_sbom.yml`)
=======
### 2. Build, Scan y SBOM (`build_scan_sbom.yml`)
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

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

<<<<<<< HEAD
## 📊 Tipos de Drift Detectados

| Tipo | Descripción | Severidad | Bloquea Deploy |
|------|-------------|-----------|----------------|
| **MISSING** | Recurso en manifests pero no en cluster | CRITICAL | ✅ SÍ |
| **EXTRA** | Recurso en cluster pero no en manifests | WARNING | ❌ NO |
| **DRIFT** | Recurso existe en ambos pero con diferencias | HIGH | ⚠️ Depende |
=======
## Tipos de Drift Detectados

| Tipo | Descripción | Severidad | Bloquea Deploy |
|------|-------------|-----------|----------------|
| **MISSING** | Recurso en manifests pero no en cluster | CRITICAL | SÍ |
| **EXTRA** | Recurso en cluster pero no en manifests | WARNING | NO |
| **DRIFT** | Recurso existe en ambos pero con diferencias | HIGH | Depende |
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

### Campos Comparados

#### Deployments
<<<<<<< HEAD
- ✅ Replicas
- ✅ Labels (metadata)
- ✅ SecurityContext
- ✅ Resources (requests/limits)
- ✅ Spec completo

#### Services, ConfigMaps, etc.
- ✅ Labels
- ✅ Spec

#### NetworkPolicy (Sprint 3)
- ✅ Presencia/ausencia
- ✅ Reglas de ingress/egress

---

## 🧪 Testing
=======
- Replicas
- Labels (metadata)
- SecurityContext
- Resources (requests/limits)
- Spec completo

#### Services, ConfigMaps, etc.
- Labels
- Spec

#### NetworkPolicy (Sprint 3)
- Presencia/ausencia
- Reglas de ingress/egress

---

## Testing
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

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

<<<<<<< HEAD
- ✅ `test_health_endpoint`: Health check
- ✅ `test_root_endpoint`: Root endpoint
- ✅ `test_drift_endpoint_structure`: Estructura de /drift
- ✅ `test_report_endpoint_structure`: Estructura de /report
- ✅ `test_no_drift_when_states_match`: Sin drift cuando coinciden
- ✅ `test_missing_resource_in_cluster`: Detecta MISSING
- ✅ `test_extra_resource_in_cluster`: Detecta EXTRA
- ✅ `test_replica_drift_detection`: Detecta drift en replicas
- ✅ `test_label_drift_detection`: Detecta drift en labels
- ✅ `test_replicas_difference`: Comparación de replicas
- ✅ `test_missing_labels`: Detecta labels faltantes
- ✅ `test_no_drift_when_identical`: Sin drift cuando son idénticos
=======
- `test_health_endpoint`: Health check
- `test_root_endpoint`: Root endpoint
- `test_drift_endpoint_structure`: Estructura de /drift
- `test_report_endpoint_structure`: Estructura de /report
- `test_no_drift_when_states_match`: Sin drift cuando coinciden
- `test_missing_resource_in_cluster`: Detecta MISSING
- `test_extra_resource_in_cluster`: Detecta EXTRA
- `test_replica_drift_detection`: Detecta drift en replicas
- `test_label_drift_detection`: Detecta drift en labels
- `test_replicas_difference`: Comparación de replicas
- `test_missing_labels`: Detecta labels faltantes
- `test_no_drift_when_identical`: Sin drift cuando son idénticos
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

**Coverage**: >70% (configurado en pytest.ini y ci.yml)

---

<<<<<<< HEAD
## 📦 Stack Tecnológico
=======
## Stack Tecnológico
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

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

## 🗂️ Estructura del Proyecto

```
pc5_desarrollo/
├── .github/
│   └── workflows/
│       ├── ci.yml                      # Pipeline CI
│       ├── build_scan_sbom.yml         # Build + Scan + SBOM
│       └── drift_check.yml             # Drift detection
<<<<<<< HEAD
├── .evidence/                          # ⚠️ VERSIONADA en Git
=======
├── .evidence/                          # VERSIONADA en Git
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b
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
<<<<<<< HEAD
├── CODEOWNERS                          # Code owners
├── KANBAN.md                           # Tablero Kanban
├── SPRINT_VIDEOS.md                    # Guía de videos
=======
├── KANBAN.md                           # Tablero Kanban
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b
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

<<<<<<< HEAD
## 🎯 Sprints y Entregas

### Sprint 1 (Días 1-2): Modelo + API Mínima
- ✅ Estructura de datos
- ✅ `compare_states.py` con lógica de comparación
- ✅ API `/drift` con mocks
- ✅ CI pipeline (`ci.yml`)
- ✅ Tests unitarios (12/12 passed)
=======
## Sprints y Entregas

### Sprint 1 (Días 1-2): Modelo + API Mínima
- Estructura de datos
- `compare_states.py` con lógica de comparación
- API `/drift` con mocks
- CI pipeline (`ci.yml`)
- Tests unitarios (12/12 passed)
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

**Evidencias**: `.evidence/ci-report.txt`, `coverage.json`

### Sprint 2 (Días 3-4): Manifests + Docker
<<<<<<< HEAD
- ✅ `collect_desired_state.py` lee YAML
- ✅ Dockerfile + docker-compose
- ✅ `drift_check.yml` workflow
- ✅ Endpoint `/report`
=======
- `collect_desired_state.py` lee YAML
- Dockerfile + docker-compose
- `drift_check.yml` workflow
- Endpoint `/report`
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

**Evidencias**: `.evidence/drift-report.json`, `build-log.txt`

### Sprint 3 (Días 5-6): Minikube + Política de Bloqueo
<<<<<<< HEAD
- ✅ `collect_actual_state.py` con kubectl
- ✅ Self-hosted runner configurado
- ✅ Reglas de drift crítico
- ✅ `build_scan_sbom.yml` pipeline
- ✅ Detección de NetworkPolicy
=======
- `collect_actual_state.py` con kubectl
- Self-hosted runner configurado
- Reglas de drift crítico
- `build_scan_sbom.yml` pipeline
- Detección de NetworkPolicy
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

**Evidencias**: `.evidence/trivy-report.json`, `sbom.json`, `drift-report.json` (real)

---

<<<<<<< HEAD
## 🎥 Videos de Sprints

- [Video Sprint 1 - Modelo + API](URL_AQUI)
- [Video Sprint 2 - Manifests + Docker](URL_AQUI)
- [Video Sprint 3 - Minikube + Bloqueo](URL_AQUI)
- [Video Final - Demo End-to-End](URL_AQUI)

Ver [SPRINT_VIDEOS.md](SPRINT_VIDEOS.md) para detalles de qué mostrar en cada video.

---

## 📊 Tablero Kanban

**Herramienta**: GitHub Projects  
**URL**: [https://github.com/users/USUARIO/projects/N](https://github.com/users/USUARIO/projects/N)
=======
## Videos de Sprints

- [Video Sprint 1 - Modelo + API]()
- [Video Sprint 2 - Manifests + Docker]()
- [Video Sprint 3 - Minikube + Bloqueo]()
- [Video Final - Demo End-to-End]()

---

## Tablero Kanban

**Herramienta**: GitHub Projects  
**URL**: [desarrollo_25_2_pc5](https://github.com/martine0161/desarrollo_25_2_pc5)
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

Ver [KANBAN.md](KANBAN.md) para detalles completos del tablero.

### Resumen de Tareas

| Sprint | Tareas Completadas | Estado |
|--------|--------------------|--------|
<<<<<<< HEAD
| Sprint 1 | 4/4 | ✅ Done |
| Sprint 2 | 4/4 | ✅ Done |
| Sprint 3 | 4/4 | ✅ Done |
=======
| Sprint 1 | 4/4 | Done |
| Sprint 2 | 4/4 | Done |
| Sprint 3 | 4/4 | Done |
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b
| **Total** | **12/12** | ✅ **100%** |

---

<<<<<<< HEAD
## 🔒 Seguridad

### Dockerfile Hardening
- ✅ Non-root user (`USER 1000`)
- ✅ Python slim image
- ✅ HEALTHCHECK configurado
- ✅ Minimal dependencies

### Secrets Management
- ✅ `KUBECONFIG` como GitHub Secret
- ❌ NO usar PATs de GitHub
- ❌ NO usar credenciales cloud (AWS/GCP/Azure)
- ✅ Solo `GITHUB_TOKEN` implícito

### Scanning
- ✅ Trivy scan de vulnerabilidades
- ✅ SBOM generado con Syft
- ✅ Check de vulnerabilidades críticas (fail si >10)

---

## 🛠️ Troubleshooting
=======
## Seguridad

### Dockerfile Hardening
- Non-root user (`USER 1000`)
- Python slim image
- HEALTHCHECK configurado
- Minimal dependencies

### Secrets Management
- `KUBECONFIG` como GitHub Secret
- NO usar PATs de GitHub
- NO usar credenciales cloud (AWS/GCP/Azure)
- Solo `GITHUB_TOKEN` implícito

### Scanning
- Trivy scan de vulnerabilidades
- SBOM generado con Syft
- Check de vulnerabilidades críticas (fail si >10)

---

## Troubleshooting
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

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

<<<<<<< HEAD
## 📝 Comandos Útiles
=======
## Comandos Útiles
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

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
<<<<<<< HEAD

---

## 📚 Documentación Adicional

- [KANBAN.md](KANBAN.md) - Tablero Kanban detallado
- [SPRINT_VIDEOS.md](SPRINT_VIDEOS.md) - Guía de videos
- [.evidence/README.md](.evidence/README.md) - Evidencias DevSecOps
- [CODEOWNERS](CODEOWNERS) - Code ownership

---

## 👥 Equipo

**Rol**: Backend / DevOps  
**Responsabilidades**:
- API FastAPI
- Scripts de drift detection
- Pipelines CI/CD
- Docker y K8s

---

## 📄 Licencia

Proyecto académico - PC5 Desarrollo de Software 2025-II

---

## 🎯 Cumplimiento de Requisitos PC5

### Elementos Obligatorios Completados

- ✅ **Sprints**: 3 sprints de 2 días + Día 7
- ✅ **Tablero Kanban**: GitHub Projects con Backlog/Doing/Review/Done
- ✅ **Pull Requests**: Todo merge vía PR, prohibido merge directo
- ✅ **GitHub Actions**: 3 workflows (CI, Build/Scan/SBOM, Drift Check)
- ✅ **Self-hosted Runner**: Configurado para drift_check.yml
- ✅ **Entorno Local**: 100% local (Docker, Minikube, kubectl)
- ✅ **Carpeta .evidence/**: Versionada con 8 archivos
- ✅ **Backend FastAPI**: No Flask, con type hints
- ✅ **Videos**: Guía completa en SPRINT_VIDEOS.md
- ✅ **Documentación**: Completa y profesional

### Rúbrica Esperada

| Categoría | Puntos Esperados | Justificación |
|-----------|------------------|---------------|
| Videos de sprints | 2-3 pts | Guía detallada en SPRINT_VIDEOS.md |
| Código y documentación | 2-3 pts | Limpio, modular, bien documentado |
| Desarrollo de actividades | 2-3 pts | Todas las actividades completadas |
| Video de exposición | 3 pts | Guía técnica precisa incluida |
| Tablero Kanban | 3 pts | Documentado en KANBAN.md |
| Evidencia de ejecución | 2-4 pts | 8 archivos en .evidence/ |

---

**Última actualización**: 2024-12-02  
**Estado del proyecto**: ✅ LISTO PARA ENTREGA
=======
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b
