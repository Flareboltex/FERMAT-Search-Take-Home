const API_BASE = "http://127.0.0.1:8000/api";

export async function fetchProducts({ q, category, brand, minPrice, maxPrice, sort }) {
  const params = new URLSearchParams();

  if (q) params.append("q", q);
  if (category) params.append("category", category);
  if (brand) params.append("brand", brand);
  if (minPrice) params.append("minPrice", minPrice);
  if (maxPrice) params.append("maxPrice", maxPrice);
  if (sort) params.append("sort", sort);

  const response = await fetch(`${API_BASE}/products?${params.toString()}`);
  if (!response.ok) throw new Error("Failed to fetch products");
  return response.json();
}
