# Account Service

A Flask-based microservice for managing user accounts.

## Endpoints

### POST /register
Registers a new user.

**Request:**
```json
{
  "username": "johndoe",
  "password": "secret"
}
