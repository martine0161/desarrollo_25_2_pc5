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
```bash
git init
```

### Agregar archivos para seguimiento en git
```bash
git add . # Todos los archivos
git add README.md pytest.ini # Agregar archivos específicos
```

### Ver estado de seguimiento de los archivos
```bash
git status
```

### Hacer el primer commit

un ejemplo:

```bash
git commit -m "Initial commit: Config Drift Detector completo

- API FastAPI con endpoints /health, /drift, /report
- Scripts de comparación de estados k8s
- Tests con pytest (>70% coverage)
- Pipeline CI/CD con GitHub Actions
- Docker y docker-compose
- Documentación completa"
```

### Conectar con el repositorio remoto (si no está conectado)
```bash
# Reemplaza <URL-DEL-REPO> con tu URL de GitHub
git remote add origin <URL-DEL-REPO>
```

### Verificar remote
```bash
git remote -v
```

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
```bash
git push -u origin main
# o si tu rama principal es master:
# git push -u origin master
```

