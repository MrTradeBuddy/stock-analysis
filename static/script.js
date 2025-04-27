const stocks = [
    "INFY - Infosys",
    "TCS - Tata Consultancy Services",
    "HDFCBANK - HDFC Bank",
    "ICICIBANK - ICICI Bank",
    "RELIANCE - Reliance Industries",
    "SUNPHARMA - Sun Pharmaceutical",
    "DRREDDY - Dr. Reddy's Laboratories",
    "SBIN - State Bank of India",
    "KOTAKBANK - Kotak Mahindra Bank",
    "AXISBANK - Axis Bank",
    "LT - Larsen & Toubro",
    "HCLTECH - HCL Technologies",
    "WIPRO - Wipro",
    "TECHM - Tech Mahindra",
    "MARUTI - Maruti Suzuki",
    "TITAN - Titan Company",
    "BAJFINANCE - Bajaj Finance",
    "BAJAJFINSV - Bajaj Finserv",
    "TATASTEEL - Tata Steel",
    "JSWSTEEL - JSW Steel",
    "ULTRACEMCO - UltraTech Cement",
    "ADANIGREEN - Adani Green Energy",
    "ADANIENT - Adani Enterprises",
    "COALINDIA - Coal India",
    "ITC - ITC Limited",
    "ASIANPAINT - Asian Paints",
    "BRITANNIA - Britannia Industries",
    "NESTLEIND - Nestle India",
    "HINDUNILVR - Hindustan Unilever",
    "BHARTIARTL - Bharti Airtel",
    "ONGC - Oil and Natural Gas Corporation",
    "NTPC - NTPC Limited",
    "POWERGRID - Power Grid Corporation",
    "DIVISLAB - Divi's Laboratories",
    "APOLLOHOSP - Apollo Hospitals",
    "EICHERMOT - Eicher Motors",
    "M&M - Mahindra & Mahindra",
    "HDFCLIFE - HDFC Life Insurance",
    "ICICIPRULI - ICICI Prudential Life",
    "SBILIFE - SBI Life Insurance",
    "INDUSINDBK - IndusInd Bank",
    "SHREECEM - Shree Cement",
    "HEROMOTOCO - Hero MotoCorp",
    "BAJAJ-AUTO - Bajaj Auto",
    "CIPLA - Cipla Limited",
    "TATAMOTORS - Tata Motors",
    "BPCL - Bharat Petroleum",
    "IOC - Indian Oil Corporation",
    "GRASIM - Grasim Industries"
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
