# Tablero Kanban - Proyecto 11: Config Drift Detector

<<<<<<< HEAD
## 📊 Herramienta Utilizada

**GitHub Projects** (recomendado) o Trello

URL del tablero: `https://github.com/users/USUARIO/projects/N` (reemplazar con tu URL real)

---

## 📋 Columnas del Tablero
=======
## Herramienta Utilizada

**GitHub Projects** document Markdown

Se creo este documento para llevar un registro detallado de las actividades para el proyecto.

---

## Detalle del Tablero

Columnas
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

```
┌─────────────┬─────────────┬─────────────┬─────────────┐
│  BACKLOG    │   DOING     │   REVIEW    │    DONE     │
│             │  (WIP: 2)   │             │             │
└─────────────┴─────────────┴─────────────┴─────────────┘
```

**Límite de WIP (Work In Progress)**: Máximo 2-3 tareas en "DOING" por persona

---

<<<<<<< HEAD
## 🎯 Sprint 1 (Días 1-2): Modelo de Estado + API Mínima
=======
## Sprint 1: Modelo de Estado + API Mínima
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

### Backlog → Doing → Done

#### Historia 1: Definir estructura de recursos
- **Descripción**: Definir estructura Python para representar recursos k8s
- **Tareas**:
  - [ ] Crear modelo de datos para Deployment, Service, ConfigMap
  - [ ] Definir campos clave: name, namespace, replicas, labels
- **Criterio de aceptación**: Tests unitarios para estructuras
<<<<<<< HEAD
- **PR**: `#1 - Define resource data structures`
=======
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

#### Historia 2: Implementar compare_states.py
- **Descripción**: Lógica de comparación entre estados
- **Tareas**:
  - [ ] Detectar recursos MISSING
  - [ ] Detectar recursos EXTRA
  - [ ] Detectar DRIFT (diferencias en replicas, labels)
- **Criterio de aceptación**: Tests con estados mockeados
<<<<<<< HEAD
- **PR**: `#2 - Implement state comparison logic`
=======
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

#### Historia 3: API /drift con mocks
- **Descripción**: Endpoint que use mocks de estados
- **Tareas**:
  - [ ] FastAPI con /health y /drift
  - [ ] /drift retorna drift_count y differences[]
  - [ ] Tests de endpoints
- **Criterio de aceptación**: curl /drift funciona con datos ficticios
<<<<<<< HEAD
- **PR**: `#3 - Add /drift endpoint with mocks`
=======
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

#### Historia 4: CI pipeline
- **Descripción**: GitHub Actions para lint y tests
- **Tareas**:
  - [ ] Crear .github/workflows/ci.yml
  - [ ] Lint con flake8
  - [ ] Tests con pytest
  - [ ] Coverage check >70%
- **Criterio de aceptación**: Pipeline pasa en PR
<<<<<<< HEAD
- **PR**: `#4 - Add CI pipeline`

**Evidencias Sprint 1**:
- ✅ `.evidence/ci-report.txt`
- ✅ Tests pasando (12/12)

---

## 🎯 Sprint 2 (Días 3-4): Integración con Manifests + Docker
=======

**Evidencias Sprint 1**:
- `.evidence/ci-report.txt`
- Tests pasando (12/12)

---

## Sprint 2: Integración con Manifests + Docker
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

### Backlog → Doing → Done

#### Historia 5: collect_desired_state.py
- **Descripción**: Leer manifests YAML de k8s/
- **Tareas**:
  - [ ] Parser de YAML con pyyaml
  - [ ] Leer Deployment, Service, ConfigMap
  - [ ] Retornar dict con recursos agrupados
- **Criterio de aceptación**: Lee k8s/ correctamente
<<<<<<< HEAD
- **PR**: `#5 - Implement desired state collector`
=======
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

#### Historia 6: Dockerfile y docker-compose
- **Descripción**: Contenerizar el servicio
- **Tareas**:
  - [ ] Dockerfile con Python 3.11-slim + kubectl
  - [ ] Non-root user
  - [ ] HEALTHCHECK configurado
  - [ ] docker-compose.yml con volúmenes
- **Criterio de aceptación**: `docker-compose up` funciona
<<<<<<< HEAD
- **PR**: `#6 - Add Docker configuration`
=======
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

#### Historia 7: drift_check.yml workflow
- **Descripción**: Pipeline que ejecuta comparación
- **Tareas**:
  - [ ] Job desired_state: lee k8s/
  - [ ] Job compare: ejecuta compare_states.py
  - [ ] Genera .evidence/drift-report.json
- **Criterio de aceptación**: Workflow ejecuta correctamente
<<<<<<< HEAD
- **PR**: `#7 - Add drift check workflow`
=======
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

