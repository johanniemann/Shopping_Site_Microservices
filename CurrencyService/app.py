from flask import Flask, request, jsonify
import sys

app = Flask(__name__)

EXCHANGE_RATES = {
    'USD': 1.0,
    'EUR': 0.85,
    'DKK': 6.37
}

@app.route('/convert', methods=['POST'])
def convert_currency():
    data = request.get_json()
    amount = data.get('amount')
    from_currency = data.get('from_currency', '').upper()
    to_currency = data.get('to_currency', '').upper()

    # Valider input
    if not amount or from_currency not in EXCHANGE_RATES or to_currency not in EXCHANGE_RATES:
        return jsonify({"error": "Invalid input"}), 400

    # Konverter via USD
    usd_amount = amount / EXCHANGE_RATES[from_currency]
    converted_amount = usd_amount * EXCHANGE_RATES[to_currency]

    return jsonify({
        'original_amount': amount,
        'from_currency': from_currency,
        'to_currency': to_currency,
        'converted_amount': round(converted_amount, 2),
        'exchange_rate': round(EXCHANGE_RATES[to_currency] / EXCHANGE_RATES[from_currency], 4)
    }), 200


if __name__ == "__main__":
    port = 5020  # standardport til V2
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    app.run(port=port)
