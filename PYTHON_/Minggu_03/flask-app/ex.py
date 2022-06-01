from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    data = {
        "id": 4646,
        "nama": "adel",
        "lahir": True,
        "alamat": [
            "trangkil",
            "pati",
            "jateng"
        ],
    }
    return data