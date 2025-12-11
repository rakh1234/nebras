from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    data = {
        "status": "مأهول",
        "residents": 4,
        "has_children": "نعم",
        "child1_age": "3 سنوات",
        "child2_age": "6 سنوات",
        "elderly": "نعم",
        "special_cases": "لا",
        "danger": "غاز",
        "phone": "0511111111",
        "home_id": "NB-0001",
        "updated": "9/12/2025"
    }
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
