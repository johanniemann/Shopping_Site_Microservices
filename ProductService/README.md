# Product Catalog Service

A Flask-based microservice for fetching and displaying product data.

## Description

This service fetches product data from [dummyjson.com](https://dummyjson.com/products), adds a converted price in DKK by calling the Currency Service, and returns the results as JSON.

## Endpoints

### GET /products

Fetches a list of products, with prices converted to DKK.

**URL:** `http://localhost:5003/products`

**Method:** `GET`

**Response Example (200 OK):**

```json
[
  {
    "id": 1,
    "title": "iPhone 9",
    "description": "An apple mobile which is nothing like apple",
    "price_usd": 549,
    "price_dkk": 3497.13,
    "category": "smartphones",
    "thumbnail": "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg"
  },
  ...
]
