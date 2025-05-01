# 📚 Documentação do Banco de Dados - FURIA Insight Engine

## 🗄️ Visão Geral

O sistema utiliza PostgreSQL como banco de dados principal, com SQLAlchemy como ORM (Object-Relational Mapping) para gerenciar as operações de banco de dados.

## 📊 Esquema do Banco de Dados

### 1. Tabela: fan_profiles
Armazena informações básicas dos perfis de fãs.

| Coluna | Tipo | Descrição | Restrições |
|--------|------|-----------|------------|
| id | Integer | Identificador único | PK, Auto-incremento |
| name | String | Nome do fã | Not Null |
| age | Integer | Idade | Not Null |
| location | String | Localização | Not Null |
| gender | String | Gênero | Not Null |
| interests | JSON | Lista de interesses | Not Null |
| social_media | JSON | Dados de redes sociais | Not Null |
| engagement_score | Float | Pontuação de engajamento | Not Null |
| created_at | DateTime | Data de criação | Not Null, Default: now() |
| updated_at | DateTime | Data de atualização | Not Null, Default: now() |

### 2. Tabela: social_media_data
Armazena dados específicos de redes sociais dos fãs.

| Coluna | Tipo | Descrição | Restrições |
|--------|------|-----------|------------|
| id | Integer | Identificador único | PK, Auto-incremento |
| fan_profile_id | Integer | ID do perfil do fã | FK, Not Null |
| platform | String | Plataforma social | Not Null |
| username | String | Nome de usuário | Not Null |
| followers | Integer | Número de seguidores | Not Null |
| posts | Integer | Número de posts | Not Null |
| engagement_rate | Float | Taxa de engajamento | Not Null |
| last_updated | DateTime | Última atualização | Not Null, Default: now() |

## 🔄 Relacionamentos

### 1. FanProfile -> SocialMediaData
- Um para Muitos (1:N)
- Um perfil de fã pode ter múltiplos registros de redes sociais
- Chave estrangeira: `social_media_data.fan_profile_id` -> `fan_profiles.id`

## 📝 Exemplos de Queries

### 1. Criar Tabelas
```sql
-- Tabela fan_profiles
CREATE TABLE fan_profiles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INTEGER NOT NULL,
    location VARCHAR(255) NOT NULL,
    gender VARCHAR(50) NOT NULL,
    interests JSONB NOT NULL,
    social_media JSONB NOT NULL,
    engagement_score FLOAT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Tabela social_media_data
CREATE TABLE social_media_data (
    id SERIAL PRIMARY KEY,
    fan_profile_id INTEGER NOT NULL REFERENCES fan_profiles(id),
    platform VARCHAR(50) NOT NULL,
    username VARCHAR(255) NOT NULL,
    followers INTEGER NOT NULL,
    posts INTEGER NOT NULL,
    engagement_rate FLOAT NOT NULL,
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

### 2. Queries Comuns
```sql
-- Buscar todos os fãs com engajamento acima de 0.8
SELECT * FROM fan_profiles WHERE engagement_score > 0.8;

-- Buscar fãs por localização
SELECT * FROM fan_profiles WHERE location = 'São Paulo';

-- Buscar dados de redes sociais de um fã específico
SELECT sm.* 
FROM social_media_data sm
JOIN fan_profiles fp ON sm.fan_profile_id = fp.id
WHERE fp.id = 1;

-- Calcular média de engajamento por plataforma
SELECT platform, AVG(engagement_rate) as avg_engagement
FROM social_media_data
GROUP BY platform;
```

## 🔒 Índices

### 1. Índices Existentes
- `fan_profiles.id` (PK)
- `fan_profiles.name` (para busca por nome)
- `social_media_data.fan_profile_id` (FK)
- `social_media_data.platform` (para agregações)

### 2. Índices Recomendados
```sql
-- Índice para busca por localização
CREATE INDEX idx_fan_profiles_location ON fan_profiles(location);

-- Índice para busca por engajamento
CREATE INDEX idx_fan_profiles_engagement ON fan_profiles(engagement_score);

-- Índice composto para dados de redes sociais
CREATE INDEX idx_social_media_platform_engagement 
ON social_media_data(platform, engagement_rate);
```

## 🛠️ Configuração

### 1. Conexão com o Banco
```python
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost:5432/furia_insight"
```

### 2. Configuração do SQLAlchemy
```python
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

## 📈 Otimizações

### 1. Particionamento
- Considerar particionamento por data para tabelas grandes
- Particionamento por localização para distribuição geográfica

### 2. Cache
- Implementar cache para queries frequentes
- Cache de resultados de agregações

### 3. Manutenção
- Backup regular
- Vacuum e Analyze periódicos
- Monitoramento de performance

## ⚠️ Considerações de Segurança

1. **Acesso**
   - Usar usuário com privilégios mínimos necessários
   - Implementar SSL para conexões
   - Limitar acesso por IP

2. **Dados**
   - Criptografar dados sensíveis
   - Implementar soft delete
   - Manter logs de alterações

3. **Backup**
   - Backup diário
   - Backup antes de migrações
   - Teste regular de restauração

## 📈 Próximos Passos

1. Implementar migrações automáticas
2. Adicionar mais índices conforme necessidade
3. Implementar particionamento
4. Configurar backup automático
5. Implementar monitoramento
6. Adicionar mais validações de dados 