# Índice de Navegación - Proyecto 11

Guía rápida para navegar todos los archivos del proyecto.

---

## EMPIEZA AQUÍ

1. **RESUMEN_PROYECTO.md** ← ¡LEE ESTO PRIMERO!
   - Resumen ejecutivo completo
   - Qué se generó y por qué
   - Estado del proyecto

2. **QUICKSTART.md** ← Setup en 5 minutos
   - Comandos rápidos para empezar
   - Troubleshooting básico

3. **COMANDOS_GIT.md** ← Para subir a GitHub
   - Comandos Git paso a paso
   - Configuración de secrets

4. **CHECKLIST_VERIFICACION.md** ← Verificar que todo funcione
   - Checklist completo de verificación
   - Tests a ejecutar
   - Troubleshooting detallado

---

## Documentación Principal

### README.md
- **Qué es**: Documentación técnica completa del proyecto
- **Cuándo leer**: Para entender la arquitectura y detalles
- **Contiene**:
  - Descripción del proyecto
  - Arquitectura y stack
  - Endpoints de la API
  - Guía de instalación
  - Guía de uso
  - Configuración
  - Troubleshooting

---

## Código del Proyecto

### Backend (Python/FastAPI)

**app/main.py**
- API FastAPI con 3 endpoints
- /health, /drift, /report
- Orquesta los scripts de comparación

**app/scripts/collect_desired_state.py**
- Lee manifests YAML del directorio k8s/
- Extrae estado deseado

**app/scripts/collect_actual_state.py**
- Consulta cluster con kubectl
- Obtiene estado real

**app/scripts/compare_states.py**
- Compara estados deseado vs actual
- Detecta drift (MISSING, EXTRA, DRIFT)
- Compara replicas, labels, securityContext

---

## Tests

**tests/test_drift_detector.py**
- 15+ tests unitarios e integración
- Tests de API endpoints
- Tests de lógica de comparación
- Tests de detección de drift
- Coverage target: >70%

**pytest.ini**
- Configuración de pytest
- Coverage settings

**.flake8**
- Configuración de linter

---

## Docker

**Dockerfile**
- Imagen con Python + kubectl
- Multi-stage build
- Health checks

**docker-compose.yml**
- Stack completo con volúmenes
- Monta k8s/ y .kube/
- Expone puerto 8000

---

## Kubernetes Manifests

**k8s/deployment.yaml**
- Deployment de ejemplo (nginx-app)
- 3 replicas
- SecurityContext configurado

**k8s/service.yaml**
- Service de ejemplo
- ClusterIP

**k8s/configmap.yaml**
- ConfigMap de ejemplo

---

## CI/CD (GitHub Actions)

**.github/workflows/ci.yml**
- Pipeline de CI (automático)
- Lint + Tests
- Coverage check

**.github/workflows/drift_check.yml**
- Pipeline de drift check (manual)
- Ejecuta comparación
- Genera reporte
- Falla si hay drift crítico

---

## Utilidades

**Makefile**
- Comandos automatizados
- make install, test, run, etc.

**setup.sh**
- Script de setup automático
- Verifica dependencias
- Instala packages
- Ejecuta tests

**check_drift.py**
- Script standalone para drift check
- Genera reporte JSON
- Útil para debugging

---

## Configuración

**requirements.txt**
- Dependencias Python
- FastAPI, pytest, etc.

**.gitignore**
- Archivos a ignorar en Git
- __pycache__, venv, etc.

---

## Directorio evidence/

**evidence/.gitkeep**
- Placeholder para Git
- Aquí se guardan reportes JSON generados

---