from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Jum'at, 20 Mei 2022"

if __name__== "__main__":
	app.run(debug=True)

