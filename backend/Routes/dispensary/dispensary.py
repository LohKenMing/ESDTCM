from flask import Flask, request, jsonify
from flask_cors import CORS  
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# client = MongoClient("mongodb+srv://IS213:BvC5v1TtmRrA9sxD@is213project.obuxewm.mongodb.net/test") # replace this with your MongoDB URI
client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.0")
db = client["esdtcm"] # replace this with the name of your MongoDB database
collection = db["dispensary"] # create a collection in the database to store patient records


class Dispensary:
    def __init__(self, _id, drugname, quantity):
        self._id = _id
        self.drugname = drugname
        self.quantity = quantity

    def to_dict(self):
        return {
            "_id": str(self._id),
            "drugname": self.drugname,
            "quantity": self.quantity,
        }


@app.route("/dispensary")
def get_all():
    dispensary_list = []
    for dispensary in collection.find():
        dispensary_list.append(Dispensary(**dispensary).to_dict())

    if len(dispensary_list):
        print("TEST")
        return jsonify({
            "code": 200,
            "data": {"dispensary": dispensary_list}
        })

    return jsonify({
        "code": 404,
        "message": "There are no medicine in the dispensary."
    }), 404


@app.route("/dispensary/<string:dispensaryID>")
def find_by_dispensaryID(dispensaryID):
    dispensary = collection.find_one({"dispensaryID": dispensaryID})
    if dispensary:
        return jsonify({
            "code": 200,
            "data": dispensary(**dispensary).to_dict()
        })
    return jsonify({
        "code": 404,
        "message": "Medicine not found."
    }), 404


@app.route("/dispensary", methods=['POST'])
def create_dispensary():
    data = request.get_json()
    dispensary = dispensary(**data)

    try:
        collection.insert_one(dispensary.to_dict())
    except:
        return jsonify({
            "code": 500,
            "data": {"dispensaryID": dispensary.dispensaryID},
            "message": "An error occurred while creating the medicine."
        }), 500

    return jsonify({
        "code": 201,
        "data": dispensary.to_dict()
    }), 201


## 
@app.route("/dispensary/<string:dispensaryID>", methods=['PUT'])
def update_dispensary(dispensaryID):
    dispensary = collection.find_one({"dispensaryID": dispensaryID})
    if dispensary:
        data = request.get_json()
        for key, item in data.items():
            dispensary[key] = item
        collection.replace_one({"dispensaryID": dispensaryID}, dispensary)
        return jsonify({
            "code": 200,
            "data": dispensary(**dispensary).to_dict()
        })
    return jsonify({
        "code": 404,
        "message": "Medicine not found."
    }), 404


if __name__ == '__main__':
    app.run(port=5001, debug=True)