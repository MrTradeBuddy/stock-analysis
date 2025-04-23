<!DOCTYPE html>
<html>
<head>
  <title>📊 Smart Signal Check – Mr. Trade Buddy</title>
  <style>
    body {
      font-family: sans-serif;
      text-align: center;
      background-color: #f4f4f4;
      padding: 40px;
    }
    .tooltip {
      position: relative;
      display: inline-block;
      border-bottom: 1px dashed #999;
      cursor: pointer;
    }
    .tooltip .tooltiptext {
      visibility: hidden;
      width: 220px;
      background-color: #333;
      color: #fff;
      text-align: left;
      border-radius: 6px;
      padding: 10px;
      position: absolute;
      z-index: 1;
      bottom: 125%;
      left: 50%;
      margin-left: -110px;
      opacity: 0;
      transition: opacity 0.3s;
    }
    .tooltip:hover .tooltiptext {
      visibility: visible;
      opacity: 1;
    }
    .signal-box {
      background: #fff;
      border-radius: 10px;
      padding: 20px;
      max-width: 500px;
      margin: 0 auto;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    .metric {
      font-size: 1.3em;
      margin: 20px 0;
    }
    .label {
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div class="signal-box">
    <h2>🔍 TATAMOTORS – Smart Signal Snapshot</h2>

    <div class="metric">
      <span class="label">📈 CMP:</span> ₹972.50
    </div>

    <div class="metric tooltip">
      <span class="label">📉 RSI:</span> 41.2
      <span class="tooltiptext">RSI between 30-70 indicates neutral momentum. Below 30 = Oversold. Above 70 = Overbought.</span>
    </div>

    <div class="metric tooltip">
      <span class="label">📊 EMA Trend:</span> Bullish
      <span class="tooltiptext">Current price is above 20 EMA – indicating upward trend strength.</span>
    </div>

    <div class="metric tooltip">
      <span class="label">📉 Supertrend:</span> Bearish
      <span class="tooltiptext">Supertrend currently signals a SELL zone. Confirm with RSI or candle breakout.</span>
    </div>
  </div>
</body>
</html>
