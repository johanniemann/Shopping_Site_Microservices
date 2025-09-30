from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

CURRENCY_SERVICE_URL = "http://localhost:5002/convert"

# Hjælpefunktion til at konvertere USD -> DKK
def convert_to_dkk(amount_usd):
    payload = {
        "amount": amount_usd,
        "from_currency": "USD",
        "to_currency": "DKK"
    }
    try:
        response = requests.post(CURRENCY_SERVICE_URL, json=payload)
        if response.status_code == 200:
            return response.json().get("converted_amount", amount_usd)
        else:
            return amount_usd  # fallback: returnér USD, hvis currency service fejler
    except:
        return amount_usd  # fallback: hvis Currency Service ikke kører

@app.route('/products', methods=['GET'])
def get_products():
    # Hent produkter fra dummyjson
    res = requests.get("https://dummyjson.com/products")
    if res.status_code != 200:
        return jsonify({"error": "Unable to fetch products"}), 500

    data = res.json()
    products = data.get("products", [])

    # Tilføj DKK-pris til hvert produkt
    catalog = []
    for p in products:
        catalog.append({
            "id": p["id"],
            "title": p["title"],
            "description": p["description"],
            "price_usd": p["price"],
            "price_dkk": convert_to_dkk(p["price"]),
            "category": p["category"],
            "thumbnail": p["thumbnail"]
        })

    return jsonify(catalog), 200


app.run(port=5003)
