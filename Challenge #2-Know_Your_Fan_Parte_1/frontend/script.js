// Espera o DOM carregar
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll para links de navegação
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Animação do header ao rolar
    const header = document.querySelector('.header');
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;

        if (currentScroll <= 0) {
            header.classList.remove('scroll-up');
            return;
        }

        if (currentScroll > lastScroll && !header.classList.contains('scroll-down')) {
            // Scroll Down
            header.classList.remove('scroll-up');
            header.classList.add('scroll-down');
        } else if (currentScroll < lastScroll && header.classList.contains('scroll-down')) {
            // Scroll Up
            header.classList.remove('scroll-down');
            header.classList.add('scroll-up');
        }
        lastScroll = currentScroll;
    });

    // Animação dos cards ao entrar na viewport
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.card, .fan-card, .chart-card, .campaign-card').forEach(card => {
        observer.observe(card);
    });

    // Configuração dos gráficos
    // Gráfico de Engajamento por Plataforma
    const engagementCtx = document.getElementById('engagementChart').getContext('2d');
    const engagementChart = new Chart(engagementCtx, {
        type: 'bar',
        data: {
            labels: ['Twitter', 'Instagram', 'Twitch', 'YouTube', 'TikTok'],
            datasets: [{
                label: 'Engajamento (%)',
                data: [75, 85, 90, 65, 80],
                backgroundColor: [
                    '#FF4655',
                    '#0F1923',
                    '#7B2CBF',
                    '#28a745',
                    '#ffc107'
                ],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100
                }
            }
        }
    });

    // Gráfico de Demografia
    const demographicsCtx = document.getElementById('demographicsChart').getContext('2d');
    const demographicsChart = new Chart(demographicsCtx, {
        type: 'doughnut',
        data: {
            labels: ['16-24 anos', '25-34 anos', '35-44 anos', '45+ anos'],
            datasets: [{
                data: [45, 30, 15, 10],
                backgroundColor: [
                    '#FF4655',
                    '#0F1923',
                    '#7B2CBF',
                    '#28a745'
                ],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });

    // Gráfico de Interações
    const interactionsCtx = document.getElementById('interactionsChart').getContext('2d');
    const interactionsChart = new Chart(interactionsCtx, {
        type: 'pie',
        data: {
            labels: ['Likes', 'Comentários', 'Compartilhamentos', 'Mensagens'],
            datasets: [{
                data: [40, 25, 20, 15],
                backgroundColor: [
                    '#FF4655',
                    '#0F1923',
                    '#7B2CBF',
                    '#28a745'
                ],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });

    // Gráfico de Crescimento
    const growthCtx = document.getElementById('growthChart').getContext('2d');
    const growthChart = new Chart(growthCtx, {
        type: 'line',
        data: {
            labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
            datasets: [{
                label: 'Novos Fãs',
                data: [100, 150, 200, 250, 300, 350],
                borderColor: '#FF4655',
                backgroundColor: 'rgba(255, 70, 85, 0.1)',
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Simulação de dados em tempo real
    function updateDashboardNumbers() {
        const numbers = document.querySelectorAll('.number');
        numbers.forEach(number => {
            const currentValue = parseInt(number.textContent.replace(/,/g, ''));
            const newValue = currentValue + Math.floor(Math.random() * 10);
            number.textContent = newValue.toLocaleString();
        });
    }

    // Atualiza os números a cada 5 segundos
    setInterval(updateDashboardNumbers, 5000);

    // Atualiza os gráficos a cada 3 segundos
    setInterval(() => {
        // Atualiza dados do gráfico de engajamento
        engagementChart.data.datasets[0].data = engagementChart.data.datasets[0].data.map(
            value => value + (Math.random() * 10 - 5)
        );
        engagementChart.update();

        // Atualiza dados do gráfico de crescimento
        const lastValue = growthChart.data.datasets[0].data[growthChart.data.datasets[0].data.length - 1];
        growthChart.data.datasets[0].data.push(lastValue + Math.floor(Math.random() * 50));
        growthChart.data.datasets[0].data.shift();
        growthChart.update();
    }, 3000);

    // Adiciona classe active ao link de navegação atual
    function updateActiveNavLink() {
        const sections = document.querySelectorAll('section');
        const navLinks = document.querySelectorAll('.nav a');

        sections.forEach(section => {
            const rect = section.getBoundingClientRect();
            if (rect.top <= 100 && rect.bottom >= 100) {
                const id = section.getAttribute('id');
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${id}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }

    window.addEventListener('scroll', updateActiveNavLink);

    // Adiciona interatividade aos cards de fãs
    document.querySelectorAll('.fan-card').forEach(card => {
        card.addEventListener('click', () => {
            card.classList.toggle('expanded');
        });
    });

    // Adiciona interatividade aos cards de campanhas
    document.querySelectorAll('.campaign-card').forEach(card => {
        card.addEventListener('click', () => {
            card.classList.toggle('expanded');
        });
    });
}); 