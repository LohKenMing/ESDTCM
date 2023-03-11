from flask import Flask, request, jsonify
from flask_cors import CORS  
from pymongo import MongoClient
# from flask_pymongo import PyMongo

app = Flask(__name__)
CORS(app)

# client = MongoClient("mongodb+srv://IS213:BvC5v1TtmRrA9sxD@is213project.obuxewm.mongodb.net/test") # replace this with your MongoDB URI
# client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.0")
# db = client["esdtcm"] # replace this with the name of your MongoDB database
# collection = db["patient"] # create a collection in the database to store patient records


# class Patient:
#     def __init__(self, _id, name, username, allergies, phoneNumber, email):
#         self._id = _id
#         self.username = username
# client = MongoClient("mongodb+srv://IS213:BvC5v1TtmRrA9sxD@is213project.obuxewm.mongodb.net/?retryWrites=true&w=majority")
# app.config["Mongo_URI"] = "mongodb+srv://IS213:BvC5v1TtmRrA9sxD@is213project.obuxewm.mongodb.net/?retryWrites=true&w=majority"
# db = client["IS213Database"] # replace this with the name of your MongoDB database
# collection = db["patient"] # create a collection in the database to store patient records
# mongodb_client = PyMongo(app)
# db = mongodb_client.db
# collection = db.patient
# app.config["MONGO_URI"] = "mongodb+srv://IS213:BvC5v1TtmRrA9sxD@is213project.obuxewm.mongodb.net/?retryWrites=true&w=majority"
# app.config["MONGO_URI"] = "mongodb+srv://IS213:BvC5v1TtmRrA9sxD@is213project.obuxewm.mongodb.net/?retryWrites=true&w=majority"
# app.config["MONGO_URI"] = "mongodb+srv://IS213:BvC5v1TtmRrA9sxD@is213project.obuxewm.mongodb.net/test"
# mongo = PyMongo(app)
# db = mongo.db
# collection = db.patient


client = MongoClient("mongodb+srv://IS213:BvC5v1TtmRrA9sxD@is213project.obuxewm.mongodb.net/?retryWrites=true&w=majority")
db = client["IS213Database"] # replace this with the name of your MongoDB database
collection = db.patient



class Patient:
    def __init__(self, _id, username, patientName, allergies, phoneNumber, email):
        self._id = _id
        self.username = username
        self.patientName = patientName
        self.allergies = allergies
        self.phoneNumber = phoneNumber
        self.email = email

    def to_dict(self):
        return {
            "_id": str(self._id),
            "username": self.username,
            "patientName": self.patientName,
            "allergies": self.allergies,
            "phoneNumber": self.phoneNumber,
            "email": self.email
        }


@app.route("/patient")
def get_all():
    patient_list = []
    for patient in collection.find():
        patient_list.append(Patient(**patient).to_dict())

    if len(patient_list):
        return jsonify({
            "code": 200,
            "data": {"patient": patient_list}
        })

    return jsonify({
        "code": 404,
        "message": "There are no patients."
    }), 404


@app.route("/patient/<string:username>")
def find_by_patientID(username):
    patient = collection.find_one({"username": username})
    if patient:
        return jsonify({
            "code": 200,
            "data": Patient(**patient).to_dict()
        })
    return jsonify({
        "code": 404,
        "message": "Patient not found."
    }), 404


@app.route("/patient", methods=['POST'])
def create_patient():
    data = request.get_json()
    patient = Patient(**data)

    try:
        collection.insert_one(patient.to_dict())
    except:
        return jsonify({
            "code": 500,
            "data": {"username": patient.username},
            "message": "An error occurred creating the patient."
        }), 500

    return jsonify({
        "code": 201,
        "data": patient.to_dict()
    }), 201



@app.route("/patient/<string:username>", methods=['PUT'])
def update_patient(username):
    patient = collection.find_one({"username": username})
    if patient:
        data = request.get_json()
        for key, item in data.items():
            patient[key] = item
        collection.replace_one({"username": username}, patient)
        return jsonify({
            "code": 200,
            "data": Patient(**patient).to_dict()
        })
    return jsonify({
        "code": 404,
        "message": "Patient not found."
    }), 404


if __name__ == '__main__':
    app.run(port=5001, debug=True)
