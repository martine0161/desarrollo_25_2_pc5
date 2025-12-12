# Quick Start - PC5 Config Drift Detector

**Setup en 5 minutos** | 11-12-2025

---

## 🚀 Instalación Rápida

### 1. Clonar e Instalar

```bash
# Clonar repositorio
git clone https://github.com/usuario/pc5_desarrollo.git
cd pc5_desarrollo

# Crear entorno virtual
python -m venv venv

# Activar (Git Bash Windows)
source venv/Scripts/activate

# Activar (PowerShell)
# .\venv\Scripts\Activate.ps1

# Instalar dependencias
python -m pip install -r requirements.txt
```

---

## 🔧 Setup Kubernetes

### Opción A: kind (Recomendado)

```bash
# Crear cluster
kind create cluster --name drift-detector

# Verificar
kubectl cluster-info
kubectl get nodes

# Aplicar manifests
kubectl apply -f k8s/

# Verificar recursos
kubectl get all
```

### Opción B: Minikube

```bash
# Iniciar cluster
minikube start

# Aplicar manifests
kubectl apply -f k8s/

# Verificar
kubectl get all
```

---

## 🎯 Ejecutar API

```bash
# Iniciar servidor
python -m uvicorn app.main:app --reload

# Debería mostrar:
# INFO: Uvicorn running on http://127.0.0.1:8000
```

---

## 🧪 Probar Endpoints

### Health Check
```bash
curl http://localhost:8000/health
```

**Respuesta esperada:**
```json
{
  "status": "healthy",
  "service": "config-drift-detector",
  "timestamp": "2025-12-11T..."
}
```

### Drift Check
```bash
curl http://localhost:8000/drift
```

### Reporte Completo
```bash
curl http://localhost:8000/report
```

---

## 🔍 Demo: Detectar Drift

### 1. Estado Inicial (Sin Drift)

```bash
# Ver replicas actuales
kubectl get deployments

# nginx-app   3/3     3            3           1m

# Verificar sin drift
curl http://localhost:8000/drift | jq '.has_drift'
# false
```

### 2. Crear Drift Intencional

```bash
# Modificar replicas en cluster
kubectl scale deployment nginx-app --replicas=2

# Verificar cambio
kubectl get deployments
# nginx-app   2/2     2            2           2m
```

### 3. Detectar Drift

```bash
# Ejecutar drift check
curl http://localhost:8000/drift | jq

# Resultado esperado:
# "has_drift": true
# "drift_count": 1
# "differences": [
#   {
#     "type": "DRIFT",
#     "drifts": [{
#       "field": "replicas",
#       "desired": 3,
#       "actual": 2
#     }]
#   }
# ]
```

---

## 🧪 Ejecutar Tests

```bash
# Tests completos
pytest tests/ -v

# Con coverage
pytest tests/ --cov=app --cov-report=term

# Esperado: 12/12 tests PASSED
```

---

## 🐳 Docker (Opcional)

```bash
# Build y run
docker-compose up --build -d

# Verificar
curl http://localhost:8000/health

# Ver logs
docker-compose logs -f

# Detener
docker-compose down
```

---

## 🐛 Troubleshooting

### Problema: Pods en CrashLoopBackOff

**Solución:** Editar `k8s/deployment.yaml`

```yaml
# Comentar estas líneas:
# securityContext:
#   runAsNonRoot: true
#   runAsUser: 1000
```

Aplicar cambio:
```bash
kubectl apply -f k8s/deployment.yaml
```

### Problema: kubectl not found

```bash
# Windows (Chocolatey)
choco install kubernetes-cli

# Verificar
kubectl version --client
```

### Problema: API no detecta drift

```bash
# Verificar cluster
kubectl cluster-info

# Verificar recursos
kubectl get all

# Ver logs API
docker-compose logs -f
```

### Problema: Import errors en Python

```bash
# Reinstalar dependencias
python -m pip install -r requirements.txt --force-reinstall

# Ejecutar con python -m
python -m uvicorn app.main:app --reload
```

---

## 📝 Comandos Útiles

```bash
# Ver estado cluster
kubectl get all

# Ver logs de pod
kubectl logs <pod-name>

# Describir recurso
kubectl describe deployment nginx-app

# Ver evidencias generadas
cat .evidence/drift-report.json | jq

# Ejecutar drift check manual
python check_drift.py

# Limpiar cluster
kind delete cluster --name drift-detector
```

---

## 🎬 Flujo Completo

```bash
# 1. Setup
kind create cluster --name drift-detector
kubectl apply -f k8s/

# 2. Iniciar API (terminal 1)
python -m uvicorn app.main:app --reload

# 3. Probar sin drift (terminal 2)
curl http://localhost:8000/drift

# 4. Crear drift
kubectl scale deployment nginx-app --replicas=2

# 5. Detectar drift
curl http://localhost:8000/drift

# 6. Ver reporte
cat .evidence/drift-report.json | jq
```