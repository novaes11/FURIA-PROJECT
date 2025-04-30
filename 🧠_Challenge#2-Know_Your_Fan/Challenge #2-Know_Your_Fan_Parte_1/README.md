# 🐯 FURIA Insight Engine

Um sistema inteligente para análise e compreensão do perfil dos fãs da FURIA, utilizando dados públicos e interativos para criar uma experiência personalizada e engajadora.

## 🎯 Objetivo

Criar um sistema inteligente que entenda quem são os fãs da FURIA, seus interesses, comportamentos, engajamento e afinidade com a marca, usando dados públicos e interativos.

## 🔍 Fontes de Dados

### Dados Pessoais (com consentimento)
- Nome, idade, localização, sexo
- Interesses declarados (games, times favoritos, etc)
- Histórico de compras (se houver e-commerce ou plataforma integrada)

### Redes Sociais
- Posts e curtidas em Twitter/X, Instagram, TikTok, YouTube
- Hashtags relacionadas: #GoFURIA, #SomosFuria, etc
- Seguidores da conta oficial e de jogadores da FURIA
- Comentários e menções públicas

### Interações
- Participações em campanhas (sorteios, enquetes, stories)
- Acessos ao site, loja, ou app oficial
- Presença em eventos e streams (via Twitch ou ticket digital)

## 🧩 Componentes da Solução

### 1. Pipeline de Coleta
- Scripts de scraping (respeitando limites e políticas de cada plataforma)
- APIs (Twitter/X, Instagram Graph API, YouTube Data API, TikTok)
- Formulários de inscrição e engajamento com coleta ativa (consentimento de dados)

### 2. Data Lake + Banco Relacional
- Armazenar dados crus no S3 (ou equivalente)
- Normalização em banco relacional (PostgreSQL, Aurora)

### 3. Análise e Enriquecimento
- Classificação de interesses por NLP (GPT ou BERT)
- Análise de sentimento dos posts
- Agrupamento de personas (clustering via K-Means, DBSCAN)

### 4. Pontuação de Afinidade (FanScore)
| Métrica | Peso (%) |
|---------|----------|
| Frequência de menções | 25% |
| Engajamento em postagens | 20% |
| Presença em eventos/streams | 20% |
| Interações diretas com FURIA | 15% |
| Similaridade com perfis-alvo | 20% |

## 📊 Dashboard Inteligente

- Mapa de calor de onde estão os fãs
- Top hashtags, emoções, tópicos mais falados
- Clusters de fãs: casual, engajado, influenciador, comprador, etc
- Timeline de engajamento por campanha/evento

## 🤖 Funcionalidades com IA

- Recomendações de campanhas personalizadas por perfil
- Chatbot interativo para coletar dados adicionais
- Resumo automático do perfil de um fã
  - Exemplo: "João é um fã superengajado da FURIA, gosta de CS:GO, está presente em streams, e já participou de 3 campanhas"

## 🛡 Privacidade e Consentimento

- LGPD-compliant: explicitar coleta e finalidade dos dados
- Opções de exclusão, exportação e consentimento granular
- Política de privacidade transparente
- Controles de acesso e segurança dos dados

## 🧠 Exemplos de Insights

- "60% dos fãs que interagem com o Yuurih também seguem Gaules"
- "Fãs entre 16-24 anos se engajam mais com conteúdos de highlight do que com análises táticas"
- "Campanhas com prêmios físicos performam 30% melhor entre o público do Sudeste"

## 🛠️ Tecnologias Utilizadas

### Backend
- Python 3.8+
- FastAPI/Flask
- PostgreSQL
- AWS S3
- Redis (cache)

### Frontend
- React.js
- D3.js (visualizações)
- Material-UI
- Chart.js

### Machine Learning
- TensorFlow/PyTorch
- Scikit-learn
- NLTK/SpaCy
- BERT/GPT

### APIs e Integrações
- Twitter API
- Instagram Graph API
- YouTube Data API
- TikTok API
- Twitch API

## 📋 Requisitos do Sistema

- Python 3.8+
- Node.js 14+
- PostgreSQL 12+
- AWS Account (para S3)
- Chaves de API para redes sociais

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd furia-insight-engine
```

2. Configure o ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
npm install  # Para o frontend
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

5. Inicie o banco de dados:
```bash
docker-compose up -d
```

6. Execute as migrações:
```bash
python manage.py migrate
```

7. Inicie o servidor:
```bash
python manage.py runserver
```

## 📁 Estrutura do Projeto

```
furia-insight-engine/
├── backend/
│   ├── api/              # Endpoints da API
│   ├── models/           # Modelos de dados
│   ├── services/         # Lógica de negócio
│   └── utils/            # Utilitários
├── frontend/
│   ├── src/
│   │   ├── components/   # Componentes React
│   │   ├── pages/        # Páginas
│   │   └── services/     # Serviços de API
│   └── public/           # Arquivos estáticos
├── ml/
│   ├── models/           # Modelos de ML
│   ├── training/         # Scripts de treinamento
│   └── evaluation/       # Avaliação de modelos
└── docs/                 # Documentação
```

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Autores

- [Seu Nome] - Desenvolvedor Principal

## 🙏 Agradecimentos

- FURIA Esports
- Comunidade de fãs da FURIA
- Contribuidores do projeto
