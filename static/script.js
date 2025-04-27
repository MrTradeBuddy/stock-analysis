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

// Default Load
window.onload = function() {
    showMarketData('nifty');
};
