from crypt import methods
from flask import Flask, request, 
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/pythonmongodb'
mongo = PyMongo(app)

@app.route('/user', methods=['POST'])
def create_user():
    # receiving data
    print(request.json)

    return {'message':'received'}

if __name__== "__main__":
    app.run(debug=True) 