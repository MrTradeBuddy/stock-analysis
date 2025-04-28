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
    <div>
      <input
        type="text"
        placeholder="🔍 Search for stocks..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      {suggest.length > 0 && (
        <ul>
          {suggest.map((s) => (
            <li key={s.symbol} onClick={() => onSelect?.(s)}>
              {s.symbol} - {s.name}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