#### Historia 8: Endpoint /report
- **Descripción**: Reporte completo con estadísticas
- **Tareas**:
  - [ ] Agrupa drifts por tipo (MISSING, EXTRA, DRIFT)
  - [ ] Agrupa por severidad (CRITICAL, HIGH, WARNING)
  - [ ] JSON con summary y details
- **Criterio de aceptación**: /report retorna estadísticas
<<<<<<< HEAD
- **PR**: `#8 - Add /report endpoint`

**Evidencias Sprint 2**:
- ✅ `.evidence/drift-report.json` (primera versión)
- ✅ `.evidence/build-log.txt`

---

## 🎯 Sprint 3 (Días 5-6): Minikube + Política de Bloqueo
=======

**Evidencias Sprint 2**:
- `.evidence/drift-report.json` (primera versión)
- `.evidence/build-log.txt`

---

## Sprint 3: Minikube + Política de Bloqueo
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

### Backlog → Doing → Done

#### Historia 9: collect_actual_state.py
- **Descripción**: Obtener estado real del cluster
- **Tareas**:
  - [ ] Ejecutar `kubectl get deploy,svc,cm -o json`
  - [ ] Parsear output JSON
  - [ ] Manejar errores de conexión
- **Criterio de aceptación**: Lee estado real de Minikube
<<<<<<< HEAD
- **PR**: `#9 - Implement actual state collector`
=======
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

#### Historia 10: Self-hosted runner
- **Descripción**: Configurar runner con acceso a cluster
- **Tareas**:
  - [ ] Setup self-hosted runner
  - [ ] Instalar Docker y kubectl
  - [ ] Actualizar drift_check.yml con runs-on: self-hosted
- **Criterio de aceptación**: Pipeline se ejecuta en self-hosted
<<<<<<< HEAD
- **PR**: `#10 - Configure self-hosted runner`
=======
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

#### Historia 11: Reglas de drift crítico
- **Descripción**: Políticas para bloquear deploy
- **Tareas**:
  - [ ] Detectar cambio en replicas -> CRITICAL
  - [ ] Detectar falta de securityContext -> CRITICAL
  - [ ] Detectar falta de NetworkPolicy -> HIGH
  - [ ] Pipeline falla si hay drift crítico
- **Criterio de aceptación**: Pipeline falla con drift crítico
<<<<<<< HEAD
- **PR**: `#11 - Add critical drift policies`
=======
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

#### Historia 12: Build, Scan & SBOM workflow
- **Descripción**: Pipeline de seguridad
- **Tareas**:
  - [ ] docker build de imagen
  - [ ] Scan con Trivy
  - [ ] Generar SBOM con Syft
  - [ ] Guardar reportes en .evidence/
- **Criterio de aceptación**: Genera trivy-report.json y sbom.json
<<<<<<< HEAD
- **PR**: `#12 - Add security scanning pipeline`

**Evidencias Sprint 3**:
- ✅ `.evidence/trivy-report.json`
- ✅ `.evidence/sbom.json`
- ✅ `.evidence/drift-report.json` (con cluster real)

---

## 📈 Métricas del Tablero

| Sprint | Tareas Completadas | Tareas Pendientes | WIP |
|--------|--------------------|-------------------|-----|
| Sprint 1 | 4/4 | 0 | 0 |
| Sprint 2 | 4/4 | 0 | 0 |
| Sprint 3 | 4/4 | 0 | 0 |

---

## 🎥 Evidencia en Videos

Cada video de sprint debe mostrar:
1. **Estado del tablero Kanban**
   - Qué tarjetas entraron y salieron
   - Qué está en DONE
2. **Tareas completadas**
   - PRs mergeados
   - Features funcionando
3. **Pipelines ejecutándose**
   - GitHub Actions en verde

---

## 📝 Notas

### Política de PRs
- Todo cambio entra vía Pull Request
- Prohibido merge directo a `main`
- Feature branches: `feature/nombre-descriptivo`
- Cada PR debe:
  - Tener descripción clara
  - Pasar CI antes de merge
  - Referenciarse en la tarjeta del Kanban

### Límite de WIP
- Máximo 2 tareas en "DOING" por persona
- Si DOING está lleno, completar antes de tomar nuevas tareas

### Evidencias por Sprint
- Sprint 1: ci-report.txt
- Sprint 2: drift-report.json, build-log.txt
- Sprint 3: trivy-report.json, sbom.json

---

## 🔗 Enlaces Útiles

- Repositorio: `https://github.com/USUARIO/REPO`
- Tablero Kanban: `https://github.com/users/USUARIO/projects/N`
- Actions: `https://github.com/USUARIO/REPO/actions`

---

**Última actualización**: Sprint 3 (Día 6)
=======

**Evidencias Sprint 3**:
- `.evidence/trivy-report.json`
- `.evidence/sbom.json`
- `.evidence/drift-report.json`

---
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b
