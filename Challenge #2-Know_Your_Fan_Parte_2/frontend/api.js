// Configuração da API
const API_BASE_URL = 'http://localhost:8000';

// Função para fazer requisições à API
async function fetchAPI(endpoint, options = {}) {
    const token = localStorage.getItem('token');
    const headers = {
        'Content-Type': 'application/json',
        ...(token && { 'Authorization': `Bearer ${token}` }),
        ...options.headers
    };

    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, {
            ...options,
            headers
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
}

// Serviço de Autenticação
const AuthService = {
    async login(email, password) {
        const data = await fetchAPI('/auth/login', {
            method: 'POST',
            body: JSON.stringify({ email, password })
        });
        localStorage.setItem('token', data.token);
        return data;
    },

    async register(userData) {
        const data = await fetchAPI('/auth/register', {
            method: 'POST',
            body: JSON.stringify(userData)
        });
        return data;
    },

    logout() {
        localStorage.removeItem('token');
        window.location.href = '/login.html';
    },

    isAuthenticated() {
        return !!localStorage.getItem('token');
    }
};

// Serviço de Fãs
const FanService = {
    async getFans() {
        return await fetchAPI('/fans');
    },

    async getFanById(id) {
        return await fetchAPI(`/fans/${id}`);
    },

    async createFan(fanData) {
        return await fetchAPI('/fans', {
            method: 'POST',
            body: JSON.stringify(fanData)
        });
    },

    async updateFan(id, fanData) {
        return await fetchAPI(`/fans/${id}`, {
            method: 'PUT',
            body: JSON.stringify(fanData)
        });
    },

    async deleteFan(id) {
        return await fetchAPI(`/fans/${id}`, {
            method: 'DELETE'
        });
    }
};

// Serviço de Análises
const AnalyticsService = {
    async getEngagementAnalytics() {
        return await fetchAPI('/analytics/engagement');
    },

    async getDemographicsAnalytics() {
        return await fetchAPI('/analytics/demographics');
    },

    async getInteractionsAnalytics() {
        return await fetchAPI('/analytics/interactions');
    },

    async getGrowthAnalytics() {
        return await fetchAPI('/analytics/growth');
    }
};

// Serviço de Campanhas
const CampaignService = {
    async getCampaigns() {
        return await fetchAPI('/campaigns');
    },

    async getCampaignById(id) {
        return await fetchAPI(`/campaigns/${id}`);
    },

    async createCampaign(campaignData) {
        return await fetchAPI('/campaigns', {
            method: 'POST',
            body: JSON.stringify(campaignData)
        });
    },

    async updateCampaign(id, campaignData) {
        return await fetchAPI(`/campaigns/${id}`, {
            method: 'PUT',
            body: JSON.stringify(campaignData)
        });
    },

    async deleteCampaign(id) {
        return await fetchAPI(`/campaigns/${id}`, {
            method: 'DELETE'
        });
    }
};

// Exporta os serviços
export {
    AuthService,
    FanService,
    AnalyticsService,
    CampaignService
}; 