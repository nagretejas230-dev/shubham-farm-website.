# Shubham Farm — Vegetables & Fruits Website

A responsive product catalogue for Shubham Farm using **HTML, CSS, JavaScript, and a Python Flask API**, plus an optional Java order-price calculator.

## Included products
- Vegetables: Onion, Capsicum, Tomato, Bottle Gourd
- Fruits: Grapes, Guava, Mango

Prices and quantities in `products.json` are demo values. Confirm and update them before publishing.

## Run locally
1. Install Python 3.10+.
2. Open a terminal in this project folder.
3. Install dependencies:
   ```bash
   python -m venv .venv
   # Windows: .venv\Scripts\activate
   # macOS/Linux: source .venv/bin/activate
   pip install -r requirements.txt
   ```
4. Start the site:
   ```bash
   python app.py
   ```
5. Open http://127.0.0.1:5000 in your browser.

The page reads current product data from `/api/products`. Change `products.json` to update prices and quantities. The API also has a `PUT /api/products/<id>` endpoint for updating one product, using JSON such as `{"price": 40, "quantity": 75}`.

## Optional Java calculator
With JDK installed:
```bash
javac java/PriceCalculator.java
java -cp java PriceCalculator
```

## Make it live on Google
The site is local until you deploy it to a public hosting service. This package does **not** automatically publish the website or make it appear in Google Search.
1. Deploy the Python app to a host that supports Flask/Python and connect a public domain (or use the host's provided URL).
2. Change the demo email in `static/index.html` to your real business email; add your phone/WhatsApp, address, delivery details, and confirmed prices.
3. In Google Search Console, add and verify the public domain, then submit the sitemap if you add one. Ask Google to index the homepage. Search listing is not instant or guaranteed.
4. Keep the public product prices and quantities accurate. Do not publish personal contact information unless you intend customers to see it.

## Important
This starter site is a product catalogue, not a payment/checkout system. The “Email to order” link is a placeholder and must be updated. The sample product stock is illustrative, not live market data.
