# Config Drift Detector

**PC5 - Desarrollo de Software** | 11-12-2025

Microservicio FastAPI que detecta configuration drift entre manifests K8s del repositorio y el estado real del cluster.

---

## 🎯 Descripción

Sistema que compara manifests YAML (`k8s/`) con el estado real del cluster y detecta:
- **MISSING**: Recursos en manifests pero no en cluster (CRITICAL)
- **EXTRA**: Recursos en cluster pero no en manifests (WARNING)
- **DRIFT**: Recursos con diferencias (replicas, labels, etc.)

---

## 🏗️ Arquitectura

```
Manifests (k8s/) → collect_desired_state.py
                            ↓
Cluster (kubectl) → collect_actual_state.py
                            ↓
                   compare_states.py
                            ↓
                  API FastAPI (/drift, /report)
                            ↓
                  .evidence/drift-report.json
```

---

## 🚀 Instalación

```bash
# Clonar repositorio
git clone https://github.com/usuario/pc5_desarrollo.git
cd pc5_desarrollo

# Crear entorno virtual
python -m venv venv
source venv/Scripts/activate  # Windows Git Bash
# .\venv\Scripts\Activate.ps1  # PowerShell

# Instalar dependencias
python -m pip install -r requirements.txt
```

---

## 📡 API Endpoints

### `GET /health`
Health check del servicio.

### `GET /drift`
Detecta drift en tiempo real.
```bash
curl http://localhost:8000/drift
```

### `GET /report`
Reporte completo con estadísticas.
```bash
curl http://localhost:8000/report
```

---

## 🧪 Testing

```bash
# Ejecutar tests
pytest tests/ -v

# Con coverage
pytest tests/ --cov=app --cov-report=term
```

**12 tests** | Coverage > 70%

---

## 🐳 Docker

```bash
# Build y run
docker-compose up --build -d

# Verificar
curl http://localhost:8000/health

# Detener
docker-compose down
```

---

## ☸️ Kubernetes

### Requisitos
- kind o Minikube
- kubectl configurado

### Setup Cluster

```bash
# Crear cluster (kind)
kind create cluster --name drift-detector

# Aplicar manifests
kubectl apply -f k8s/

# Verificar
kubectl get all
```

### Probar Drift

```bash
# 1. Sin drift
curl http://localhost:8000/drift

# 2. Crear drift
kubectl scale deployment nginx-app --replicas=2

# 3. Detectar drift
curl http://localhost:8000/drift
```

---

## 🔄 CI/CD Pipelines

### `ci.yml`
Ejecuta en cada push:
- Lint (flake8)
- Tests (pytest)
- Coverage check

### `build_scan_sbom.yml`
Seguridad:
- Docker build
- Trivy scan
- SBOM con Syft

### `drift_check.yml`
Drift detection (manual):
- Compara estados
- Genera reporte
- Falla si drift crítico

---

## 📦 Stack Tecnológico

| Componente | Tecnología |
|------------|------------|
| Backend | FastAPI 0.104.1 |
| Tests | pytest 7.4.3 |
| Container | Docker |
| Orchestration | Kubernetes |
| CI/CD | GitHub Actions |
| Security | Trivy, Syft |

---

## 🗂️ Estructura

```
pc5_desarrollo/
├── app/
│   ├── main.py                     # API FastAPI
│   └── scripts/
│       ├── collect_desired_state.py
│       ├── collect_actual_state.py
│       └── compare_states.py
├── tests/
│   └── test_drift_detector.py      # 12 tests
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── configmap.yaml
├── .github/workflows/              # CI/CD
├── requirements.txt
└── README.md
```

---

## ⚙️ Configuración

### Variables de Entorno
```bash
export KUBECONFIG=~/.kube/config
```

### GitHub Secrets
- `KUBECONFIG`: Para drift_check.yml

---

## 🐛 Troubleshooting

**Error: kubectl not found**
```bash
# Instalar kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```

**Error: No se detecta drift**
- Verificar cluster: `kubectl cluster-info`
- Verificar recursos: `kubectl get all`
- Ver logs API: `docker-compose logs -f`

**Pods CrashLoopBackOff**
- Comentar `securityContext` en deployment.yaml
- O usar `nginxinc/nginx-unprivileged:1.21`

---

## 📝 Comandos Útiles

```bash
# Ejecutar API
python -m uvicorn app.main:app --reload

# Ejecutar tests
pytest tests/ -v

# Drift check manual
python check_drift.py

# Ver evidencias
cat .evidence/drift-report.json | jq
```

---

## 👥 Equipo

- **Martin** - Backend
- **Ariana** - Infraestructura
- **Elmer** - QA

---

## 📄 Licencia

Este proyecto es para fines académicos - PC5 Desarrollo de Software 2025-II
