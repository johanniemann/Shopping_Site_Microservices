from flask import Flask, request, jsonify

app = Flask(__name__)

# midlertidig "database" i hukommelsen
users = []
user_id_counter = 1


@app.route('/register', methods=['POST'])
def register():
    global user_id_counter
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    # check om brugernavnet allerede findes
    if any(u["username"] == username for u in users):
        return jsonify({"error": "Username already exists"}), 400

    # opret bruger
    new_user = {
        "id": user_id_counter,
        "username": username,
        "password": password,  # i virkeligheden skal man hashe den!
        "role": "user"
    }
    users.append(new_user)
    user_id_counter += 1

    return jsonify({"message": "User registered", "user": new_user}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    # find bruger
    user = next((u for u in users if u["username"] == username and u["password"] == password), None)

    if user:
        return jsonify({"message": "Login successful", "user": user}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401


@app.route('/profile/<int:user_id>', methods=['GET'])
def profile(user_id):
    user = next((u for u in users if u["id"] == user_id), None)

    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404


app.run(port=5001)