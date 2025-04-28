import React, { useState } from "react";

export default function HomePage() {
  const [search, setSearch] = useState("");

  const indices = [
    { name: "SENSEX", value: 80218.37, change: 1005.84, percent: 1.27 },
    { name: "NIFTY", value: 24328.5, change: 289.15, percent: 1.20 },
    { name: "NIFTY BANK", value: 55432.8, change: 768.75, percent: 1.41 },
  ];

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center p-6">
      {/* Search Box */}
      <input
        type="text"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        placeholder="🔍 Search for stocks..."
        className="w-full max-w-md p-3 rounded-2xl border border-gray-300 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-400 mb-8"
      />

      {/* Indices Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 w-full max-w-5xl">
        {indices.map((index) => (
          <div
            key={index.name}
            className="bg-white rounded-2xl shadow-md p-6 flex flex-col items-center justify-center text-center hover:shadow-lg transition"
          >
            <h2 className="text-xl font-bold text-gray-800">{index.name}</h2>
            <p className="text-3xl font-extrabold text-blue-600 mt-2">{index.value}</p>
            <p
              className={`mt-2 text-green-500 font-semibold flex items-center gap-1`}
            >
              ↗ {index.change} ({index.percent}%)
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}
