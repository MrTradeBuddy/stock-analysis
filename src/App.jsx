import HomePage from "./components/HomePage";
import FavouriteStocks from "./components/FavouriteStocks";  // ✅ Add this

function App() {
  return (
    <div className="flex flex-col space-y-6 p-4">
      <HomePage />           {/* Existing Dashboard / Indices part */}
      <FavouriteStocks />    {/* New Favourite Stocks Section */}
    </div>
  );
}

export default App;
