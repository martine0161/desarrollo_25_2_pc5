# Proyecto 11 - Config Drift Detector
## Resumen Ejecutivo

### Proyecto Completo y Listo para Usar

---

## Contenido Generado

### Estructura del Proyecto
```
pc5_desarrollo/
├── app/                      # API FastAPI
│   ├── main.py              # 3 endpoints: /health, /drift, /report
│   └── scripts/             # Lógica de comparación
│       ├── collect_desired_state.py    # Lee manifests k8s/
│       ├── collect_actual_state.py     # Consulta cluster (kubectl)
│       └── compare_states.py           # Detecta drift
├── tests/                    # Tests con pytest (>70% coverage)
├── k8s/                      # Manifests de ejemplo (deployment, service, configmap)
├── .github/workflows/        # CI/CD
│   ├── ci.yml               # Lint + Tests automáticos
│   └── drift_check.yml      # Drift check bajo demanda
├── Dockerfile               # Imagen con kubectl + Python
├── docker-compose.yml       # Stack completo
├── Makefile                 # Comandos automatizados
├── README.md                # Documentación principal
└── documentación
```

---

## Funcionalidades Implementadas

### API FastAPI
- **GET /health**: Health check
- **GET /drift**: Detecta drift en tiempo real
- **GET /report**: Reporte completo con estadísticas

### Scripts Python
1. **collect_desired_state.py**: Lee manifests YAML del repo
2. **collect_actual_state.py**: Consulta cluster con kubectl
3. **compare_states.py**: Compara y detecta diferencias

### Detección de Drift
Detecta 3 tipos:
- **MISSING** (Critical): Recurso en manifests pero no en cluster
- **EXTRA** (Warning): Recurso en cluster pero no en manifests  
- **DRIFT** (High): Recurso existe pero con diferencias

Compara:
- Replicas (Deployments)
- Labels (metadata)
- SecurityContext
- Resources
- Spec completo

### Tests (pytest)
- 15+ tests unitarios e integración
- Coverage >70% requerido
- Tests de API, comparación, detección de drift

### Pipeline DevSecOps
**CI Pipeline (automático)**:
- Lint con flake8
- Tests con pytest
- Coverage report
- Falla si coverage <70%

**Drift Check Pipeline (bajo demanda)**:
- Lee estado deseado y actual
- Genera reporte JSON
- Falla si hay drift crítico

### Docker
- Dockerfile multi-stage con kubectl
- docker-compose con volúmenes
- Health checks configurados

### Documentación
- QUICKSTART.md (setup en 5 minutos)
- COMANDOS_GIT.md (guía para subir a GitHub)
- Comentarios en código

---
