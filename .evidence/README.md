# Carpeta .evidence/

Esta carpeta contiene las evidencias DevSecOps generadas por los pipelines de GitHub Actions.

## Archivos Generados

### CI Pipeline (ci.yml)
- `ci-report.txt`: Output completo de tests y cobertura
- `coverage.json`: Reporte de cobertura en formato JSON

<<<<<<< HEAD
### Build, Scan & SBOM Pipeline (build_scan_sbom.yml)
=======
### Build, Scan y SBOM Pipeline (build_scan_sbom.yml)
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b
- `build-log.txt`: Log de construcción de la imagen Docker
- `trivy-report.json`: Reporte de vulnerabilidades en formato JSON
- `trivy-report.txt`: Reporte de vulnerabilidades en formato texto
- `sbom.json`: Software Bill of Materials en formato JSON
<<<<<<< HEAD
- `sbom.txt`: SBOM en formato tabla legible
=======
- `sbom.txt`: SBOM en formato texto con salida como tabla, para mayor legibilidad
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b

### Drift Check Pipeline (drift_check.yml)
- `drift-report.json`: Reporte de configuration drift detectado

## Versionado

<<<<<<< HEAD
⚠️ **IMPORTANTE**: Esta carpeta está versionada en Git (NO está en .gitignore).

Cada sprint debe agregar al menos una evidencia nueva aquí.

## Sprints

### Sprint 1 (Días 1-2)
- ✅ ci-report.txt (primera versión)
- ✅ coverage.json

### Sprint 2 (Días 3-4)
- ✅ build-log.txt
- ✅ drift-report.json (primera versión con datos simulados)

### Sprint 3 (Días 5-6)
- ✅ trivy-report.json
- ✅ sbom.json
- ✅ drift-report.json (versión con cluster real)
=======
**IMPORTANTE**: Esta carpeta está versionada en Git (NO está en .gitignore).
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b
