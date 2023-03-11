from flask import Flask, request, jsonify
from flask_cors import CORS  
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# client = MongoClient("mongodb+srv://IS213:BvC5v1TtmRrA9sxD@is213project.obuxewm.mongodb.net/test") # replace this with your MongoDB URI
# client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.0")
# db = client["esdtcm"] # replace this with the name of your MongoDB database
# collection = db["doctor"] # create a collection in the database to store patient records

client = MongoClient("mongodb+srv://IS213:BvC5v1TtmRrA9sxD@is213project.obuxewm.mongodb.net/?retryWrites=true&w=majority")
db = client["IS213Database"] # replace this with the name of your MongoDB database
collection = db.doctor

class Doctor:
    def __init__(self, _id, name, username, practice):
        self._id = _id
        self.name = name
        self.username = username
        self.practice = practice

    def to_dict(self):
        return {
            "_id": str(self._id),
            "name": self.name,
            "username": self.username,
            "practice": self.practice
        }


@app.route("/doctor")
def get_all():
    doctor_list = []
    for doctor in collection.find():
        doctor_list.append(Doctor(**doctor).to_dict())

    if len(doctor_list):
        print("TEST")
        return jsonify({
            "code": 200,
            "data": {"doctor": doctor_list}
        })

    return jsonify({
        "code": 404,
        "message": "There are no doctors."
    }), 404


@app.route("/doctor/<string:doctorID>")
def find_by_doctorID(doctorID):
    doctor = collection.find_one({"doctorID": doctorID})
    if doctor:
        return jsonify({
            "code": 200,
            "data": doctor(**doctor).to_dict()
        })
    return jsonify({
        "code": 404,
        "message": "Doctor not found."
    }), 404


@app.route("/doctor", methods=['POST'])
def create_doctor():
    data = request.get_json()
    doctor = doctor(**data)

    try:
        collection.insert_one(doctor.to_dict())
    except:
        return jsonify({
            "code": 500,
            "data": {"doctorID": doctor.doctorID},
            "message": "An error occurred while creating the doctor record."
        }), 500

    return jsonify({
        "code": 201,
        "data": doctor.to_dict()
    }), 201


## 
@app.route("/doctor/<string:doctorID>", methods=['PUT'])
def update_doctor(doctorID):
    doctor = collection.find_one({"doctorID": doctorID})
    if doctor:
        data = request.get_json()
        for key, item in data.items():
            doctor[key] = item
        collection.replace_one({"doctorID": doctorID}, doctor)
        return jsonify({
            "code": 200,
            "data": doctor(**doctor).to_dict()
        })
    return jsonify({
        "code": 404,
        "message": "Doctor not found."
    }), 404


if __name__ == '__main__':
    app.run(port=5001, debug=True)
