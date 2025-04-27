window.onload = function() {
    // Dummy Chart
    const ctx = document.getElementById('priceChart').getContext('2d');
    const chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['10AM', '11AM', '12PM', '1PM', '2PM', '3PM'],
            datasets: [{
                label: 'NIFTY 50',
                data: [18000, 18200, 18100, 18300, 18250, 18400],
                borderColor: '#1f51ff',
                backgroundColor: 'rgba(31,81,255,0.1)',
                tension: 0.4,
                fill: true,
                pointRadius: 0,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } }
        }
    });

    // API Status Checking
    checkAPIStatus();
};

function checkAPIStatus() {
    // Dummy check - simulate "Connected"
    const statusElement = document.getElementById('apiStatus');
    statusElement.textContent = "API Connected ✅";
    statusElement.style.color = "green";

    // Later, real Upstox API Call and response check here
}
