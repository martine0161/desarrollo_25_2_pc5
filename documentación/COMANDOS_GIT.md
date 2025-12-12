<<<<<<< HEAD
# Comandos para subir el proyecto a Git

## Ejecutar desde Git Bash en Windows

### Paso 1: Ir al directorio del proyecto
```bash
cd "C:\Users\marti\OneDrive\Desktop\Ciclo 25-II\6.Desarrollo de Software\Repositorio\Examenes\avance\pc5_desarrollo"
```

### Paso 2: Copiar todos los archivos del proyecto
```bash
# Los archivos están en /mnt/user-data/outputs/pc5_desarrollo/
# Cópialos todos a tu directorio local
```

### Paso 3: Inicializar Git (si no está inicializado)
=======
# Comandos Git a tener en cuenta

## Ejecutar desde Git Bash

### Ir al directorio del proyecto

Tenemos el path del directorio donde se encuentra nuestro proyecto en `dir_path`, por ejemplo:

- Linux: `dir_path=/home/user/Documentos`
- Windows: `C:\Users\user\Documentos`
```bash
cd "dir_path/pc5_desarrollo"
```

### Copiar todos los archivos del proyecto
```bash
# Si iniciamos el proyecto, en el directorio actual generamos todos los archivos necesarios, si ya tenemos vasta con clonar el repositorio
```

### Inicializar Git (si no está inicializado)
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b
```bash
git init
```

<<<<<<< HEAD
### Paso 4: Agregar todos los archivos
```bash
git add .
```

### Paso 5: Ver qué archivos se agregarán
=======
### Agregar archivos para seguimiento en git
```bash
git add . # Todos los archivos
git add README.md pytest.ini # Agregar archivos específicos
```

### Ver estado de seguimiento de los archivos
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b
```bash
git status
```

<<<<<<< HEAD
### Paso 6: Hacer el primer commit
=======
### Hacer el primer commit

un ejemplo:

>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b
```bash
git commit -m "Initial commit: Config Drift Detector completo

- API FastAPI con endpoints /health, /drift, /report
- Scripts de comparación de estados k8s
- Tests con pytest (>70% coverage)
- Pipeline CI/CD con GitHub Actions
- Docker y docker-compose
- Documentación completa"
```

<<<<<<< HEAD
### Paso 7: Conectar con el repositorio remoto (si no está conectado)
=======
### Conectar con el repositorio remoto (si no está conectado)
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b
```bash
# Reemplaza <URL-DEL-REPO> con tu URL de GitHub
git remote add origin <URL-DEL-REPO>
```

<<<<<<< HEAD
### Paso 8: Verificar remote
=======
### Verificar remote
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b
```bash
git remote -v
```

<<<<<<< HEAD
### Paso 9: Push al repositorio
=======
### Crear ramas
```bash
# Crear nueva rama y navegar a ella
git branch nombre_rama
git checkout nombre_rama

# O hacemos lo mismo que lo anterior en una sola linea
git checkout -b nombre_rama
```

### Navegar entre ramas
```bash
git checkout nombre_rama
```

### Actualizar repositorio local

Antes de ejecutar el comando, navegar a la rama que desea actualizar
```bash
git pull
```


### Push al repositorio
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b
```bash
git push -u origin main
# o si tu rama principal es master:
# git push -u origin master
```

<<<<<<< HEAD
## Alternativa: Si el repo ya existe

Si ya tienes el repositorio clonado:

```bash
cd "C:\Users\marti\OneDrive\Desktop\Ciclo 25-II\6.Desarrollo de Software\Repositorio\Examenes\avance\pc5_desarrollo"

# Agregar todos los archivos
git add .

# Commit
git commit -m "Initial commit: Config Drift Detector"

# Push
git push origin main
```

## Verificar en GitHub

1. Ve a tu repositorio en GitHub
2. Verifica que todos los archivos estén presentes
3. Ve a "Actions" → verifica que los workflows aparezcan

## Estructura que deberías ver en GitHub

```
pc5_desarrollo/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── drift_check.yml
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── scripts/
│       ├── __init__.py
│       ├── collect_desired_state.py
│       ├── collect_actual_state.py
│       └── compare_states.py
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── configmap.yaml
├── tests/
│   ├── __init__.py
│   └── test_drift_detector.py
├── evidence/
│   └── .gitkeep
├── .flake8
├── .gitignore
├── check_drift.py
├── docker-compose.yml
├── Dockerfile
├── Makefile
├── pytest.ini
├── QUICKSTART.md
├── README.md
└── requirements.txt
```

## Notas importantes

- ⚠️ NO subas tu kubeconfig al repositorio (ya está en .gitignore)
- ⚠️ Para usar el workflow de drift_check.yml, necesitas configurar el secret KUBECONFIG en GitHub
- ✅ El workflow de CI se ejecutará automáticamente en cada push

## Configurar secret en GitHub (para drift_check.yml)

1. Ve a tu repo → Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `KUBECONFIG`
4. Value: El contenido de tu archivo ~/.kube/config
5. Click "Add secret"
=======
>>>>>>> de88fd9f0f4c4071238e1155dfc3f4ce7a85d54b
