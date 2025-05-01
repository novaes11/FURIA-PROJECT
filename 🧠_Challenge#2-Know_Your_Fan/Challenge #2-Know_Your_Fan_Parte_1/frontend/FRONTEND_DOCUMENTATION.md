# 📚 Documentação do Frontend - FURIA Insight Engine

## 🎨 Estrutura do Frontend

```
frontend/
├── index.html       # Página principal
├── styles.css       # Estilos
├── script.js        # Lógica do frontend
└── images/          # Imagens e assets
```

## 📱 Componentes da Interface

### 1. Header
- Logo da FURIA
- Nome do sistema
- Menu de navegação
  - Dashboard
  - Fãs
  - Análises
  - Campanhas

### 2. Hero Section
- Título principal
- Descrição do sistema
- Botão de call-to-action

### 3. Dashboard
- Cards com métricas principais:
  - Total de Fãs
  - Engajamento Médio
  - Interações Sociais
  - Campanhas Ativas

### 4. Seção de Fãs
- Cards de perfis de fãs
- Informações por perfil:
  - Avatar
  - Nome
  - Localização
  - Estatísticas de engajamento
  - Interesses

### 5. Seção de Análises
- Gráficos interativos:
  - Engajamento por Plataforma
  - Demografia
  - Interações por Tipo
  - Crescimento Mensal

### 6. Seção de Campanhas
- Cards de campanhas ativas
- Status das campanhas
- Métricas de performance

## 🎯 Funcionalidades Implementadas

### 1. Visualização de Dados
- Dashboard com métricas em tempo real
- Gráficos interativos usando Chart.js
- Cards de perfis de fãs

### 2. Responsividade
- Layout adaptativo para diferentes tamanhos de tela
- Design mobile-first
- Breakpoints para tablets e desktops

### 3. Interatividade
- Gráficos interativos
- Cards com hover effects
- Navegação suave entre seções

## 🛠️ Tecnologias Utilizadas

### 1. HTML5
- Estrutura semântica
- Meta tags para SEO
- Integração com Font Awesome

### 2. CSS3
- Flexbox e Grid para layout
- Variáveis CSS para temas
- Animações e transições
- Media queries para responsividade

### 3. JavaScript
- Manipulação do DOM
- Integração com Chart.js
- Event listeners
- Fetch API para comunicação com backend

### 4. Bibliotecas
- Chart.js para gráficos
- Font Awesome para ícones
- Google Fonts (Roboto)

## 📊 Integração com Backend

### 1. Endpoints Utilizados
```javascript
const API_ENDPOINTS = {
    base: 'http://localhost:8000',
    fans: '/fans/profile',
    analytics: '/analytics/engagement'
};
```

### 2. Exemplo de Requisição
```javascript
async function fetchFanProfile(fanId) {
    try {
        const response = await fetch(`${API_ENDPOINTS.base}/fans/${fanId}`);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Erro ao buscar perfil:', error);
    }
}
```

## 🎨 Estilos e Temas

### 1. Cores Principais
```css
:root {
    --primary-color: #FF4655;    /* Vermelho FURIA */
    --secondary-color: #0F1923;  /* Azul escuro */
    --accent-color: #7B2CBF;     /* Roxo */
    --text-color: #FFFFFF;       /* Branco */
    --background-color: #1A1A1A; /* Preto */
}
```

### 2. Tipografia
```css
body {
    font-family: 'Roboto', sans-serif;
    font-size: 16px;
    line-height: 1.5;
}
```

## 📱 Responsividade

### Breakpoints
```css
/* Mobile First */
@media (min-width: 768px) {
    /* Tablet */
}

@media (min-width: 1024px) {
    /* Desktop */
}

@media (min-width: 1440px) {
    /* Large Desktop */
}
```

## ⚠️ Limitações Atuais

1. Não há formulário de cadastro de fãs
2. Não há autenticação de usuários
3. Não há persistência local de dados
4. Não há tratamento de erros robusto
5. Não há testes automatizados

## 📈 Próximos Passos

1. Implementar formulário de cadastro
2. Adicionar autenticação
3. Implementar persistência local
4. Melhorar tratamento de erros
5. Adicionar testes
6. Implementar PWA

## 🔧 Como Executar

1. Clone o repositório
2. Navegue até a pasta frontend
3. Abra o arquivo index.html em um navegador
   - Ou use um servidor local:
     ```bash
     python -m http.server 8000
     ```
4. Acesse http://localhost:8000

## 🎯 Boas Práticas

1. **Performance**
   - Lazy loading de imagens
   - Minificação de assets
   - Otimização de fontes

2. **Acessibilidade**
   - Alt text em imagens
   - ARIA labels
   - Contraste adequado

3. **SEO**
   - Meta tags
   - Estrutura semântica
   - URLs amigáveis

4. **Manutenção**
   - Código comentado
   - Funções modulares
   - Nomes descritivos 