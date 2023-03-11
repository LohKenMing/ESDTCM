from flask import Flask, request, jsonify
from flask_cors import CORS  
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# client = MongoClient("mongodb+srv://IS213:BvC5v1TtmRrA9sxD@is213project.obuxewm.mongodb.net/test") # replace this with your MongoDB URI
client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.0")
db = client["esdtcm"] # replace this with the name of your MongoDB database
collection = db["doctor"] # create a collection in the database to store patient records

class Order:
    def __init__(self, _id, patientID, drugID, drugName, status):
        self._id = _id
        self.patientID = patientID
        self.drugID = drugID
        self.drugName = drugName
        self.status = status

    def to_dict(self):
        return {
            "_id": str(self._id),
            "patientID": self.patientID,
            "drugID": self.drugID,
            "drugName": self.drugName,
            "status": self.status
        }

# Retrieve all orders
@app.route("/order")
def get_all():
    order_list = []
    for order in collection.find():
        order_list.append(Order(**order).to_dict())

    if len(order_list):
        print("TEST")
        return jsonify({
            "code": 200,
            "data": {"order": order_list}
        })

    return jsonify({
        "code": 404,
        "message": "There are no orders."
    }), 404


#find order by orderID
@app.route("/order/<string:orderID>")
def find_by_orderID(orderID):
    order_list = []
    for order in collection.find():
        order_list.append(Order(**order).to_dict())
    
    if len(order_list):
        return jsonify({
            "code": 200,
            "data": {"order": order_list}
        })
        
    return jsonify({
        "code": 404,
        "message": "Order not found."
    }), 404
    

#Create order
@app.route("/order/<string:orderID>/<string:drugID>")
def create_order():
    data = request.get_json()
    order = Order(**data)
    
    try:
        collection.insert_one(order.to_dict())
    except:
        return jsonify({
            "code": 500,
            "data": {
                "orderID": order.orderID,
                "patientID": order.patientID,
                "drugID": order.drugID,
                "drugName": order.drugName,
                "status": order.status
            }
            }),500
    return jsonify({
        "code": 201,
        "data": order.to_dict()
    }), 201

#update order by orderID
@app.route("/order/<string:orderID>", methods=["PUT"])
def update_order(orderID):
    order = Order.query.filter_by(orderID=orderID).first()
    if order:
        data = request.get_json()
        for key, item in data.items():
            setattr(order, key, item)
        db.session.commit()
        return jsonify({
            "code": 200,
            "data": order.json()
            })
    return jsonify({
        "code": 404,
        "message": "Order not found."
    }), 404
    
if __name__ == "__main__":
    app.run(port=5001, debug=True)    
            