# Checklist de Verificación - Proyecto 11

<<<<<<< HEAD
=======
Mostramos los requerimientos y contenido que debe tener el proyecto al finalizar, para esto se tiene mapeado los pasos que se contemplaron para el desarrollo y ejecución.

>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b
## Pre-requisitos
- [ ] Python 3.11+ instalado
- [ ] pip actualizado
- [ ] kubectl instalado y configurado
- [ ] Acceso a cluster Kubernetes
- [ ] Docker y Docker Compose instalados (opcional)
- [ ] Git configurado

---

## Fase 1: Setup Local

### Instalación
- [ ] Copiar archivos a directorio local
- [ ] Navegar al directorio del proyecto
- [ ] Ejecutar `pip install -r requirements.txt`
- [ ] Verificar instalación: `python -c "import fastapi; print('OK')"`

### Verificación de Dependencias
```bash
# Ejecutar estos comandos y verificar que funcionen
kubectl version --client
python --version
docker --version  # opcional
```

---

## Fase 2: Tests

### Ejecutar Tests
- [ ] Ejecutar `pytest tests/ -v`
- [ ] Verificar que todos los tests pasen (✓)
- [ ] Ejecutar `pytest tests/ --cov=app --cov-report=term`
- [ ] Verificar coverage >70%
- [ ] Revisar reporte HTML: `pytest tests/ --cov=app --cov-report=html`

### Tests Esperados
```
test_health_endpoint ............................ PASSED
test_root_endpoint .............................. PASSED
test_drift_endpoint_structure ................... PASSED
test_report_endpoint_structure .................. PASSED
test_no_drift_when_states_match ................. PASSED
test_missing_resource_in_cluster ................ PASSED
test_extra_resource_in_cluster .................. PASSED
test_replica_drift_detection .................... PASSED
test_label_drift_detection ...................... PASSED
test_replicas_difference ........................ PASSED
test_missing_labels ............................. PASSED
test_no_drift_when_identical .................... PASSED
```

---

## Fase 3: API Local

### Iniciar API
- [ ] Ejecutar `uvicorn app.main:app --reload`
- [ ] Verificar mensaje: "Application startup complete"
- [ ] API corriendo en http://127.0.0.1:8000

### Probar Endpoints
```bash
# En otra terminal:

# 1. Health check
curl http://localhost:8000/health
# Esperado: {"status":"healthy","service":"config-drift-detector",...}

# 2. Root endpoint
curl http://localhost:8000/
# Esperado: Info del servicio con lista de endpoints

# 3. Drift check
curl http://localhost:8000/drift
# Esperado: {"has_drift":false/true,"drift_count":...}

# 4. Report
curl http://localhost:8000/report
# Esperado: Reporte completo con summary y details
```

- [ ] Todos los endpoints responden correctamente
- [ ] JSON válido en todas las respuestas
- [ ] Sin errores 500 en logs

---

## Fase 4: Docker (Opcional)

### Build y Run
- [ ] Ejecutar `docker-compose build`
- [ ] Build exitoso sin errores
- [ ] Ejecutar `docker-compose up -d`
- [ ] Contenedor corriendo: `docker ps`
- [ ] Health check OK: `docker ps` (healthy)

### Probar en Docker
- [ ] `curl http://localhost:8000/health`
- [ ] `curl http://localhost:8000/drift`
- [ ] Ver logs: `docker-compose logs -f`

### Cleanup
- [ ] Detener: `docker-compose down`

---

## Fase 5: Scripts Individuales

### Test de Scripts
```bash
# 1. Collect desired state
python app/scripts/collect_desired_state.py
# Esperado: Lista de recursos encontrados en k8s/

# 2. Collect actual state (requiere cluster)
python app/scripts/collect_actual_state.py
# Esperado: Lista de recursos del cluster

# 3. Manual drift check
python check_drift.py
# Esperado: Reporte completo en consola + archivo evidence/drift-report.json
```

- [ ] Scripts ejecutan sin errores
- [ ] Reporte JSON generado en evidence/

---

## Fase 6: Git y GitHub

### Local Git
- [ ] Navegar a directorio del proyecto
- [ ] `git init` (si no está inicializado)
- [ ] `git add .`
- [ ] `git status` - verificar archivos agregados
- [ ] `git commit -m "Initial commit: Config Drift Detector"`

### GitHub
- [ ] Crear repositorio en GitHub (si no existe)
- [ ] `git remote add origin <URL>`
- [ ] `git push -u origin main`
- [ ] Verificar archivos en GitHub
- [ ] Verificar estructura de directorios

---

## Fase 7: GitHub Actions

### CI Pipeline
- [ ] Ver en GitHub: Actions → "CI Pipeline"
- [ ] Pipeline se ejecutó automáticamente en push
- [ ] Todos los jobs pasaron (✓)
- [ ] Lint exitoso
- [ ] Tests exitosos
- [ ] Coverage >70%

### Drift Check Pipeline
- [ ] Configurar secret KUBECONFIG en GitHub
  - Settings → Secrets → New secret
  - Name: `KUBECONFIG`
  - Value: Contenido de ~/.kube/config
