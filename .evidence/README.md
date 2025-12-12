# 📂 Carpeta .evidence/

Esta carpeta almacena las **evidencias DevSecOps** generadas automáticamente por los pipelines de GitHub Actions.

> ⚠️ **IMPORTANTE:** Esta carpeta **se versiona en Git** (no está en `.gitignore`) para mantener un historial de auditoría de cada Sprint.

## 📄 Archivos Generados

| Pipeline | Archivos | Descripción |
| :--- | :--- | :--- |
| **🧪 CI** | `ci-report.txt`<br>`coverage.json` | Resultados de tests y porcentaje de cobertura. |
| **🛡️ Build & Scan** | `build-log.txt`<br>`trivy-report.*`<br>`sbom.*` | Logs de Docker, reportes de vulnerabilidades y lista de materiales de software (SBOM). |
| **⚙️ Drift** | `drift-report.json` | Reporte de desviaciones de configuración (drift). |

## 📅 Progreso por Sprint

* **Sprint 1:** ✅ Tests y Cobertura (`ci-report`, `coverage`).
* **Sprint 2:** ✅ Build Docker y Drift simulado (`build-log`, `drift-report`).
* **Sprint 3:** ✅ Seguridad y Drift real (`trivy`, `sbom`, `drift-report` actualizado).