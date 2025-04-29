import React, { useState } from "react";

// ✅ Static Stocks Data
const stocks = [
  { symbol: "RELIANCE", name: "Reliance Industries" },
  { symbol: "TCS", name: "Tata Consultancy Services" },
  { symbol: "INFY", name: "Infosys Limited" },
  { symbol: "ICICIBANK", name: "ICICI Bank" },
  { symbol: "HDFCBANK", name: "HDFC Bank" },
  { symbol: "SBIN", name: "State Bank of India" },
  { symbol: "AXISBANK", name: "Axis Bank" },
  { symbol: "KOTAKBANK", name: "Kotak Mahindra Bank" },
  { symbol: "ITC", name: "ITC Limited" },
  { symbol: "LT", name: "Larsen & Toubro" },
];

function SearchBox() {
  const [query, setQuery] = useState("");
  const [suggestions, setSuggestions] = useState([]);

  const handleSearch = (e) => {
  const value = e.target.value;
  setQuery(value);

  console.log("📝 Typed Value:", value);  // ✅ Console Log 1

  if (value.length > 1) {
    const filtered = stocks.filter(
      (stock) =>
        stock.symbol.toLowerCase().includes(value.toLowerCase()) ||
        stock.name.toLowerCase().includes(value.toLowerCase())
    );

    console.log("🔎 Filtered Suggestions:", filtered);  // ✅ Console Log 2
    setSuggestions(filtered);
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
