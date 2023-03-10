from flask import Flask, request, jsonify
from flask_cors import CORS  
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

class Patient(db.Model):
    ## This is the table name in the database that we need to replace later
    __tablename__ = 'patient'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.Integer)

    def __init__(self, patientID, name, allergies,phoneNumber,email):
        self.patientID = patientID
        self.name = name
        self.allergies = allergies
        self.phoneNumber = phoneNumber
        self.email = email

    def __repr__(self):
        return '<Patient %r>' % self.name
    

    def json(self):
        return {"patientID": self.patientID, "name": self.name, "allergies": self.allergies, "phoneNumber": self.phoneNumber, "email": self.email}
    

@app.route("/patient")
def get_all():

    patientlist = Patient.query.all()

    if(len(patientlist)):
        return jsonify({
            "code": 200,
            "data": {
                "patient": [patient.json() for patient in patientlist]
            }
        })

    return jsonify({
        "code": 404,
        "message": "There are no patients."
    }), 404


@app.route("/patient/<string:patientID>")
def find_by_patientID(patientID):
    patient = Patient.query.filter_by(patientID=patientID).first()
    if patient:
        return jsonify({
            "code": 200,
            "data": patient.json()
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
        db.session.add(patient)
        db.session.commit()
    except:
        return jsonify({
            "code": 500,
            "data": {
                "patientID": patient.patientID
            },
            "message": "An error occurred creating the patient."
        }), 500

    return jsonify({
        "code": 201,
        "data": patient.json()
    }), 201

@app.route("/patient/<string:patientID>", methods=['PUT'])
def update_patient(patientID):
    patient = Patient.query.filter_by(patientID=patientID).first()
    if patient:
        data = request.get_json()
        for key, item in data.items():
            setattr(patient, key, item)
        db.session.commit()
        return jsonify({
            "code": 200,
            "data": patient.json()
        })
    return jsonify({
        "code": 404,
        "message": "Patient not found."
    }), 404


if __name__ == '__main__':
    app.run(port=5000, debug=True)

