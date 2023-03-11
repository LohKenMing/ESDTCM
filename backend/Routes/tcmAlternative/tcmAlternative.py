from flask import Flask, request, jsonify
from flask_cors import CORS  
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# client = MongoClient("mongodb+srv://IS213:BvC5v1TtmRrA9sxD@is213project.obuxewm.mongodb.net/test") # replace this with your MongoDB URI
client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.0")
db = client["esdtcm"] # replace this with the name of your MongoDB database
collection = db["tcmalternative"] # create a collection in the database to store patient records


class AlternateDrug:
    def __init__(self, _id, drugname, altDrug):
        self._id = _id
        self.drugname = drugname
        self.altDrug = altDrug

    def to_dict(self):
        return {
            "_id": str(self._id),
            "drugname": self.drugname,
            "altDrug": self.altDrug,
        }


@app.route("/tcmalternative")
def get_all():
    tcmalternative_list = []
    for tcmalternative in collection.find():
        tcmalternative_list.append(AlternateDrug(**tcmalternative).to_dict())

    if len(tcmalternative_list):
        print("TEST")
        return jsonify({
            "code": 200,
            "data": {"tcmalternative": tcmalternative_list}
        })

    return jsonify({
        "code": 404,
        "message": "There are no alternative medicine."
    }), 404


@app.route("/tcmalternative/<string:tcmalternativeID>")
def find_by_tcmalternativeID(tcmalternativeID):
    tcmalternative = collection.find_one({"tcmalternativeID": tcmalternativeID})
    if tcmalternative:
        return jsonify({
            "code": 200,
            "data": tcmalternative(**tcmalternative).to_dict()
        })
    return jsonify({
        "code": 404,
        "message": "Alternative medicine not found."
    }), 404


@app.route("/tcmalternative", methods=['POST'])
def create_tcmalternative():
    data = request.get_json()
    tcmalternative = tcmalternative(**data)

    try:
        collection.insert_one(tcmalternative.to_dict())
    except:
        return jsonify({
            "code": 500,
            "data": {"tcmalternativeID": tcmalternative.tcmalternativeID},
            "message": "An error occurred while creating the alternative medicine."
        }), 500

    return jsonify({
        "code": 201,
        "data": tcmalternative.to_dict()
    }), 201


## 
@app.route("/tcmalternative/<string:tcmalternativeID>", methods=['PUT'])
def update_tcmalternative(tcmalternativeID):
    tcmalternative = collection.find_one({"tcmalternativeID": tcmalternativeID})
    if tcmalternative:
        data = request.get_json()
        for key, item in data.items():
            tcmalternative[key] = item
        collection.replace_one({"tcmalternativeID": tcmalternativeID}, tcmalternative)
        return jsonify({
            "code": 200,
            "data": tcmalternative(**tcmalternative).to_dict()
        })
    return jsonify({
        "code": 404,
        "message": "Alternative medicine not found."
    }), 404


if __name__ == '__main__':
    app.run(port=5001, debug=True)
