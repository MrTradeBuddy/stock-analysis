import React, { useState, useEffect } from "react";
import axios from "axios";

export default function SearchBox({ onSelect }) {
  const [query, setQuery] = useState("");
  const [suggest, setSuggest] = useState([]);

  useEffect(() => {
    if (query.length < 2) {
      setSuggest([]);
      return;
    }
    const id = setTimeout(async () => {
      try {
        const { data } = await axios.get(`https://stock-analysis-4dvn.onrender.com/search?q=${query}`);
        setSuggest(data);
      } catch (error) {
        console.error(error);
      }
    }, 300);
    return () => clearTimeout(id);
  }, [query]);

  return (
    <div style={{ position: "relative", width: "100%" }}>
      <input
        type="text"
        placeholder="🔍 Search for stocks..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        style={{
          width: "100%",
          padding: "10px",
          fontSize: "16px",
          borderRadius: "10px",
          border: "1px solid #ccc",
          marginBottom: "10px",
        }}
      />
      {suggest.length > 0 && (
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
          {suggest.map((s) => (
            <li
              key={s.symbol}
              style={{ padding: "10px", cursor: "pointer", borderBottom: "1px solid #eee" }}
              onClick={() => onSelect?.(s)}
            >
              {s.symbol} - {s.name}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
