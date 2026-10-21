from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from pathlib import Path
import json

app = Flask(__name__, static_folder="static")
CORS(app)
DATA_FILE = Path(__file__).with_name("products.json")

DEFAULT_PRODUCTS = [
    {"id": 1, "name": "Onion", "category": "Vegetables", "unit": "kg", "price": 35, "quantity": 100, "emoji": "🧅"},
    {"id": 2, "name": "Capsicum", "category": "Vegetables", "unit": "kg", "price": 60, "quantity": 45, "emoji": "🫑"},
    {"id": 3, "name": "Tomato", "category": "Vegetables", "unit": "kg", "price": 30, "quantity": 80, "emoji": "🍅"},
    {"id": 4, "name": "Bottle Gourd", "category": "Vegetables", "unit": "piece", "price": 25, "quantity": 35, "emoji": "🥒"},
    {"id": 5, "name": "Grapes", "category": "Fruits", "unit": "kg", "price": 90, "quantity": 40, "emoji": "🍇"},
    {"id": 6, "name": "Guava", "category": "Fruits", "unit": "kg", "price": 55, "quantity": 50, "emoji": "🍐"},
    {"id": 7, "name": "Mango", "category": "Fruits", "unit": "kg", "price": 120, "quantity": 25, "emoji": "🥭"}
]

def load_products():
    if not DATA_FILE.exists():
        save_products(DEFAULT_PRODUCTS)
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))

def save_products(products):
    DATA_FILE.write_text(json.dumps(products, indent=2), encoding="utf-8")

@app.get("/")
def home():
    return send_from_directory("static", "index.html")

@app.get("/api/products")
def get_products():
    return jsonify(load_products())

@app.put("/api/products/<int:product_id>")
def update_product(product_id):
    body = request.get_json(silent=True) or {}
    products = load_products()
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    try:
        price = float(body.get("price", product["price"]))
        quantity = int(body.get("quantity", product["quantity"]))
        if price < 0 or quantity < 0:
            raise ValueError()
    except (TypeError, ValueError):
        return jsonify({"error": "Price and quantity must be non-negative numbers"}), 400
    product["price"] = price
    product["quantity"] = quantity
    save_products(products)
    return jsonify(product)

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

import os

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
