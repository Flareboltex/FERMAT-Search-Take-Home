export default function ProductCard({ product }) {
  return (
    <div style={{
      border: "1px solid #ddd",
      borderRadius: "8px",
      padding: "12px"
    }}>
      <img
        src={product.imageUrl}
        alt={product.name}
        style={{ width: "100%", height: "180px", objectFit: "cover" }}
      />
      <h3>{product.name}</h3>
      <p><strong>${product.price}</strong></p>
      <p>{product.category} • {product.brand}</p>
      <p>⭐ {product.rating}</p>
      <p>🔥 Popularity: {product.popularity}</p>
      {!product.inStock && <p style={{ color: "red" }}>Out of stock</p>}
    </div>
  );
}
