async function fetchMarketData() {
    try {
        const data = {
            nifty: {
                price: 22450.55,
                prev_close: 22330.10
            },
            banknifty: {
                price: 47850.00,
                prev_close: 47750.00
            },
            sensex: {
                price: 74000.40,
                prev_close: 74200.00
            }
        };

        updateCard('nifty', data.nifty.price, data.nifty.prev_close);
        updateCard('banknifty', data.banknifty.price, data.banknifty.prev_close);
        updateCard('sensex', data.sensex.price, data.sensex.prev_close);

        document.getElementById('connection-status').innerText = "🟢 Connected";
    } catch (error) {
        console.error('Error fetching data:', error);
        document.getElementById('connection-status').innerText = "🔴 Disconnected";
    }
}

function updateCard(id, price, prevClose) {
    const change = price - prevClose;
    const percentChange = (change / prevClose) * 100;
    const priceElem = document.getElementById(`${id}-price`);
    const statusElem = document.getElementById(`${id}-status`);

    const isPositive = change >= 0;
    const color = isPositive ? 'green' : 'red';
    const emoji = isPositive ? '📈' : '📉';
    const statusText = isPositive ? 'Rising' : 'Falling';

    priceElem.innerHTML = `₹ ${price.toFixed(2)} <br> <span style="color:${color};">${emoji} ${change.toFixed(2)} | ${percentChange.toFixed(2)}%</span>`;
    statusElem.innerHTML = `<span style="color:${color}; font-weight:bold;">${statusText}</span>`;
}

fetchMarketData();
setInterval(fetchMarketData, 60000);
