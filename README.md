# FURIA CS:GO Chat

Um chatbot para fãs da FURIA CS:GO que fornece informações sobre o time, notícias e resultados.

## Funcionalidades

- Chat interativo para perguntas sobre a FURIA CS:GO
- Exibição de notícias atualizadas sobre o time
- Interface web amigável e responsiva
- Atualização automática de notícias

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
python app.py
```

2. Acesse o chat no navegador:
```
http://localhost:8000
```

## Estrutura do Projeto

```
furia-chat/
├── app.py              # Aplicação principal
├── requirements.txt    # Dependências
├── static/            # Arquivos estáticos
└── templates/         # Templates HTML
    └── index.html     # Interface do chat
```

## Integração com Fontes de Notícias

Para integrar com fontes reais de notícias, você pode:

1. Usar APIs de sites de esports como HLTV.org
2. Implementar web scraping de sites de notícias
3. Integrar com APIs de redes sociais da FURIA

## Contribuição

Sinta-se à vontade para contribuir com o projeto! Abra uma issue ou envie um pull request.

## Licença

Este projeto está sob a licença MIT.
