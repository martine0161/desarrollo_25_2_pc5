"""
FastAPI - Config Drift Detector API

Este módulo implementa la API REST para detectar configuration drift
entre manifests de Kubernetes y el estado real del cluster.

Endpoints disponibles:
    - GET /health: Health check del servicio
    - GET /drift: Detecta drift en tiempo real
    - GET /report: Reporte completo con estadísticas
    - GET /: Información del servicio

Author: Martin (Backend Team)
Sprint 3 - Mejoras de documentación
"""

from fastapi import FastAPI, HTTPException
from datetime import datetime
from app.scripts.collect_desired_state import get_desired_state
from app.scripts.collect_actual_state import get_actual_state
from app.scripts.compare_states import compare_states

app = FastAPI(
    title="Config Drift Detector",
    description="Detecta diferencias entre manifests k8s y estado real del cluster",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    """
    Health check endpoint.
    
    Verifica que el servicio está corriendo correctamente.
    
    Returns:
        dict: Estado del servicio con timestamp
        
    Example:
        >>> GET /health
        {
            "status": "healthy",
            "service": "config-drift-detector",
            "timestamp": "2024-12-05T12:00:00Z"
        }
    """
    return {
        "status": "healthy",
        "service": "config-drift-detector",
        "timestamp": datetime.utcnow().isoformat()
    }


@app.get("/drift")
def check_drift():
    """
    Endpoint principal: compara manifests del repo con estado real del cluster
    
    Returns:
        - has_drift: bool indicando si hay diferencias
        - differences: lista de diferencias detectadas
    """
    try:
        # 1. Obtener estado deseado (manifests)
        desired = get_desired_state("./k8s")
        
        # 2. Obtener estado actual (cluster)
        actual = get_actual_state()
        
        # 3. Comparar estados
        diff = compare_states(desired, actual)
        
        return {
            "has_drift": len(diff) > 0,
            "drift_count": len(diff),
            "differences": diff,
            "timestamp": datetime.utcnow().isoformat()
        }
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Error checking drift: {str(e)}"
        )


@app.get("/report")
def get_drift_report():
    """
    Genera reporte completo de drift con estadísticas
    
    Returns:
        Reporte detallado con resumen y detalles de drift
    """
    try:
        drift_data = check_drift()
        
        # Generar estadísticas
        differences = drift_data["differences"]
        
        stats = {
            "total_drifts": len(differences),
            "by_type": {},
            "by_severity": {}
        }
        
        for diff in differences:
            # Contar por tipo
            diff_type = diff.get("type", "UNKNOWN")
            stats["by_type"][diff_type] = stats["by_type"].get(diff_type, 0) + 1
            
            # Contar por severidad
            severity = diff.get("severity", "UNKNOWN")
            stats["by_severity"][severity] = stats["by_severity"].get(severity, 0) + 1
        
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "has_drift": drift_data["has_drift"],
            "summary": stats,
            "details": differences,
            "evidence_file": "/.evidence/drift-report.json"
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating report: {str(e)}"
        )


@app.get("/")
def root():
    """
    Root endpoint con información del servicio
    """
    return {
        "service": "Config Drift Detector",
        "version": "1.0.0",
        "endpoints": {
            "/health": "Health check",
            "/drift": "Check configuration drift",
            "/report": "Generate detailed drift report"
        }
    }
