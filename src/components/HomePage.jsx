import React, { useState, useEffect } from "react";
import SearchBox from "../SearchBox"; // ✅ Added import

export default function HomePage() {
  const [time, setTime] = useState(new Date());

  const indices = [
    { name: "SENSEX", value: 80218.37, change: 1005.84, percent: 1.27 },
    { name: "NIFTY", value: 24328.5, change: 289.15, percent: 1.20 },
    { name: "NIFTY BANK", value: 55432.8, change: 768.75, percent: 1.41 },
  ];

  useEffect(() => {
    const interval = setInterval(() => {
      setTime(new Date());
    }, 60000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center p-6 space-y-6">

      {/* Logo */}
      <img
        src="https://via.placeholder.com/150x50?text=Your+Logo"
        alt="Logo"
        className="mb-6"
      />

      {/* 🔍 Search Box Component */}
      <SearchBox /> {/* ✅ Changed from <input> to component */}

      {/* 📊 Indices Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 w-full max-w-6xl mt-8">
        {indices.map((index) => (
          <div
            key={index.name}
            className="bg-white rounded-2xl shadow-md p-6 flex flex-col items-center justify-center text-center hover:shadow-lg transition"
          >
            <h2 className="text-xl font-bold text-gray-800">{index.name}</h2>
            <p className="text-3xl font-extrabold text-blue-600 mt-2">{index.value}</p>
            <p className="mt-2 text-green-500 font-semibold flex items-center gap-1">
              ↗ {index.change} ({index.percent}%)
            </p>
          </div>
        ))}
      </div>

      {/* ⏰ Last Updated */}
      <p className="text-gray-400 text-sm mt-6">
        Last updated at {time.toLocaleString()}
      </p>

    </div>
  );
}
