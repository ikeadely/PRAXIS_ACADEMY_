from flask import Flask, Response, jsonify, make_response, request
import pymongo
import json
from bson.objectid import ObjectId
app = Flask(__name__)

try:
    mongo= pymongo.MongoClient(
        host="localhost",
        port=27017,
        serverSelectionTimeoutMS = 1000
    )
    db = mongo.DATA_BULAN_JUNI
    mongo.server_info()
except:
    print("ERROR- Cannot connect to db")
# -----------------------------------------------
@app.route("/admin/create", methods=["POST"])
def create_admin():
    try:
        user = {
            'nama': request.form["nama"],
            'alamat': request.form["alamat"],
            'jenisKelamin': request.form["jenisKelamin"],
            'phoneNumber': request.form["phoneNumber"]
            }
        dbResponse = db.user.insert_one(user)
        return make_response(jsonify({"data": f"{user}", "message": "Success"})), 200

    except Exception as ex:
        return make_response(jsonify({"data": f"{ex}", "message": "Error"})), 400
# -----------------------------------------------
@app.route("/admin/read", methods=["GET"])
def get_some_users():
    try:
        data = list(db.user.find())
        arrayData = []
        for d in data:
            user["_id"]=str(user["_id"])
            arrayData.append({
                'nama': d["nama"],
                'alamat': d["alamat"],
                'jenisKelamin': d["jenisKelamin"],
                'phoneNumber': d["phoneNumber"]
            })
        # data = {
        #     "_id": 1
        # # }
        # print(data)
        return make_response(jsonify({"data": arrayData, "message": "Success"})), 200
    except Exception as ex:
        return make_response(jsonify({"data": f"{ex}", "message": "Error"})), 400
# -----------------------------------------------
@app.route("/admin/<id>", methods=["PATCH"])
def update_user(id):
    try:
        dbResponse = db.users.update_one(
            {"_id": ObjectId(id)},
            {"$set":{"nama":request.form["nama"]},
            }
        )
        if dbResponse.modified_count == 1:
            return Response(
                response=json.dumps(
                    {"message": "user update"}),
                status=200,
                mimetype="application/json"
            )
        return Response(
            response=json.dumps(
                {"message":"nothing to update"}),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print("*************")
        print(ex)
        print("*************")
        return Response(
            response=json.dumps(
                {"message":"sorry can't update user"}),
            status=500,
            mimetype="application/json"
            )
# -----------------------------------------------
@app.route("/admin/<id>", methods=["DELETE"])
def delete_user(id):
    try:
        dbResponse = db.users.delete_one({"_id":ObjectId(id)})
        if dbResponse.deleted_count == 1:
            return Response(
                response=json.dumps(
                    {"message": "user delete", "id":f"{id}"}),
                status=200,
                mimetype="application/json"
                )
    except Exception as ex:
        print("*************")
        print(ex)
        print("*************")
        return Response(
        response = json.dumps(
            {"message": "sorry can't delete user"}),
        status=500,
        mimetype="application/json"
        )
# -----------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)