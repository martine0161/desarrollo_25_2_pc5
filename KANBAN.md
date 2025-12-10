# Tablero Kanban - Proyecto 11: Config Drift Detector

## Herramienta Utilizada

**GitHub Projects** document Markdown

Se creo este documento para llevar un registro detallado de las actividades para el proyecto.

---

## Detalle del Tablero

Columnas

```
┌─────────────┬─────────────┬─────────────┬─────────────┐
│  BACKLOG    │   DOING     │   REVIEW    │    DONE     │
│             │  (WIP: 2)   │             │             │
└─────────────┴─────────────┴─────────────┴─────────────┘
```

**Límite de WIP (Work In Progress)**: Máximo 2-3 tareas en "DOING" por persona

---

## Sprint 1: Modelo de Estado + API Mínima

### Backlog → Doing → Done

#### Historia 1: Definir estructura de recursos
- **Descripción**: Definir estructura Python para representar recursos k8s
- **Tareas**:
  - [ ] Crear modelo de datos para Deployment, Service, ConfigMap
  - [ ] Definir campos clave: name, namespace, replicas, labels
- **Criterio de aceptación**: Tests unitarios para estructuras

#### Historia 2: Implementar compare_states.py
- **Descripción**: Lógica de comparación entre estados
- **Tareas**:
  - [ ] Detectar recursos MISSING
  - [ ] Detectar recursos EXTRA
  - [ ] Detectar DRIFT (diferencias en replicas, labels)
- **Criterio de aceptación**: Tests con estados mockeados

#### Historia 3: API /drift con mocks
- **Descripción**: Endpoint que use mocks de estados
- **Tareas**:
  - [ ] FastAPI con /health y /drift
  - [ ] /drift retorna drift_count y differences[]
  - [ ] Tests de endpoints
- **Criterio de aceptación**: curl /drift funciona con datos ficticios

#### Historia 4: CI pipeline
- **Descripción**: GitHub Actions para lint y tests
- **Tareas**:
  - [ ] Crear .github/workflows/ci.yml
  - [ ] Lint con flake8
  - [ ] Tests con pytest
  - [ ] Coverage check >70%
- **Criterio de aceptación**: Pipeline pasa en PR

**Evidencias Sprint 1**:
- `.evidence/ci-report.txt`
- Tests pasando (12/12)

---

## Sprint 2: Integración con Manifests + Docker

### Backlog → Doing → Done

#### Historia 5: collect_desired_state.py
- **Descripción**: Leer manifests YAML de k8s/
- **Tareas**:
  - [ ] Parser de YAML con pyyaml
  - [ ] Leer Deployment, Service, ConfigMap
  - [ ] Retornar dict con recursos agrupados
- **Criterio de aceptación**: Lee k8s/ correctamente

#### Historia 6: Dockerfile y docker-compose
- **Descripción**: Contenerizar el servicio
- **Tareas**:
  - [ ] Dockerfile con Python 3.11-slim + kubectl
  - [ ] Non-root user
  - [ ] HEALTHCHECK configurado
  - [ ] docker-compose.yml con volúmenes
- **Criterio de aceptación**: `docker-compose up` funciona

#### Historia 7: drift_check.yml workflow
- **Descripción**: Pipeline que ejecuta comparación
- **Tareas**:
  - [ ] Job desired_state: lee k8s/
  - [ ] Job compare: ejecuta compare_states.py
  - [ ] Genera .evidence/drift-report.json
- **Criterio de aceptación**: Workflow ejecuta correctamente

#### Historia 8: Endpoint /report
- **Descripción**: Reporte completo con estadísticas
- **Tareas**:
  - [ ] Agrupa drifts por tipo (MISSING, EXTRA, DRIFT)
  - [ ] Agrupa por severidad (CRITICAL, HIGH, WARNING)
  - [ ] JSON con summary y details
- **Criterio de aceptación**: /report retorna estadísticas

**Evidencias Sprint 2**:
- `.evidence/drift-report.json` (primera versión)
- `.evidence/build-log.txt`

---

## Sprint 3: Minikube + Política de Bloqueo

### Backlog → Doing → Done

#### Historia 9: collect_actual_state.py
- **Descripción**: Obtener estado real del cluster
- **Tareas**:
  - [ ] Ejecutar `kubectl get deploy,svc,cm -o json`
  - [ ] Parsear output JSON
  - [ ] Manejar errores de conexión
- **Criterio de aceptación**: Lee estado real de Minikube

#### Historia 10: Self-hosted runner
- **Descripción**: Configurar runner con acceso a cluster
- **Tareas**:
  - [ ] Setup self-hosted runner
  - [ ] Instalar Docker y kubectl
  - [ ] Actualizar drift_check.yml con runs-on: self-hosted
- **Criterio de aceptación**: Pipeline se ejecuta en self-hosted

#### Historia 11: Reglas de drift crítico
- **Descripción**: Políticas para bloquear deploy
- **Tareas**:
  - [ ] Detectar cambio en replicas -> CRITICAL
  - [ ] Detectar falta de securityContext -> CRITICAL
  - [ ] Detectar falta de NetworkPolicy -> HIGH
  - [ ] Pipeline falla si hay drift crítico
- **Criterio de aceptación**: Pipeline falla con drift crítico

#### Historia 12: Build, Scan & SBOM workflow
- **Descripción**: Pipeline de seguridad
- **Tareas**:
  - [ ] docker build de imagen
  - [ ] Scan con Trivy
  - [ ] Generar SBOM con Syft
  - [ ] Guardar reportes en .evidence/
- **Criterio de aceptación**: Genera trivy-report.json y sbom.json

**Evidencias Sprint 3**:
- `.evidence/trivy-report.json`
- `.evidence/sbom.json`
- `.evidence/drift-report.json`

---
