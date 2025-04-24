from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')
CORS(app)  # Habilita CORS para todas as rotas

# Cache para armazenar as notícias
news_cache = {
    'last_update': None,
    'news': []
}

def fetch_draft5_data():
    """Busca dados do site Draft5"""
    urls = {
        'news': "https://draft5.gg/equipe/330-FURIA/noticias",
        'matches': "https://draft5.gg/proximas-partidas",
        'results': "https://draft5.gg/resultados",
        'tournaments': "https://draft5.gg/campeonatos"
    }
    
    try:
        # Aqui você implementaria o web scraping real
        # Por enquanto, retornamos dados mockados
        return True
    except Exception as e:
        print(f"Erro ao buscar dados: {str(e)}")
        return None

def fetch_furia_news():
    """Busca ou retorna do cache as notícias da FURIA"""
    global news_cache
    
    # Se o cache existe e tem menos de 5 minutos
    if (news_cache['last_update'] and 
        datetime.now() - news_cache['last_update'] < timedelta(minutes=5)):
        return news_cache['news']
    
    # Fallback para dados mockados se a busca falhar
    return [
        {
            "title": "FURIA é derrotada pela The MongolZ e está fora da PGL Bucharest 2025",
            "date": "09/04/2025",
            "link": "https://draft5.gg/partida/36342-FURIA-vs-The-MongolZ-PGL-Bucharest-2025"
        },
        {
            "title": "FURIA vence partida importante",
            "date": "2024-02-20",
            "link": "https://draft5.gg/noticias/furia-vence"
        },
        {
            "title": "Novo jogador na FURIA",
            "date": "2024-02-19",
            "link": "https://draft5.gg/noticias/novo-jogador"
        }
    ]

def process_chat_message(message):
    """Processa a mensagem do chat e retorna uma resposta apropriada"""
    message = message.lower()
    
    if "notícia" in message or "novidade" in message:
        news = fetch_furia_news()
        if news:
            latest_news = news[0]
            return f"A última notícia é: {latest_news['title']} ({latest_news['date']})"
        return "Desculpe, não consegui encontrar notícias recentes."
    
    elif "resultado" in message or "último jogo" in message:
        return "A FURIA foi derrotada pela The MongolZ por 2x0 na PGL Bucharest 2025."
    
    elif "próximo jogo" in message or "próxima partida" in message:
        return "O próximo compromisso da FURIA é a PGL Astana 2025, que será realizada entre os dias 10 e 18 de maio, no Cazaquistão."
    
    elif "campeonato" in message or "torneio" in message:
        return "A FURIA está classificada para a PGL Astana 2025, que acontecerá em maio no Cazaquistão."
    
    else:
        return "Desculpe, não entendi sua pergunta. Você pode perguntar sobre últimos resultados, próximos jogos, notícias recentes ou campeonatos."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/news')
def get_news():
    news = fetch_furia_news()
    return jsonify(news)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    response = process_chat_message(message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True) 