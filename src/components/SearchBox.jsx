import React, { useState } from "react";
import axios from "axios";

function SearchBox() {
  const [query, setQuery] = useState("");
  const [suggestions, setSuggestions] = useState([]);
  const [selectedStock, setSelectedStock] = useState(null); // ✅ Selected stock
  const [livePrice, setLivePrice] = useState(null); // ✅ Live Price

  const handleSearch = async (e) => {
    const value = e.target.value;
    setQuery(value);

    if (value.length > 1) {
      try {
        const response = await axios.get(`https://stock-analysis-4dvn.onrender.com/search?q=${value}`);
        setSuggestions(response.data);
      } catch (err) {
        console.error("❌ Error fetching suggestions:", err);
      }
    } else {
      setSuggestions([]);
    }
  };

  const handleSelectStock = async (stock) => {
    setSelectedStock(stock);
    setQuery(stock.symbol); // Fill the input box with selected symbol
    setSuggestions([]); // Hide suggestions

    try {
      const response = await axios.get(`https://stock-analysis-4dvn.onrender.com/liveprice/${stock.symbol}`);
      setLivePrice(response.data.ltp);
    } catch (err) {
      console.error("❌ Error fetching live price:", err);
    }
  };

  return (
    <div className="relative w-full max-w-md mx-auto">
      <input
        type="text"
        value={query}
        onChange={handleSearch}
        placeholder="🔍 Search for stocks..."
        className="w-full p-3 rounded-xl border border-gray-300 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
      {suggestions.length > 0 && (
        <ul className="absolute left-0 right-0 bg-white mt-1 border border-gray-300 rounded-md max-h-60 overflow-y-auto z-10">
          {suggestions.map((stock, index) => (
            <li
              key={index}
              className="px-4 py-2 hover:bg-gray-100 cursor-pointer"
              onClick={() => handleSelectStock(stock)} // ✅ OnClick added
            >
              {stock.symbol} - {stock.name}
            </li>
          ))}
        </ul>
      )}
      {selectedStock && livePrice !== null && (
        <div className="mt-4 p-4 bg-green-100 rounded-xl shadow">
          <h2 className="text-lg font-bold">{selectedStock.symbol} - {selectedStock.name}</h2>
          <p className="text-xl mt-2">📈 Live Price: ₹{livePrice}</p>
        </div>
      )}
    </div>
  );
}

export default SearchBox;
