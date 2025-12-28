import { useEffect, useState } from "react";
import ProductCard from "./components/ProductCard";

function App() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [query, setQuery] = useState("");

  const [debouncedQuery, setDebouncedQuery] = useState(query);

  useEffect(() => {
    const handler = setTimeout(() => setDebouncedQuery(query), 300);
    return () => clearTimeout(handler);
  }, [query]);

  useEffect(() => {
    setLoading(true);
    fetch(`http://127.0.0.1:8000/api/products?q=${encodeURIComponent(debouncedQuery)}`)
      .then((res) => {
        if (!res.ok) throw new Error("Failed to fetch");
        return res.json();
      })
      .then((data) => {
        setProducts(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, [debouncedQuery]);

  if (error) return <p>Error: {error}</p>;

  return (
    <div style={{ padding: "20px" }}>
      <h1>Product Catalog</h1>

      <input
        type="text"
        placeholder="Search products..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        style={{
          padding: "8px",
          width: "100%",
          maxWidth: "400px",
          marginBottom: "20px"
        }}
      />

      {loading ? (
        <p>Loading products...</p>
      ) : products.length === 0 ? (
        <p>No products match your search.</p>
      ) : (
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fill, minmax(250px, 1fr))",
            gap: "16px"
          }}
        >
          {products.map((p) => (
            <ProductCard key={p.id} product={p} />
          ))}
        </div>
      )}
    </div>
  );
}

export default App;
