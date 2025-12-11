# Carpeta .evidence/

Esta carpeta contiene las evidencias DevSecOps generadas por los pipelines de GitHub Actions.

## Archivos Generados

### CI Pipeline (ci.yml)
- `ci-report.txt`: Output completo de tests y cobertura
- `coverage.json`: Reporte de cobertura en formato JSON

### Build, Scan y SBOM Pipeline (build_scan_sbom.yml)
- `build-log.txt`: Log de construcción de la imagen Docker
- `trivy-report.json`: Reporte de vulnerabilidades en formato JSON
- `trivy-report.txt`: Reporte de vulnerabilidades en formato texto
- `sbom.json`: Software Bill of Materials en formato JSON
- `sbom.txt`: SBOM en formato texto con salida como tabla, para mayor legibilidad

### Drift Check Pipeline (drift_check.yml)
- `drift-report.json`: Reporte de configuration drift detectado

## Versionado

**IMPORTANTE**: Esta carpeta está versionada en Git (NO está en .gitignore).
