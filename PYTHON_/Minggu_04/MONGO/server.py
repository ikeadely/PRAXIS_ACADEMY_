from flask import Flask, Response, request
import pymongo
import json
from bson.objectid import ObjectId
app = Flask(__name__)

#########################
# connect database
#########################

try:
    mongo = pymongo.MongoClient(
        host="localhost",
        port=27017,
        serverSelectionTimeoutMS = 1000
    )
    db = mongo.localhostAdel
    mongo.server_info() #trigger exceptions if cannot connect to db
except:
        print("ERROR- Cannot connect to db")

########################
# create
########################
@app.route("/users", methods=["POST"])
def create_user():
    try:
        user = {
            'name': request.form["name"],
            'lastname': request.form["lastname"]
            }
        dbResponse = db.users.insert_one(user)
        print(dbResponse.inserted_id)
        # for attr in dir(dbResponse):
        #     print(attr)
        return Response(
            response= json.dumps(
                {"message": "user created",
                "id":f"{dbResponse.inserted_id}"
                }),
            status=200,
            mimetype="application/json")

    except Exception as ex:
        print("**********")
        print(ex)
        print("**********")

########################
# read
########################
@app.route("/users", methods=["GET"])
def get_some_users():
    try:
        data = list(db.users.find())
        for user in data:
            user["_id"]=str(user["_id"])
        return Response(
            response= json.dumps(data),
            status=500, 
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(response= json.dumps({"message":"cannot read users"}), status=500, mimetype="application/json")
            
##########################
# update
# set sesuai yang ingin diedit. ex: ingin update name maka diganti name, ingin update lastname maka diganti lastname. (sesuai kebutuhan)
##########################

@app.route("/users/<id>", methods=["PATCH"])
def update_user(id):
    try:
        dbResponse = db.users.update_one(
            {"_id": ObjectId(id)},
            {"$set":{"lastname":request.form["lastname"]},
            }
        )
    # for attr in dir(dbResponse):
    #   print(f"******{attr}******")
        if dbResponse.modified_count == 1:
            return Response(
                response=json.dumps(
                    {"message": "user updated"}),
                status=200,
                mimetype="application/json"
            )
        return Response(
            response= json.dumps(
                {"message":"nothing to update"}),
            status=200,
            mimetype="application/json"
        )  #else
    except Exception as ex:
        print("***************")
        print(ex)
        print("***************")
        return Response(
            response= json.dumps(
                {"message": "sorry can't update user"}),
            status=500,
            mimetype="application/json"
        )
############################
# delete
############################
@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    try:
        dbResponse = db.users.delete_one({"_id":ObjectId(id)})
        if dbResponse.deleted_count == 1:
            return Response(
                response= json.dumps(
                    {"message": "user delete", "id":f"{id}"}),
                status=200,
                mimetype="application/json"
            )
        
        
    except Exception as ex:
        print("*******")
        print(ex)
        print("*******")
        return Response(
        response = json.dumps(
            {"message": "sorry can't delete user"}),
        status=500,
        mimetype="application/json"
        )

#################################
#################################
if __name__ == "__main__":
    app.run(debug=True)