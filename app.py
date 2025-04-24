from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import os

app = FastAPI()

# Configuração dos templates e arquivos estáticos
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")
templates = Jinja2Templates(directory="templates")

# Cache para armazenar notícias (em produção, use um banco de dados)
news_cache = {
    "last_update": None,
    "news": []
}

async def fetch_furia_news():
    """
    Função para buscar notícias sobre a FURIA de CS:GO
    Por enquanto retorna dados mockados, mas pode ser integrada com APIs reais
    """
    # Exemplo de dados mockados
    return [
        {
            "title": "FURIA vence importante partida no ESL Pro League",
            "date": datetime.now().strftime("%d/%m/%Y"),
            "content": "A FURIA demonstra grande forma no campeonato...",
            "source": "ESL"
        },
        {
            "title": "Novo jogador se junta à equipe",
            "date": datetime.now().strftime("%d/%m/%Y"),
            "content": "A FURIA anuncia nova contratação...",
            "source": "FURIA Esports"
        }
    ]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/news")
async def get_news():
    """
    Endpoint para retornar notícias sobre a FURIA
    """
    # Atualiza o cache a cada 5 minutos
    if not news_cache["last_update"] or (datetime.now() - news_cache["last_update"]).seconds > 300:
        news_cache["news"] = await fetch_furia_news()
        news_cache["last_update"] = datetime.now()
    
    return {"news": news_cache["news"]}

@app.post("/api/chat")
async def chat(message: dict):
    """
    Endpoint para processar mensagens do chat
    """
    user_message = message.get("message", "").lower()
    
    # Respostas básicas (pode ser expandido com NLP)
    if "furia" in user_message:
        return {"response": "A FURIA é uma das melhores equipes de CS:GO do Brasil!"}
    elif "jogadores" in user_message:
        return {"response": "Os jogadores atuais da FURIA são: KSCERATO, yuurih, arT, VINI e saffee"}
    elif "próximo jogo" in user_message:
        return {"response": "O próximo jogo da FURIA será anunciado em breve. Fique ligado!"}
    else:
        return {"response": "Desculpe, não entendi sua pergunta. Você pode perguntar sobre jogadores, próximos jogos ou notícias da FURIA."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 