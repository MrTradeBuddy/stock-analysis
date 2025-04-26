<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mission Memory - Home</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f5f5f5;
            font-family: Arial, sans-serif;
        }
        .search-container {
            text-align: center;
        }
        input[type="text"] {
            width: 300px;
            padding: 10px;
            font-size: 18px;
            border-radius: 8px;
            border: 1px solid #ccc;
        }
        .suggestions {
            margin-top: 5px;
            border: 1px solid #ccc;
            width: 300px;
            background: white;
            border-radius: 8px;
            overflow: hidden;
        }
        .suggestions div {
            padding: 10px;
            cursor: pointer;
        }
        .suggestions div:hover {
            background-color: #f0f0f0;
        }
    </style>
</head>
<body>

<div class="search-container">
    <input type="text" id="searchBox" placeholder="Search for a stock...">
    <div class="suggestions" id="suggestions"></div>
</div>

<script>
    const stocks = ["INFY - Infosys", "TCS - Tata Consultancy", "HDFCBANK - HDFC Bank", "ICICIBANK - ICICI Bank", "RELIANCE - Reliance Industries"];

    const searchBox = document.getElementById('searchBox');
    const suggestionsBox = document.getElementById('suggestions');

    searchBox.addEventListener('input', function() {
        const input = searchBox.value.toUpperCase();
        suggestionsBox.innerHTML = '';
        if (input.length === 0) return;
        const filteredStocks = stocks.filter(stock => stock.toUpperCase().includes(input));
        filteredStocks.forEach(stock => {
            const div = document.createElement('div');
            div.textContent = stock;
            div.addEventListener('click', () => {
                searchBox.value = stock;
                suggestionsBox.innerHTML = '';
                // Here we can add redirection code later
            });
            suggestionsBox.appendChild(div);
        });
    });
</script>

</body>
</html>
