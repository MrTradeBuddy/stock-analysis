async function fetchMarketData() {
    try {
        const response = await fetch('/market-data');
        const data = await response.json();

        document.getElementById('nifty-price').innerText = `₹ ${data.nifty.price}`;
        document.getElementById('nifty-status').innerText = data.nifty.status;

        document.getElementById('banknifty-price').innerText = `₹ ${data.banknifty.price}`;
        document.getElementById('banknifty-status').innerText = data.banknifty.status;

        document.getElementById('sensex-price').innerText = `₹ ${data.sensex.price}`;
        document.getElementById('sensex-status').innerText = data.sensex.status;

        document.getElementById('connection-status').innerText = "🟢 Connected";
    } catch (error) {
        console.error('Error fetching data:', error);
        document.getElementById('connection-status').innerText = "🔴 Disconnected";
    }
}

// First fetch immediately
fetchMarketData();

// Then auto-refresh every 60 seconds
setInterval(fetchMarketData, 60000);
