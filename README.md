# FERMAT E-commerce Product Catalog

## Overview

This project is a product catalog web application with search, filtering, sorting, and pagination. Users can view products, search by name/description, filter by category/brand/price, sort by price/rating/popularity, and navigate through pages of results.

Backend: Python + FastAPI
Frontend: React + Vite


---
## Running from Terminal

* **Activate virtual environment**
    * (From root directory) venv\Scripts\Activate.ps1

* **Frontend Startup**
    * (From frontend directory) npm run dev

* **Backend Startup**
    * (From backend directory) uvicorn app.main:app --reload

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

* **Pagination** 
* **Debounced Search** (prevents excessive API calls while typing)

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
## What I Would Do With More Time

With additional time, I would focus on:

- Implementing backend pagination to improve scalability for large datasets
- Adding URL state management so filters and search queries are shareable
- Making category and brand filters fully dynamic and dependent on each other
- Implementing co-purchase recommendations based on order history
- Adding caching or memoization to reduce repeated computations on the backend

---




