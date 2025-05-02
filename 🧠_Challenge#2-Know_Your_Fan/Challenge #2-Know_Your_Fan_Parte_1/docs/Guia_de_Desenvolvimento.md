# 📚 Guia de Desenvolvimento - FURIA Insight Engine

## 🎯 Visão Geral

Este guia fornece instruções detalhadas para desenvolvedores que desejam contribuir com o projeto FURIA Insight Engine.

## 🛠️ Ambiente de Desenvolvimento

### 1. Requisitos
- Python 3.8+
- PostgreSQL 12+
- Docker e Docker Compose
- Git
- Editor de código (VS Code recomendado)

### 2. Extensões VS Code Recomendadas
- Python
- Pylance
- Docker
- PostgreSQL
- GitLens
- Prettier
- ESLint

## 🚀 Primeiros Passos

### 1. Clone do Repositório
```bash
git clone [URL_DO_REPOSITÓRIO]
cd furia-insight-engine
```

### 2. Configuração do Ambiente Virtual
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Instalação de Dependências
```bash
# Backend
cd backend
pip install -r requirements.txt

# Frontend
cd frontend
npm install
```

### 4. Configuração do Banco de Dados
```bash
# Criar arquivo .env
cp .env.example .env

# Editar variáveis de ambiente
# DATABASE_URL=postgresql://user:password@localhost:5432/furia_insight
```

## 📝 Convenções de Código

### 1. Python (Backend)
- PEP 8 para estilo de código
- Docstrings em todas as funções e classes
- Type hints para parâmetros e retornos
- Testes unitários para novas funcionalidades

Exemplo:
```python
def calculate_engagement_score(fan_id: int) -> float:
    """
    Calcula a pontuação de engajamento para um fã específico.

    Args:
        fan_id (int): ID do fã

    Returns:
        float: Pontuação de engajamento entre 0 e 1
    """
    # Implementação
    pass
```

### 2. JavaScript (Frontend)
- ESLint para estilo de código
- JSDoc para documentação
- Componentes funcionais com hooks
- Testes com Jest

Exemplo:
```javascript
/**
 * Calcula a pontuação de engajamento
 * @param {number} fanId - ID do fã
 * @returns {Promise<number>} Pontuação de engajamento
 */
async function calculateEngagementScore(fanId) {
    // Implementação
}
```

## 🔄 Fluxo de Trabalho

### 1. Git Workflow
```bash
# Criar nova branch
git checkout -b feature/nova-funcionalidade

# Fazer commits
git add .
git commit -m "feat: adiciona nova funcionalidade"

# Atualizar branch
git pull origin main

# Enviar alterações
git push origin feature/nova-funcionalidade
```

### 2. Convenções de Commit
- feat: nova funcionalidade
- fix: correção de bug
- docs: documentação
- style: formatação
- refactor: refatoração
- test: testes
- chore: tarefas gerais

## 🧪 Testes

### 1. Backend (Python)
```bash
# Executar todos os testes
pytest

# Executar testes específicos
pytest tests/test_models.py

# Cobertura de código
pytest --cov=.
```

### 2. Frontend (JavaScript)
```bash
# Executar testes
npm test

# Cobertura de código
npm run test:coverage
```

## 📊 Banco de Dados

### 1. Migrações
```bash
# Criar nova migração
alembic revision -m "descricao"

# Aplicar migrações
alembic upgrade head

# Reverter migração
alembic downgrade -1
```

### 2. Seeds
```bash
# Popular banco com dados de teste
python scripts/seed.py
```

## 🔍 Debugging

### 1. Backend
```python
# Usar debugger do VS Code
import pdb; pdb.set_trace()

# Logging
import logging
logging.debug("Mensagem de debug")
```

### 2. Frontend
```javascript
// Console
console.log("Debug:", variable);

// Debugger
debugger;
```

## 📈 Performance

### 1. Backend
- Usar cache quando apropriado
- Otimizar queries do banco
- Implementar paginação
- Usar async/await

### 2. Frontend
- Lazy loading de componentes
- Otimizar imagens
- Minificar assets
- Usar memoização

## 🔒 Segurança

### 1. Backend
- Validar inputs
- Sanitizar dados
- Usar HTTPS
- Implementar rate limiting

### 2. Frontend
- Sanitizar inputs
- Implementar CSRF protection
- Usar HTTPS
- Validar dados

## 📚 Documentação

### 1. Código
- Documentar funções e classes
- Manter README atualizado
- Documentar APIs
- Comentar código complexo

### 2. Projeto
- Atualizar documentação
- Manter changelog
- Documentar decisões técnicas
- Criar guias de usuário

## 🚀 Deploy

### 1. Desenvolvimento
```bash
# Iniciar serviços
docker-compose up -d

# Verificar logs
docker-compose logs -f
```

### 2. Produção
```bash
# Build
docker-compose -f docker-compose.prod.yml build

# Deploy
docker-compose -f docker-compose.prod.yml up -d
```

## ⚠️ Problemas Comuns

### 1. Backend
- Problemas de conexão com banco
- Erros de importação
- Problemas com dependências
- Erros de CORS

### 2. Frontend
- Problemas de CORS
- Erros de build
- Problemas com dependências
- Erros de renderização

## 📈 Próximos Passos

1. Implementar CI/CD
2. Adicionar mais testes
3. Melhorar documentação
4. Otimizar performance
5. Implementar monitoramento
6. Adicionar analytics 