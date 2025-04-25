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

def fetch_furia_results():
    """Retorna os últimos resultados da FURIA"""
    return [
        {
            "data": "08/04/2025",
            "adversario": "Virtus.pro",
            "resultado": "0-2",
            "torneio": "PGL Bucharest 2025",
            "placares": {
                "Anubis": "11-13",
                "Dust2": "8-13",
                "Mirage": "0-5"
            },
            "estatisticas": {
                "FURIA": {
                    "KSCERATO": {"K/D": "31/28", "K/D DIFF": "+3", "ADR": "80.1", "KAST": "70.55%", "Rating": "1.11"},
                    "chelo": {"K/D": "27/31", "K/D DIFF": "-4", "ADR": "62.15", "KAST": "71.1%", "Rating": "0.99"},
                    "yuurih": {"K/D": "20/29", "K/D DIFF": "-9", "ADR": "54.5", "KAST": "70.85%", "Rating": "0.84"},
                    "FalleN": {"K/D": "27/34", "K/D DIFF": "-7", "ADR": "63.55", "KAST": "61.91%", "Rating": "0.84"},
                    "skullz": {"K/D": "16/28", "K/D DIFF": "-12", "ADR": "39.71", "KAST": "66.35%", "Rating": "0.64"}
                },
                "Virtus.pro": {
                    "ICY": {"K/D": "30/20", "K/D DIFF": "+10", "ADR": "72.95", "KAST": "84.85%", "Rating": "1.25"},
                    "fame": {"K/D": "31/24", "K/D DIFF": "+7", "ADR": "64.45", "KAST": "84.5%", "Rating": "1.19"},
                    "electroNic": {"K/D": "34/32", "K/D DIFF": "+2", "ADR": "88", "KAST": "64.6%", "Rating": "1.15"},
                    "FL4MUS": {"K/D": "30/24", "K/D DIFF": "+6", "ADR": "72.6", "KAST": "81.56%", "Rating": "1.12"},
                    "FL1T": {"K/D": "25/21", "K/D DIFF": "+4", "ADR": "73.85", "KAST": "79.75%", "Rating": "1.08"}
                }
            }
        },
        {
            "data": "07/04/2025",
            "adversario": "Complexity",
            "resultado": "1-2",
            "torneio": "PGL Bucharest 2025",
            "placares": {
                "Dust2": "13-8",
                "Train": "1-13",
                "Inferno": "4-13"
            },
            "estatisticas": {
                "FURIA": {
                    "KSCERATO": {"K/D": "33/37", "K/D DIFF": "-4", "ADR": "81.7", "KAST": "60.84%", "Rating": "1.06"},
                    "yuurih": {"K/D": "32/41", "K/D DIFF": "-9", "ADR": "71.9", "KAST": "62.44%", "Rating": "0.93"},
                    "chelo": {"K/D": "33/40", "K/D DIFF": "-7", "ADR": "62.57", "KAST": "63.27%", "Rating": "0.89"},
                    "skullz": {"K/D": "27/44", "K/D DIFF": "-17", "ADR": "63.57", "KAST": "64.84%", "Rating": "0.71"},
                    "FalleN": {"K/D": "25/41", "K/D DIFF": "-16", "ADR": "49.07", "KAST": "56.5%", "Rating": "0.63"}
                },
                "Complexity": {
                    "JT": {"K/D": "44/25", "K/D DIFF": "+19", "ADR": "101.57", "KAST": "71.97%", "Rating": "1.51"},
                    "Grim": {"K/D": "45/34", "K/D DIFF": "+11", "ADR": "95.27", "KAST": "79.1%", "Rating": "1.42"},
                    "cxzi": {"K/D": "42/30", "K/D DIFF": "+12", "ADR": "83.24", "KAST": "70.3%", "Rating": "1.25"}
                }
            }
        },
        {
            "data": "06/04/2025",
            "adversario": "Apogee",
            "resultado": "2-0",
            "torneio": "PGL Bucharest 2025",
            "placares": {
                "Mirage": "13-7",
                "Inferno": "13-5"
            },
            "estatisticas": {
                "FURIA": {
                    "KSCERATO": {"K/D": "35/25", "K/D DIFF": "+10", "ADR": "85.2", "KAST": "72.5%", "Rating": "1.25"},
                    "yuurih": {"K/D": "30/28", "K/D DIFF": "+2", "ADR": "75.8", "KAST": "68.3%", "Rating": "1.15"},
                    "chelo": {"K/D": "28/26", "K/D DIFF": "+2", "ADR": "70.1", "KAST": "65.8%", "Rating": "1.08"},
                    "skullz": {"K/D": "25/24", "K/D DIFF": "+1", "ADR": "68.9", "KAST": "64.2%", "Rating": "1.05"},
                    "FalleN": {"K/D": "24/25", "K/D DIFF": "-1", "ADR": "65.4", "KAST": "62.1%", "Rating": "0.98"}
                }
            }
        },
        {
            "data": "05/04/2025",
            "adversario": "M80",
            "resultado": "2-1",
            "torneio": "BLAST Open Lisbon 2025",
            "placares": {
                "Ancient": "13-11",
                "Nuke": "8-13",
                "Inferno": "13-7"
            },
            "estatisticas": {
                "FURIA": {
                    "KSCERATO": {"K/D": "38/32", "K/D DIFF": "+6", "ADR": "82.3", "KAST": "71.2%", "Rating": "1.18"},
                    "yuurih": {"K/D": "35/30", "K/D DIFF": "+5", "ADR": "78.9", "KAST": "69.8%", "Rating": "1.12"},
                    "chelo": {"K/D": "32/34", "K/D DIFF": "-2", "ADR": "72.4", "KAST": "66.5%", "Rating": "1.05"},
                    "skullz": {"K/D": "30/35", "K/D DIFF": "-5", "ADR": "70.2", "KAST": "65.1%", "Rating": "0.98"},
                    "FalleN": {"K/D": "28/36", "K/D DIFF": "-8", "ADR": "68.9", "KAST": "63.4%", "Rating": "0.95"}
                }
            }
        }
    ]

