from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
from datetime import datetime
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Inicializa a aplicação FastAPI
app = FastAPI(
    title="FURIA Insight Engine",
    description="API para análise e compreensão do perfil dos fãs da FURIA",
    version="1.0.0"
)

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique os domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos de dados
class FanProfile(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    location: str
    gender: str
    interests: List[str]
    social_media: dict
    engagement_score: float
    created_at: datetime = datetime.now()

class SocialMediaData(BaseModel):
    platform: str
    username: str
    followers: int
    posts: int
    engagement_rate: float

# Rotas da API
@app.get("/")
async def root():
    """Rota principal da API"""
    return {
        "message": "Bem-vindo à FURIA Insight Engine API",
        "version": "1.0.0",
        "status": "online"
    }

@app.get("/health")
async def health_check():
    """Verifica o status da API"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }

@app.post("/fans/profile")
async def create_fan_profile(profile: FanProfile):
    """Cria um novo perfil de fã"""
    try:
        # Aqui você implementará a lógica para salvar no banco de dados
        return {
            "message": "Perfil criado com sucesso",
            "profile": profile
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/fans/{fan_id}")
async def get_fan_profile(fan_id: int):
    """Obtém o perfil de um fã específico"""
    try:
        # Aqui você implementará a lógica para buscar no banco de dados
        return {
            "message": "Perfil encontrado",
            "fan_id": fan_id
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail="Perfil não encontrado")

@app.get("/analytics/engagement")
async def get_engagement_analytics():
    """Obtém análises de engajamento"""
    try:
        # Aqui você implementará a lógica para análise de engajamento
        return {
            "total_fans": 1000,
            "average_engagement": 0.75,
            "top_platforms": ["Twitter", "Instagram", "Twitch"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Execução do servidor
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    ) 