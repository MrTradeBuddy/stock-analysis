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
        setSuggestions(data); // Dynamic API Response
      } catch (error) {
        console.error("Error fetching suggestions:", error);
      }
    } else {
      setSuggestions([]);
    }
  };

  return (
    <div className="relative">
      <input
        type="text"
        value={query}
        onChange={handleSearch}
        placeholder="🔍 Search for stocks..."
        className="w-full max-w-md p-3 rounded-2xl border border-gray-300 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
      />

      {/* Suggestions Dropdown */}
      {suggestions.length > 0 && (
        <ul className="absolute bg-white border border-gray-300 rounded-md mt-1 max-h-60 overflow-y-auto w-full">
          {suggestions.map((stock, idx) => (
            <li key={idx} className="p-2 hover:bg-gray-100 cursor-pointer">
              {stock.symbol} - {stock.name}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default SearchBox;
