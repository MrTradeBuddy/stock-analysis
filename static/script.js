const marketContent = {
    nifty: {
        name: "NIFTY 50",
        current: 24039.35,
        high: 24365.45,
        low: 23847.85,
        return: -0.86
    },
    banknifty: {
        name: "BANK NIFTY",
        current: 54664.05,
        high: 55000.00,
        low: 54000.00,
        return: -0.97
    },
    sensex: {
        name: "SENSEX",
        current: 79212.53,
        high: 80000.00,
        low: 78800.00,
        return: -0.74
    },
    giftnifty: {
        name: "GIFT NIFTY",
        current: 24220.00,
        high: 24350.00,
        low: 24100.00,
        return: -0.04
    }
};

function showMarketData(market) {
    const data = marketContent[market];
    const container = document.getElementById('market-data');

    const returnClass = data.return >= 0 ? "positive" : "negative";
    const arrow = data.return >= 0 ? "▲" : "▼";

    container.innerHTML = `
        <h3>${data.name}</h3>
        <p>Current: <b>${data.current}</b></p>
        <p>Today's High: ${data.high}</p>
        <p>Today's Low: ${data.low}</p>
        <p class="${returnClass}">Return: ${arrow} ${Math.abs(data.return)}%</p>
    `;

    const buttons = document.querySelectorAll('.tab-button');
    buttons.forEach(btn => btn.classList.remove('active'));
    document.querySelector(`button[onclick="showMarketData('${market}')"]`).classList.add('active');
}

let chart;

function createChart() {
    const ctx = document.getElementById('priceChart').getContext('2d');
    chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['10:00', '11:00', '12:00', '13:00', '14:00', '15:00'],
            datasets: [{
                label: 'Price',
                data: [24000, 23950, 24020, 24010, 24030, 24039],
                borderColor: '#3498db',
                backgroundColor: 'rgba(52, 152, 219, 0.2)',
                tension: 0.4,
                fill: true,
                pointRadius: 0
            }]
        },
        options: {
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                x: {
                    grid: {
                        display: false
                    }
                },
                y: {
                    grid: {
                        display: false
                    }
                }
            },
            responsive: true,
            maintainAspectRatio: false
        }
    });
}

// Initial Load
window.onload = function() {
    showMarketData('nifty');
    createChart();
};
