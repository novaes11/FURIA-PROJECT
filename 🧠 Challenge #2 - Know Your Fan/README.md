# FURIA CS:GO Chat

Um chatbot para fãs da FURIA CS:GO que fornece informações sobre o time, notícias e resultados em tempo real.

## Funcionalidades

- Chat interativo para perguntas sobre a FURIA CS:GO
- Exibição de notícias atualizadas do Draft5
- Informações sobre próximos jogos
- Resultados recentes das partidas
- Interface web moderna e responsiva
- Atualização automática de dados a cada 5 minutos

## Requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd furia-chat
```

2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como Executar

1. Inicie o servidor:
```bash
python flask_app.py
```

2. Acesse o chat no navegador:
```
http://localhost:3000
```

## Estrutura do Projeto

```
furia-chat/
├── flask_app.py        # Aplicação Flask principal
├── requirements.txt    # Dependências do projeto
├── static/            # Arquivos estáticos
│   ├── css/          # Estilos CSS
│   └── images/       # Imagens do projeto
└── templates/         # Templates HTML
    └── index.html    # Interface do chat
```

## Funcionalidades do Chat

O bot pode responder perguntas sobre:
- Últimos resultados da FURIA
- Próximos jogos agendados
- Notícias recentes do time
- Informações gerais sobre a equipe

## Integração com Fontes de Dados

O projeto utiliza:
- Web scraping do Draft5 para notícias e resultados
- Cache de dados para otimização de performance
- Atualização automática a cada 5 minutos

## Contribuição

Sinta-se à vontade para contribuir com o projeto! Abra uma issue ou envie um pull request.

## Licença

Este projeto está sob a licença MIT.
