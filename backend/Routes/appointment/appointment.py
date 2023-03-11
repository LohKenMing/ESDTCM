from flask import Flask, request, jsonify
from flask_cors import CORS  
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# client = MongoClient("mongodb+srv://IS213:BvC5v1TtmRrA9sxD@is213project.obuxewm.mongodb.net/test") # replace this with your MongoDB URI
client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.0")
db = client["esdtcm"] # replace this with the name of your MongoDB database
collection = db["doctor"] # create a collection in the database to store patient records

class Appointment:
    def __init__(self, _id, date, time, duration, patientID, booked):
        self._id = _id
        self.date = date
        self.time = time
        self.duration = duration
        self.patientID = patientID
        self.booked = booked
        

    def to_dict(self):
        return {
            "_id": str(self._id),
            "date": self.date,
            "time": self.time,
            "patientID": self.patientID,
            "duration": self.duration,
            "booked": self.booked
        }

#display all appointments
@app.route("/appointment")
def get_all():
    appointment_list = []
    for appointment in collection.find():
        appointment_list.append(Appointment(**appointment).to_dict())

    if len(appointment_list):
        print("TEST")
        return jsonify({
            "code": 200,
            "data": {"appointment": appointment_list}
        })

    return jsonify({
        "code": 404,
        "message": "There are no appointments."
    }), 404

#find appointment by appointmentID
@app.route("/appointment/<string:appointmentID>")
def find_by_appointmentID(appointmentID):
    appointment = collection.find_one({"appointmentID": appointmentID})
    if appointment:
        return jsonify({
            "code": 200,
            "data": appointment(**appointment).to_dict()
        })
    return jsonify({
        "code": 404,
        "message": "Appointment not found."
    }), 404

#create appointment
@app.route("/appointment", methods=["POST"])
def create_appointment():
    data = request.get_json()
    appointment = Appointment(**data)
    
    try:
        collection.insert_one(appointment.to_dict())
    except:
        return jsonify({
            "code": 500,
            "data": {"appointmentID": appointment.appointmentID},
            "message": "An error occurred while creating Appointment."
        }), 500
        
    return jsonify({
        "code": 201,
        "data": appointment.to_dict()
    }),201

#update appointment
@app.route("/appointment/<string:appointmentID>", methods=["PUT"])
def update_appointment(appointmentID):
    appointment = collection.find_one({"appointmentID": appointmentID})
    if appointment:
        data = request.get_json()
        for key, item in data.items():
            appointment[key] = item
        collection.replace_one({"appointmentID": appointmentID}, appointment)

        return jsonify({
            "code": 200,
            "data": appointment(**appointment).to_dict()
        })
    return jsonify({
        "code": 404,
        "message": "Appointment not found."
    }), 404

#delete appointment
@app.route("/appointment/<string:appointmentID>", methods=["DELETE"])
def delete_appointment(appointmentID):
    appointment = collection.find_one({"appointmentID": appointmentID})
    if appointment:
        collection.delete_one({"appointmentID": appointmentID})
        return jsonify({
            "code": 200,
            "data": appointment(**appointment).to_dict()
        })
    return jsonify({
        "code": 404,
        "message": "Appointment not found."
    }), 404
    
if __name__ == "__main__":
    app.run(port=5001, debug=True)    
    