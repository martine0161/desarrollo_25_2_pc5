# Índice - PC5 Config Drift Detector

**Fecha:** 11-12-2025

---

## 📚 Documentación Disponible

### [README.md](README.md)
Documentación técnica completa del proyecto.
- Arquitectura y componentes
- Endpoints de la API
- Instalación y configuración
- Stack tecnológico

### [RESUMEN.md](RESUMEN.md)
Resumen ejecutivo del proyecto.
- Qué se implementó
- Funcionalidades principales
- Estado del proyecto

### [QUICKSTART.md](QUICKSTART.md)
Guía de inicio rápido.
- Setup en 5 minutos
- Comandos esenciales
- Troubleshooting básico

---

## 🗂️ Estructura del Proyecto

```
pc5_desarrollo/
├── app/                    # API FastAPI
├── tests/                  # Tests (pytest)
├── k8s/                    # Manifests Kubernetes
├── .github/workflows/      # CI/CD pipelines
├── documentación/          # Esta carpeta
├── requirements.txt
└── README.md
```

---

## 🚀 Inicio Rápido

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Ejecutar API
python -m uvicorn app.main:app --reload

# 3. Probar
curl http://localhost:8000/health
```

---

## 🔗 Enlaces Útiles

- **Repositorio:** [GitHub](https://github.com/martine0161/desarrollo_25_2_pc5)
- **CI Pipeline:** [.github/workflows/ci.yml](.github/workflows/ci.yml)
- **Tests:** [tests/test_drift_detector.py](tests/test_drift_detector.py)
