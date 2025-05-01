# 📚 Documentação da API - FURIA Insight Engine

## 🔗 Endpoints

### 1. Rota Principal
- **GET /** `/`
  - Descrição: Rota principal da API
  - Resposta:
    ```json
    {
        "message": "Bem-vindo à FURIA Insight Engine API",
        "version": "1.0.0",
        "status": "online"
    }
    ```

### 2. Verificação de Saúde
- **GET /** `/health`
  - Descrição: Verifica o status da API
  - Resposta:
    ```json
    {
        "status": "healthy",
        "timestamp": "2024-03-14T12:00:00Z"
    }
    ```

### 3. Perfis de Fãs
- **POST /** `/fans/profile`
  - Descrição: Cria um novo perfil de fã
  - Corpo da Requisição:
    ```json
    {
        "name": "string",
        "age": "integer",
        "location": "string",
        "gender": "string",
        "interests": ["string"],
        "social_media": {
            "platform": "string",
            "username": "string"
        },
        "engagement_score": "float"
    }
    ```
  - Resposta:
    ```json
    {
        "message": "Perfil criado com sucesso",
        "profile": {
            "id": "integer",
            "name": "string",
            "age": "integer",
            "location": "string",
            "gender": "string",
            "interests": ["string"],
            "social_media": {
                "platform": "string",
                "username": "string"
            },
            "engagement_score": "float",
            "created_at": "datetime"
        }
    }
    ```

- **GET /** `/fans/{fan_id}`
  - Descrição: Obtém o perfil de um fã específico
  - Parâmetros:
    - `fan_id`: ID do fã (integer)
  - Resposta:
    ```json
    {
        "message": "Perfil encontrado",
        "fan_id": "integer",
        "profile": {
            "id": "integer",
            "name": "string",
            "age": "integer",
            "location": "string",
            "gender": "string",
            "interests": ["string"],
            "social_media": {
                "platform": "string",
                "username": "string"
            },
            "engagement_score": "float",
            "created_at": "datetime"
        }
    }
    ```

### 4. Análises
- **GET /** `/analytics/engagement`
  - Descrição: Obtém análises de engajamento
  - Resposta:
    ```json
    {
        "total_fans": "integer",
        "average_engagement": "float",
        "top_platforms": ["string"]
    }
    ```

## 🔒 Autenticação

Atualmente, a API não requer autenticação para desenvolvimento. Em produção, recomenda-se implementar:
- Autenticação via JWT
- Rate limiting
- Validação de origem das requisições

## 📊 Modelos de Dados

### FanProfile
```python
class FanProfile(Base):
    __tablename__ = "fan_profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    location = Column(String)
    gender = Column(String)
    interests = Column(JSON)
    social_media = Column(JSON)
    engagement_score = Column(Float)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
```

### SocialMediaData
```python
class SocialMediaData(Base):
    __tablename__ = "social_media_data"

    id = Column(Integer, primary_key=True, index=True)
    fan_profile_id = Column(Integer, ForeignKey("fan_profiles.id"))
    platform = Column(String)
    username = Column(String)
    followers = Column(Integer)
    posts = Column(Integer)
    engagement_rate = Column(Float)
    last_updated = Column(DateTime, default=datetime.now)
```

## 🛠️ Configuração do Ambiente

1. Variáveis de Ambiente Necessárias:
   ```
   DATABASE_URL=postgresql://user:password@localhost:5432/furia_insight
   ```

2. Dependências Python:
   ```
   fastapi
   uvicorn
   sqlalchemy
   psycopg2-binary
   python-dotenv
   pydantic
   ```

## 🔄 Exemplos de Uso

### Criar um Novo Perfil
```python
import requests

url = "http://localhost:8000/fans/profile"
data = {
    "name": "João Silva",
    "age": 25,
    "location": "São Paulo",
    "gender": "Masculino",
    "interests": ["CS:GO", "E-sports", "Streaming"],
    "social_media": {
        "platform": "Twitter",
        "username": "@joaosilva"
    },
    "engagement_score": 0.85
}

response = requests.post(url, json=data)
print(response.json())
```

### Buscar um Perfil
```python
import requests

fan_id = 1
url = f"http://localhost:8000/fans/{fan_id}"

response = requests.get(url)
print(response.json())
```

## ⚠️ Limitações Atuais

1. Não há autenticação implementada
2. Não há validação de dados complexa
3. Não há paginação nas listagens
4. Não há cache implementado
5. Não há tratamento de concorrência

## 📈 Próximos Passos

1. Implementar autenticação JWT
2. Adicionar validação de dados mais robusta
3. Implementar paginação
4. Adicionar cache com Redis
5. Implementar testes automatizados
6. Adicionar documentação Swagger/OpenAPI 