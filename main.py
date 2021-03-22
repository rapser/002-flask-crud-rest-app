from flask import Flask, jsonify, request, Response
from bson import json_util
from bson.objectid import ObjectId
from src.connection import obtener_bd

app = Flask(__name__)
import pymongo
import certifi

client = obtener_bd()
db = client['tienda']
collection = db.productos
#print(client.list_database_names())

@app.route('/products/<string:id>', methods=['GET'])
def getProduct(id):

    product = collection.find_one({"_id": ObjectId(id)})
    response = json_util.dumps(product)
    return Response(response, mimetype='application/json')

@app.route('/products', methods=['GET'])
def getProducts():
    products = collection.find()
    res = json_util.dumps(products)
    return Response(res, mimetype='application/json')

@app.route('/products', methods=['POST'])
def addProduct():

    name = request.json['name']
    price = request.json['price']
    quantity = request.json['quantity']
    
    if name and price and quantity:
        collection.insert_one({
            'name': name,
            'price': price,
            'quantity': quantity
        })

    res = json_util.dumps({"message": "agregado"})
    return Response(res, mimetype='application/json')

@app.route('/products/<string:id>', methods=['DELETE'])
def deleteProduct(id):
    productFound = collection.delete_one({"_id": ObjectId(id)})
    response = json_util.dumps({"message": "eliminado"})
    return Response(response, mimetype='application/json')

@app.route('/products/<string:id>', methods=['PUT'])
def editProduct(id):

    name = request.json['name']
    price = request.json['price']
    quantity = request.json['quantity']

    collection.update_one({"_id": ObjectId(id)}, {"$set": {
        'name': name,
        'price': price,
        'quantity': quantity
    }})

    return jsonify({"message": "el usuario " + id + " fue actualizado"})

if (__name__) == '__main__' :
    app.run(debug= True, port= 4000)