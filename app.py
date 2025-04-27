<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Financial Dashboard</title>
    <link rel="stylesheet" href="/static/css/styles.css">
</head>
<body>

    <h1>📈 Financial Dashboard</h1>
    <div id="connection-status" class="status">Checking Connection...</div>

    <div class="dashboard">
        <div class="card">
            <h2>NIFTY 50</h2>
            <div id="nifty-price">Loading...</div>
            <div id="nifty-status">Checking...</div>
        </div>

        <div class="card">
            <h2>BANK NIFTY</h2>
            <div id="banknifty-price">Loading...</div>
            <div id="banknifty-status">Checking...</div>
        </div>

        <div class="card">
            <h2>SENSEX</h2>
            <div id="sensex-price">Loading...</div>
            <div id="sensex-status">Checking...</div>
        </div>
    </div>

    <script src="/static/js/script.js"></script>
</body>
</html>
