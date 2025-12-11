from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    # Fake example data
    data = {
        "house_id": "NB-0001",
        "last_update": datetime(2025, 12, 9).strftime("%-d/%-m/%Y"),
        "status": "مأهول",
        "occupants": 4,
        "has_children": "نعم",
        "children_details": [
            {"label": "طفل 1", "age": "3 سنوات"},
            {"label": "طفل 2", "age": "6 سنوات"},
        ],
        "has_elderly": "نعم",
        "has_medical_cases": "لا",
        "hazard_sources": "غاز",
        "primary_contact": "0511111111",
        "emergency_button_label": "مباشرة بالبلاغ"
    }
    return render_template("index.html", d=data)

if __name__ == "__main__":
    app.run(debug=True)
