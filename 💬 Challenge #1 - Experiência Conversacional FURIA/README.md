# 🐯 FURIA CS:GO Chat - Experiência Conversacional

Um chatbot interativo desenvolvido para os fãs da FURIA CS:GO, oferecendo uma experiência conversacional rica e informativa sobre o time.

## 🎯 Objetivo

Criar uma interface conversacional que permita aos fãs da FURIA obter informações atualizadas sobre:
- Resultados de partidas
- Próximos jogos
- Notícias do time
- Estatísticas dos jogadores
- Campeonatos
- Line-up atual

## ✨ Funcionalidades Principais

### Chat Interativo
- Interface web moderna e responsiva
- Respostas em tempo real
- Suporte a múltiplos tipos de perguntas
- Formatação rica com emojis e estilos

### Informações em Tempo Real
- Notícias atualizadas do Draft5
- Resultados recentes das partidas
- Próximos jogos agendados
- Estatísticas detalhadas dos jogadores

### Sistema de Cache
- Atualização automática a cada 5 minutos
- Otimização de performance
- Redução de requisições ao servidor

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3.8+ com Flask (recomendado: python 3.12.10)
- **Frontend**: HTML5, CSS3, JavaScript
- **APIs**: Draft5 (web scraping)
- **Cache**: Sistema de cache em memória
- **Deploy**: Servidor local para desenvolvimento

## 📋 Requisitos do Sistema

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Navegador web moderno
- Conexão com internet

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd furia-chat
```

2. Crie e ative o ambiente virtual:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 💻 Como Executar

1. Inicie o servidor Flask:
```bash
python flask_app.py
```

2. Acesse o chat no navegador:
```
http://localhost:3000
```

## 📁 Estrutura do Projeto

```
furia-chat/
├── flask_app.py        # Aplicação Flask principal
├── requirements.txt    # Dependências do projeto
├── static/            # Arquivos estáticos
│   ├── css/          # Estilos CSS
│   └── images/       # Imagens e assets
└── templates/         # Templates HTML
    └── index.html    # Interface do chat
```

## 🤖 Funcionalidades do Chat

O bot pode responder a diversos tipos de perguntas:

### Resultados
- Últimos resultados da FURIA
- Estatísticas detalhadas das partidas
- Placares por mapa

### Jogos
- Próximos jogos agendados
- Informações sobre campeonatos
- Calendário de competições

### Time
- Line-up atual
- Estatísticas dos jogadores
- Informações sobre o coach

### Notícias
- Últimas notícias do time
- Atualizações sobre transferências
- Informações sobre campeonatos

## 🔄 Integração com Fontes de Dados

O projeto utiliza:
- Web scraping do Draft5 para dados em tempo real
- Sistema de cache para otimização
- Atualização automática dos dados
- Tratamento de erros e fallbacks

## 🎨 Interface do Usuário

- Design moderno e responsivo
- Suporte a emojis e formatação rica
- Interface intuitiva e fácil de usar
- Adaptação para diferentes dispositivos

## 🔒 Segurança

- Validação de inputs
- Proteção contra XSS
- Sanitização de dados
- Tratamento de erros

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 👥 Autores

- João Vitor Novaes - Desenvolvedor Principal

## 🙏 Agradecimentos

- FURIA Esports
- Draft5
- Comunidade de fãs da FURIA