def process_chat_message(message):
    """Processa a mensagem do chat e retorna uma resposta apropriada"""
    message = message.lower()
    
    if "tchau" in message or "até logo" in message or "adeus" in message or "muito obrigado" in message or "obrigado" in message or "flw" in message:
        return "Valeu, torcedor! Vamo que vamo com a FURIA! 🐯🔥 #VamoFURIA"
    
    elif "notícia" in message or "novidade" in message or "noticia" in message or "noticias" in message or "novidades" in message:
        news = fetch_furia_news()
        if news:
            latest_news = news[0]
            response = f"A última notícia é: {latest_news['title']} ({latest_news['date']})\n\n"
            response += "Precisa de mais alguma informação, torcedor?🐯🔥\nPosso te ajudar com:\n"
            response += "- Últimos resultados\n"
            response += "- Próximos jogos\n"
            response += "- Notícias recentes\n"
            response += "- Estatísticas dos jogos\n"
            response += "- Campeonatos\n\n"
            # Aqui é onde você converte para HTML com <br>
            response_html = response.replace("\n", "<br>")
            return response_html
            return response
        return "Desculpe, não consegui encontrar notícias recentes."
    
    elif "resultado do" in message or "último jogo" in message or "ultimo jogo" in message or "ultimo resultado da" in message:
        results = fetch_furia_results()
        if results:
            latest_result = results[0]
            response = "🎮 ÚLTIMO JOGO DA FURIA 🎮\n"
            response += "=" * 40 + "\n\n"
            response += f"🏆 Torneio: {latest_result['torneio']}\n"
            response += f"📅 Data: {latest_result['data']}\n"
            response += f"⚔️ Adversário: {latest_result['adversario']}\n"
            response += f"📊 Resultado Final: {latest_result['resultado']}\n\n"
            response += "🗺️ PLACARES POR MAPA:\n"
            response += "-" * 20 + "\n"
            for mapa, placar in latest_result['placares'].items():
                response += f"• {mapa}: {placar}\n"
            response += "\n" + "=" * 40 + "\n\n"
            response += "❓ Deseja ver as estatísticas detalhadas deste jogo?\n"
            
            def process_chat_message(message):
                    """Processa a mensagem do chat e retorna uma resposta apropriada"""
                    message = message.lower()
                    if "sim" in message or "estatísticas" in message:
                        results = fetch_furia_results()
                        if results:
                            latest_result = results[0]
                            response = "📊 ESTATÍSTICAS DO ÚLTIMO JOGO 📊\n"
                            response += "=" * 40 + "\n\n"
                            response += f"⚔️ FURIA vs {latest_result['adversario']}\n"
                            response += f"📅 {latest_result['data']}\n\n"
                            
                            response += "🐯 FURIA:\n"
                            response += "-" * 20 + "\n"
                            for jogador, stats in latest_result['estatisticas']['FURIA'].items():
                                response += f"\n{jogador}:\n"
                                for stat, valor in stats.items():
                                    response += f"• {stat}: {valor}\n"
                            
                            if latest_result['adversario'] in latest_result['estatisticas']:
                                response += f"\n⚔️ {latest_result['adversario']}:\n"
                                response += "-" * 20 + "\n"
                                for jogador, stats in latest_result['estatisticas'][latest_result['adversario']].items():
                                    response += f"\n{jogador}:\n"
                                    for stat, valor in stats.items():
                                        response += f"• {stat}: {valor}\n"
                            
                            response += "\n" + "=" * 40 + "\n\n"
                            response += "💡 Precisa de mais alguma informação, torcedor?🐯🔥\n"
                            response += "   Posso te ajudar com:\n"
                            response += "- Últimos resultados\n"
                            response += "- Próximos jogos\n"
                            response += "- Notícias recentes\n"
                            response += "- Estatísticas dos jogos\n"
                            response += "- Campeonatos\n\n"

                    elif "não" in message or "nao" in message or "Não" in message or "Nao" in message:
                        if "estatísticas" in message:
                            response = "💡 Precisa de mais alguma informação, torcedor?🐯🔥\n"
                            response += "   Posso te ajudar com:\n"
                            response += "- Últimos resultados\n"
                            response += "- Próximos jogos\n"
                            response += "- Notícias recentes\n"
                            response += "- Estatísticas dos jogos\n"
                            response += "- Campeonatos\n\n"
                            # Aqui é onde você converte para HTML com <br>
                            response_html = response.replace("\n", "<br>")
                            return response_html
                            return response
                        return "Valeu, torcedor! Vamo que vamo com a FURIA! 🐯🔥 #VamoFURIA"
                    
            # Aqui é onde você converte para HTML com <br>
            response_html = response.replace("\n", "<br>")
            return response_html
            return response
        return "Desculpe, não consegui encontrar o resultado do último jogo."
    
    elif "últimos jogos" in message or "histórico" in message or "ultimos" in message or "historico" in message or "resultados" in message:
        results = fetch_furia_results()
        if results:
            response = "Últimos jogos da FURIA:\n\n"
            for result in results:
                response += f"Data: {result['data']}\n"
                response += f"Adversário: {result['adversario']}\n"
                response += f"Torneio: {result['torneio']}\n"
                response += f"Resultado: {result['resultado']}\n"
                response += "Placares por mapa:\n"
                for mapa, placar in result['placares'].items():
                    response += f"- {mapa}: {placar}\n"
                response += "\n"
            response += "Deseja ver as estatísticas detalhadas de algum jogo específico? (Responda com a data do jogo, ex: '08/04/2025')\n\n"
            response += "Precisa de mais alguma informação, torcedor?🐯🔥\n Posso te ajudar com:\n"
            response += "- Últimos resultados\n"
            response += "- Próximos jogos\n"
            response += "- Notícias recentes\n"
            response += "- Estatísticas dos jogos\n"
            response += "- Campeonatos\n\n"
            # Aqui é onde você converte para HTML com <br>
            response_html = response.replace("\n", "<br>")
            return response_html
            return response
        return "Desculpe, não consegui encontrar o histórico de jogos."
    
    elif "Outros resultados" in message or "stats" in message or "estatisticas" in message:
        response += "Por favor, especifique a data do jogo que deseja ver as estatísticas (ex: '08/04/2025')"
        results = fetch_furia_results()
        data_mencoes = ["08/04/2025", "07/04/2025", "06/04/2025", "05/04/2025"]
        data_encontrada = none
        
        for data in data_mencoes:
            if data in message:
                data_encontrada = data
                break
        
        if data_encontrada:
            for result in results:
                if result["data"] == data_encontrada:
                    response = f"Estatísticas do jogo contra {result['adversario']} em {result['data']}:\n\n"
                    response += "FURIA:\n"
                    for jogador, stats in result['estatisticas']['FURIA'].items():
                        response += f"\n{jogador}:\n"
                        for stat, valor in stats.items():
                            response += f"- {stat}: {valor}\n"
                    
                    if result['adversario'] in result['estatisticas']:
                        response += f"\n{result['adversario']}:\n"
                        for jogador, stats in result['estatisticas'][result['adversario']].items():
                            response += f"\n{jogador}:\n"
                            for stat, valor in stats.items():
                                response += f"- {stat}: {valor}\n"
                    
                    response += "\nPrecisa de mais alguma informação, torcedor? Posso te ajudar com:\n"
                    response += "- Últimos resultados\n"
                    response += "- Próximos jogos\n"
                    response += "- Notícias recentes\n"
                    # Aqui é onde você converte para HTML com <br>
                    response_html = response.replace("\n", "<br>")
                    return response_html
                    return response
        
        
    
    elif "próximo jogo" in message or "próxima partida" in message:
        response = "O próximo compromisso da FURIA é a PGL Astana 2025, que será realizada entre os dias 10 e 18 de maio, no Cazaquistão.\n\n"
        response += "Precisa de mais alguma informação, torcedor?🐯🔥\nPosso te ajudar com:\n"
        response += "- Últimos resultados\n"
        response += "- Próximos jogos\n"
        response += "- Notícias recentes\n"
        response += "- Estatísticas dos jogos\n"
        response += "- Campeonatos\n\n"
        # Aqui é onde você converte para HTML com <br>
        response_html = response.replace("\n", "<br>")
        return response_html
        return response
    
    elif "campeonato" in message or "torneio" in message:
        response = "A FURIA está classificada para a PGL Astana 2025, que acontecerá em maio no Cazaquistão.\n\n"
        response += "Precisa de mais alguma informação, torcedor?🐯🔥\nPosso te ajudar com:\n"
        response += "- Últimos resultados\n"
        response += "- Próximos jogos\n"
        response += "- Notícias recentes\n"
        response += "- Estatísticas dos jogos\n"
        response += "- Campeonatos\n\n"
        # Aqui é onde você converte para HTML com <br>
        response_html = response.replace("\n", "<br>")
        return response_html
        return response
    
    else:
        response = "Desculpe, não entendi sua pergunta. Você pode perguntar sobre:\n"
        response += "- Últimos resultados\n"
        response += "- Próximos jogos\n"
        response += "- Notícias recentes\n"
        response += "- Estatísticas dos jogos\n"
        response += "- Campeonatos\n\n"
        response += "O que você gostaria de saber, torcedor? 🐯🔥"
        # Aqui é onde você converte para HTML com <br>
        response_html = response.replace("\n", "<br>")
        return response_html
        return response

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