- [ ] GitHub → Actions → "Drift Check Pipeline"
- [ ] Click "Run workflow"
- [ ] Pipeline ejecuta correctamente
- [ ] Artifacts generados (drift-report)

---

## Fase 8: Funcionalidad de Drift Detection

### Setup Inicial
- [ ] Cluster Kubernetes disponible
- [ ] kubectl conectado: `kubectl cluster-info`
- [ ] Aplicar manifests: `kubectl apply -f k8s/`

### Test Sin Drift
- [ ] Ejecutar `curl http://localhost:8000/drift`
- [ ] Esperado: `"has_drift": false`

### Test Con Drift
- [ ] Crear drift intencional: `kubectl scale deployment nginx-app --replicas=2`
- [ ] Ejecutar `curl http://localhost:8000/drift`
- [ ] Esperado: `"has_drift": true`
- [ ] Verificar detalle del drift en respuesta
- [ ] Campo "replicas": desired=3, actual=2

### Test de Report
- [ ] Ejecutar `curl http://localhost:8000/report`
- [ ] Verificar summary con estadísticas
- [ ] Verificar by_type y by_severity
- [ ] Verificar details con lista de drifts

---

## Fase 9: Documentación

### Archivos de Documentación
- [ ] README.md existe y está completo
- [ ] QUICKSTART.md existe
- [ ] COMANDOS_GIT.md existe
- [ ] RESUMEN_PROYECTO.md existe (este archivo)
- [ ] Comentarios en código presentes

### Contenido
- [ ] README explica arquitectura
- [ ] README incluye ejemplos de uso
- [ ] README incluye troubleshooting
- [ ] QUICKSTART tiene comandos funcionales

---

## Fase 10: Limpieza y Verificación Final

### Estructura de Archivos
```bash
# Ejecutar en directorio del proyecto:
tree -L 2 -I '__pycache__|*.pyc|htmlcov|.pytest_cache'
```

<<<<<<< HEAD
Verificar estructura:
=======
Verificar estructura principal:
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b
```
.
├── .flake8
├── .github/
│   └── workflows/
├── .gitignore
├── Dockerfile
├── Makefile
├── QUICKSTART.md
├── README.md
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── scripts/
├── check_drift.py
├── docker-compose.yml
├── evidence/
│   └── .gitkeep
├── k8s/
│   ├── configmap.yaml
│   ├── deployment.yaml
│   └── service.yaml
├── pytest.ini
├── requirements.txt
└── tests/
    ├── __init__.py
    └── test_drift_detector.py
```

### Archivos Sensibles
- [ ] Verificar que .gitignore excluye:
  - `__pycache__/`
  - `.pytest_cache/`
  - `*.kubeconfig`
  - `evidence/*.json` (opcional)

### Limpieza
- [ ] Ejecutar `make clean` (o manual)
- [ ] Sin archivos __pycache__
- [ ] Sin archivos .pyc
- [ ] Sin .coverage o .pytest_cache

<<<<<<< HEAD
---

## Checklist de Entrega

### Código
- [x] API FastAPI funcional
- [x] Scripts de comparación
- [x] Manifests k8s de ejemplo
- [x] Tests con >70% coverage

### Infraestructura
- [x] Dockerfile funcional
- [x] docker-compose.yml
- [x] Makefile con comandos

### CI/CD
- [x] Pipeline de CI
- [x] Pipeline de drift check
- [x] Workflows de GitHub Actions

### Documentación
- [x] README.md completo
- [x] QUICKSTART.md
- [x] Comentarios en código
- [x] Este checklist

### Evidencia
- [ ] Screenshots de API funcionando
- [ ] Screenshots de tests pasando
- [ ] Screenshots de pipelines en GitHub
- [ ] Screenshot de drift detectado

---

## ✅ Proyecto Verificado y Listo para Entrega

**Fecha de verificación**: _______________

**Verificado por**: _______________

**Notas adicionales**:
_________________________________________________________
_________________________________________________________
_________________________________________________________

---

## 🎯 Próximos Pasos Post-Verificación

1. **Demo**: Preparar demostración del proyecto
2. **Presentación**: Crear slides si es requerido
3. **Video**: Grabar demo si es requerido
4. **Entrega**: Subir a plataforma del curso

---

## 📞 Troubleshooting

Si algo no funciona en el checklist:

1. **Tests fallan**:
   - Reinstalar dependencias: `pip install -r requirements.txt --force-reinstall`
   - Verificar Python 3.11+

2. **API no inicia**:
   - Verificar puerto 8000 disponible
   - Ver logs para errores

3. **kubectl no funciona**:
   - Verificar KUBECONFIG: `echo $KUBECONFIG`
   - Verificar acceso: `kubectl cluster-info`

4. **Docker falla**:
   - Verificar Docker corriendo: `docker ps`
   - Ver logs: `docker-compose logs`

5. **GitHub Actions falla**:
   - Verificar secret KUBECONFIG configurado
   - Ver logs en Actions tab
=======
---
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b
