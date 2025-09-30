# Currency Service V2

A Flask-based microservice for currency conversion.

## Endpoints

### POST /convert
Convert an amount between currencies.

**Example Request**
```json
{
  "amount": 100,
  "from_currency": "USD",
  "to_currency": "DKK"
}
