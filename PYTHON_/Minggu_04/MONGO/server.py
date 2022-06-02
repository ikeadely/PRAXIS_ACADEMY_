from flask import Flask, Response, request
from importlib_metadata import method_cache
import pymongo
import json
from bson.objectid import ObjectId
app = Flask(__name__)

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
            
########################
# create
########################
@app.route("/users", methods=["POST"])
def create_user():
    try:
        user = {
            "name": request.form["name"],
            "lastName": request.form["lastname"]
            }
        dbResponse = db.users.insert_one(user)
        print(dbResponse.insert_id)
        # for attr in dir(dbResponse):
        #     print(attr)
        return Response(
            
        )
    except Exception as ex:
        print("**********")
        print(ex)
        print("**********")

##########################
# update
##########################

@app.route("/users/<id>", methods=["PATCH"])
def update_user(id):
    try:
        dbResponse = db.users.update_one(
            {"_id": ObjectId(id)},
            {"$set":{"name":request.form["name"]}}
        )
        # for attr in dir(dbResponse):
        #   print(f"******{attr}******")
        if dbResponse.modified_count == 1:
            return Response(
                response=json.dumps(
                    {"message": "user updated"}),
                status=500,
                mimetype="application/json"
            )
        else:
            return Response(
                response= json.dumps(
                    {"message":"nothing to update"}),
                status=500,
                mimetype="application/json"
            )
    except Exception as ex:
        print("***************")
        print(ex)
        print("***************")
        return Response(
            response= json.dumps(
                {"message": "sorry cannot update user"}),
            status=500,
            mimetype="application/json"
            )
############################
# delete
############################
@app.route("/user/<id>", methods=["DELETE"])
def delete_user(id):
    try:
        dbResponse = db.uses.delete_one({"_id_":ObjectId(id)})
        for attr in dir(dbResponse):
            print(f"***{attr}***")
        return Response(
            response= json.dumps(
                {"message":"user delete", "id":f"{id}"}),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print("*******")
        print(ex)
        print("*******")
#################################
#################################
if __name__ == "__main__":
    app.run(debug=True)