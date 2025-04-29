return (
  <div className="min-h-screen bg-gray-100 flex flex-col items-center p-6 space-y-6">
    
    {/* Logo */}
    <img
      src="https://via.placeholder.com/150x50?text=Your+Logo"
      alt="Logo"
      className="mb-6"
    />

    {/* Search Box */}
    <SearchBox />

    {/* Indices Cards */}
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

    {/* Last Updated */}
    <p className="text-gray-400 text-sm mt-6">
      Last updated at {time.toLocaleString()}
    </p>
  </div>
);
