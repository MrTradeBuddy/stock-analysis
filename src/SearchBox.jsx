import React, { useState } from "react";
import axios from "axios";

function SearchBox() {
  const [query, setQuery] = useState("");
  const [suggestions, setSuggestions] = useState([]);

  const handleSearch = async (e) => {
    const value = e.target.value;
    setQuery(value);
    console.log("Query Changed:", value); // ✅ Debug line

    if (value.length > 1) {
      try {
        const { data } = await axios.get(`https://stock-analysis-4dvn.onrender.com/search?q=${value}`);
        console.log("Suggestions:", data); // ✅ Debug line
        setSuggestions(data);
      } catch (error) {
        console.error("Suggestion fetch failed:", error);
      }
    } else {
      setSuggestions([]);
    }
  };

  return (
    <div style={{ position: "relative", width: "100%" }}>
      <input
        type="text"
        value={query}
        onChange={handleSearch}
        placeholder="🔍 Search for stocks..."
        style={{
          width: "100%",
          padding: "10px",
          fontSize: "16px",
          borderRadius: "10px",
          border: "1px solid #ccc",
          marginBottom: "10px",
        }}
      />
      <div style={{ fontSize: "12px", color: "gray" }}>
        {suggestions.length} results
      </div>
      {suggestions.length > 0 && (
        <ul style={{
          position: "absolute",
          background: "white",
          width: "100%",
          boxShadow: "0px 4px 8px rgba(0, 0, 0, 0.1)",
          listStyleType: "none",
          padding: "0",
          margin: "0",
          borderRadius: "8px",
          zIndex: 100
        }}>
          {suggestions.map((s, i) => (
            <li
              key={i}
              style={{ padding: "10px", cursor: "pointer", borderBottom: "1px solid #eee" }}
            >
              {s.symbol} - {s.name}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default SearchBox;
