import React, { useState } from "react";
import axios from "axios";

function FavouriteStocks() {
  const [stockInput, setStockInput] = useState("");
  const [favourites, setFavourites] = useState([]);
  const [livePrices, setLivePrices] = useState({});

  const handleAddStock = async () => {
    if (!stockInput) return;

    const newSymbol = stockInput.toUpperCase();
    if (!favourites.includes(newSymbol)) {
      setFavourites([...favourites, newSymbol]);

      // Live Price 가져오기
      try {
        const response = await axios.get(
          `https://stock-analysis-4dvn.onrender.com/liveprice/${newSymbol}`
        );
        setLivePrices((prev) => ({
          ...prev,
          [newSymbol]: response.data.ltp,
        }));
      } catch (error) {
        console.error("❌ Error fetching live price:", error);
      }
    }

    setStockInput(""); // input clear
  };

  return (
    <div className="p-6 max-w-3xl mx-auto space-y-6">
      <h1 className="text-2xl font-bold text-center">⭐ My Favourite Stocks</h1>

      <div className="flex space-x-4">
        <input
          type="text"
          value={stockInput}
          onChange={(e) => setStockInput(e.target.value)}
          placeholder="Enter Stock Symbol (eg: TCS)"
          className="flex-grow p-3 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-400"
        />
        <button
          onClick={handleAddStock}
          className="px-6 py-3 bg-blue-500 text-white rounded-xl hover:bg-blue-600"
        >
          ➕ Add
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {favourites.map((symbol) => (
          <div
            key={symbol}
            className="bg-white p-4 rounded-xl shadow-md flex flex-col items-center justify-center"
          >
            <h2 className="text-lg font-semibold">{symbol}</h2>
            <p className="text-xl font-bold mt-2">
              ₹{livePrices[symbol] ? livePrices[symbol] : "Fetching..."}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default FavouriteStocks;
