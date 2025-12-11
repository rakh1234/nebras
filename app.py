# app.py
from flask import Flask, jsonify, request, abort
import jwt
import datetime

SECRET = "change_this_secret_for_demo_only"  # for demo; in production use env var + strong key
ALGORITHM = "HS256"

app = Flask(__name__)

# ==== fake DB ====
FAKE_HOUSES = {
    "NB-0001": {
        "id": "NB-0001",
        "occupied": True,
        "count": 4,
        "children": 1,
        "elders": 1,
        "medical": "سكري (1)، حساسية دوائية",
        "hazards": ["غاز منزلي"],
        "contact_number": "+966-50-123-4567"
    },
    "NB-0002": {
        "id": "NB-0002",
        "occupied": False,
        "count": 0,
        "children": 0,
        "elders": 0,
        "medical": None,
        "hazards": [],
        "contact_number": None
    }
}

# ==== auth endpoint (simulate government device getting a signed token) ====
@app.route('/auth', methods=['POST'])
def auth():
    # For demo: always returns a token indicating device_type=gov and allowed scope
    payload = {
        "device": "gov_dispatch_tablet",
        "scope": "read:house",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=45)
    }
    token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)
    return jsonify({"token": token})

# ==== house endpoint (requires Authorization header with Bearer token) ====
@app.route('/api/house/<hid>')
def get_house(hid):
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        abort(403)

    token = auth.split(" ", 1)[1]
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
    except Exception as e:
        abort(403)

    # check scope
    if payload.get("scope") != "read:house":
        abort(403)

    # return fake data if exists
    house = FAKE_HOUSES.get(hid)
    if not house:
        return jsonify({"error":"not found"}), 404

    # mask sensitive details if device not gov (extra check could be done)
    return jsonify(house)

# lightweight index to serve the demo file when running locally
@app.route('/')
def index():
    return open('index.html', 'r', encoding='utf-8').read()

if __name__ == "__main__":
    app.run(port=5000, debug=True)
