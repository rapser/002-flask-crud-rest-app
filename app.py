from flask import Flask, jsonify, request, Response
from bson import json_util
from bson.objectid import ObjectId

import pymongo
import certifi

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://rapser:rapser2018@cluster0.5zuzx.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where())
db = client['tienda']
print(client.list_database_names())

@app.route('/products/<string:id>', methods=['GET'])
def getProduct(id):

    product = db.productos.find_one({"_id": ObjectId(id)})
    response = json_util.dumps(product)
    return Response(response, mimetype='application/json')

@app.route('/products', methods=['GET'])
def getProducts():
    products = db.productos.find()
    res = json_util.dumps(products)
    return Response(res, mimetype='application/json')

@app.route('/products', methods=['POST'])
def addProduct():

    name = request.json['name']
    price = request.json['price']
    quantity = request.json['quantity']
    
    if name and price and quantity:
        db.productos.insert_one({
            'name': name,
            'price': price,
            'quantity': quantity
        })

    res = json_util.dumps({"message": "agregado"})
    return Response(res, mimetype='application/json')

@app.route('/products/<string:id>', methods=['DELETE'])
def deleteProduct(id):
    productFound = db.productos.delete_one({"_id": ObjectId(id)})
    response = json_util.dumps({"message": "eliminado"})
    return Response(response, mimetype='application/json')

@app.route('/products/<string:id>', methods=['PUT'])
def editProduct(id):

    name = request.json['name']
    price = request.json['price']
    quantity = request.json['quantity']

    db.productos.update_one({"_id": ObjectId(id)}, {"$set": {
        'name': name,
        'price': price,
        'quantity': quantity
    }})

    return jsonify({"message": "el usuario " + id + " fue actualizado"})

if (__name__) == '__main__' :
    app.run(debug= True, port= 4000)