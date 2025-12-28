# FERMAT-Search-Take-Home
Basic product catalog application for FERMAT Commerce
venv\Scripts\Activate.ps1
Frontend activation C:\Users\kanis\Downloads\FERMAT-Search-Take-Home\frontend> npm run dev
Backend Activation C:\Users\kanis\Downloads\FERMAT-Search-Take-Home\backend> uvicorn app.main:app --reload

Perfect! After all that, the README is actually **your chance to shine** without coding more. We can make it **professional, clear, and complete**, so your submission looks polished. Here’s a structured draft you can start with — you just need to fill in any small details about your environment or extra notes:

---

# FERMAT E-commerce Product Catalog

## Overview

This project is a product catalog web application with search, filtering, sorting, and pagination. Users can view products, search by name/description, filter by category/brand/price, sort by price/rating/popularity, and navigate through pages of results.

Backend: Python + FastAPI
Frontend: React + Vite


---

## Architecture / Approach

* **Backend:**

  * FastAPI provides a single `/api/products` endpoint that supports query parameters for search, filtering, and sorting.
  * Popularity is calculated by counting the occurrences of product IDs in `orders.json`.

* **Frontend:**

  * React handles search, filter, sort state and communicates with the backend API.
  * Pagination is implemented in the frontend using `slice` to show a subset of products per page.

---

## Popularity Calculation

Popularity is computed from `orders.json` by counting the number of times each product appears in all orders. Products with higher purchase counts are considered more popular and can be sorted accordingly.

---

## Assumptions / Tradeoffs

* Sample datasets are used by default to speed up development; full datasets can be loaded for demos.
* Pagination is handled on the frontend; backend could be optimized for very large datasets.
* Brand and category values are hard-coded; in production, they would be dynamic from the dataset.

---

## Bonus Features Implemented

* **Pagination** (frontend)

Optional features not implemented:

* Co-purchase recommendations
* Advanced filtering (availability, tags)
* URL state management
* Backend caching or infinite scroll

---

## Known Limitations

* Backend currently returns all products in memory; may not scale for very large datasets without server-side pagination.
* Filters like brand and category are static.

---

## How to Run Tests

* Backend unit test for popularity calculation:

```bash
cd backend
pytest
```

---




