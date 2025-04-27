const stocks = [
    "INFY - Infosys", 
    "TCS - Tata Consultancy", 
    "HDFCBANK - HDFC Bank", 
    "ICICIBANK - ICICI Bank", 
    "RELIANCE - Reliance Industries",
    "SUNPHARMA - Sun Pharma",
    "DRREDDY - Dr Reddy Labs"
];

const searchBox = document.getElementById('searchBox');
const suggestionsBox = document.getElementById('suggestions');

searchBox.addEventListener('input', function() {
    const input = searchBox.value.toUpperCase();
    suggestionsBox.innerHTML = '';

    if (input.length === 0) {
        return;
    }

    const filteredStocks = stocks.filter(stock => stock.toUpperCase().includes(input));

    filteredStocks.forEach(stock => {
        const div = document.createElement('div');
        div.textContent = stock;
        div.addEventListener('click', () => {
            searchBox.value = stock;
            suggestionsBox.innerHTML = '';
        });
        suggestionsBox.appendChild(div);
    });
});
