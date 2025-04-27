window.onload = function () {
    const ctx = document.getElementById('priceChart').getContext('2d');

    const chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['10:00', '11:00', '12:00', '13:00', '14:00', '15:00'],
            datasets: [{
                label: 'NIFTY 50',
                data: [24000, 23950, 24020, 24010, 24030, 24039],
                borderColor: '#1f51ff',
                backgroundColor: 'rgba(31,81,255,0.1)',
                tension: 0.4,
                fill: true,
                pointRadius: 0,
                borderWidth: 2
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
                    grid: { display: false }
                },
                y: {
                    grid: { display: false }
                }
            },
            responsive: true,
            maintainAspectRatio: false
        }
    });
}
