# 📚 Documentação Docker - FURIA Insight Engine

## 🐳 Visão Geral

O projeto utiliza Docker para containerização dos serviços, facilitando o desenvolvimento e deploy da aplicação. O arquivo `docker-compose.yml` define os serviços necessários para rodar a aplicação.

## 🛠️ Serviços

### 1. Backend (FastAPI)
- **Imagem Base**: Python 3.8
- **Porta**: 8000
- **Dependências**: requirements.txt
- **Variáveis de Ambiente**: .env

### 2. Banco de Dados (PostgreSQL)
- **Imagem**: postgres:12
- **Porta**: 5432
- **Volume**: dados do banco
- **Variáveis de Ambiente**:
  - POSTGRES_USER
  - POSTGRES_PASSWORD
  - POSTGRES_DB

## 📝 docker-compose.yml

```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    volumes:
      - ./backend:/app
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/furia_insight
    depends_on:
      - db

  db:
    image: postgres:12
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=furia_insight

volumes:
  postgres_data:
```

## 🔧 Dockerfile

### Backend
```dockerfile
FROM python:3.8

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 🚀 Como Executar

### 1. Construir as Imagens
```bash
docker-compose build
```

### 2. Iniciar os Serviços
```bash
docker-compose up -d
```

### 3. Verificar Logs
```bash
docker-compose logs -f
```

### 4. Parar os Serviços
```bash
docker-compose down
```

## 📦 Volumes

### 1. Dados do PostgreSQL
- Nome: postgres_data
- Localização: /var/lib/postgresql/data
- Persistência: Sim

### 2. Código Fonte
- Backend: ./backend:/app
- Hot-reload: Sim

## 🔒 Segurança

### 1. Variáveis de Ambiente
- Usar arquivo .env para senhas e chaves
- Não commitar .env no repositório
- Usar secrets em produção

### 2. Redes
- Isolar serviços em redes Docker
- Expor apenas portas necessárias
- Usar HTTPS em produção

## 📈 Monitoramento

### 1. Logs
```bash
# Logs de todos os serviços
docker-compose logs

# Logs de um serviço específico
docker-compose logs backend

# Logs em tempo real
docker-compose logs -f
```

### 2. Status
```bash
# Verificar status dos containers
docker-compose ps

# Verificar uso de recursos
docker stats
```

## 🔄 Comandos Úteis

### 1. Gerenciamento de Containers
```bash
# Reiniciar um serviço
docker-compose restart backend

# Reconstruir um serviço
docker-compose up -d --build backend

# Remover containers e volumes
docker-compose down -v
```

### 2. Banco de Dados
```bash
# Acessar shell do PostgreSQL
docker-compose exec db psql -U user -d furia_insight

# Backup do banco
docker-compose exec db pg_dump -U user furia_insight > backup.sql
```

## ⚠️ Considerações

### 1. Desenvolvimento
- Usar volumes para hot-reload
- Manter node_modules em volume
- Configurar .dockerignore

### 2. Produção
- Usar multi-stage builds
- Implementar healthchecks
- Configurar restart policies
- Usar secrets para senhas

## 📈 Próximos Passos

1. Adicionar Nginx como proxy reverso
2. Implementar CI/CD com Docker
3. Configurar monitoramento com Prometheus
4. Adicionar testes em containers
5. Implementar backup automático
6. Configurar SSL/TLS

## 🛠️ Troubleshooting

### 1. Problemas Comuns

#### Container não inicia
```bash
# Verificar logs
docker-compose logs backend

# Verificar variáveis de ambiente
docker-compose config
```

#### Problemas de conexão com banco
```bash
# Verificar se o banco está rodando
docker-compose ps db

# Testar conexão
docker-compose exec backend python -c "from database import engine; print(engine.connect())"
```

### 2. Limpeza

#### Remover containers parados
```bash
docker-compose down
```

#### Limpar volumes não utilizados
```bash
docker volume prune
```

#### Limpar imagens não utilizadas
```bash
docker image prune
``` 