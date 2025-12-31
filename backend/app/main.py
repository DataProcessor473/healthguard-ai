from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

app = FastAPI(
    title="HealthGuard AI API",
    description="Real-time Health Monitoring & Predictive Alert System",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "🏥 HealthGuard AI API",
        "status": "operational",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "docs": "/docs",
            "predict": "/api/v1/predict",
            "history": "/api/v1/history/{user_id}"
        }
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "services": {
            "api": "running",
            "ml_model": "ready",
            "database": "connected"
        }
    }

@app.get("/api/v1/version")
async def get_version():
    return {
        "name": "HealthGuard AI",
        "version": "1.0.0",
        "description": "Real-time Health Monitoring System"
    }

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
