import React, { useState } from "react";
import axios from "axios";

function SearchBox() {
  const [query, setQuery] = useState("");
  const [suggestions, setSuggestions] = useState([]);

  const handleSearch = async (e) => {
    const value = e.target.value;
    setQuery(value);

    if (value.length > 1) {
      try {
        const { data } = await axios.get(`https://stock-analysis-4dvn.onrender.com/search?q=${value}`);
        setSuggestions(data);
      } catch (error) {
        console.error("Suggestion fetch failed:", error);
      }
    } else {
      setSuggestions([]);
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
            <li key={index} className="px-4 py-2 hover:bg-gray-100 cursor-pointer">
              {stock.symbol} - {stock.name}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default SearchBox;
