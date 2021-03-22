# products = [
#     {
#         "name": "Macbook-pro",
#         "price": 1800.00,
#         "quantity": 5
#     },
#     {
#         "name": "monitor",
#         "price": 900.00,
#         "quantity": 6
#     },    
#     {
#         "name": "mouse",
#         "price": 500.00,
#         "quantity": 2
#     }
# ]

# from products import products

# @app.route('/ping')
# def ping():
#     return jsonify({"message": "Hola Miguel"})

# @app.route('/products', methods=['GET'])
# def getProducts():
#     return jsonify({"message": "Lista de productos","products": products})


# @app.route('/products/<string:productName>', methods=['GET'])
# def getProduct(productName):
#     productsFound = [product for product in products if product['name'] == productName]
#     if (len(productsFound) > 0):
#         return jsonify({"product": productsFound[0]})
#     return jsonify({"message": "producto no encontrado"})

# @app.route('/products', methods=['POST'])
# def addProduct():
#     new_product = {
#         "name": request.json['name'],
#         "price": request.json['price'],
#         "quantity": request.json['quantity']
#     }

#     products.append(new_product)
#     return jsonify({"message": "producto agregado"})

# @app.route('/products/<string:product_name>', methods=['PUT'])
# def editProduct(product_name):
#     productFound = [product for product in products if product['name'] == product_name]
#     if (len(productFound) > 0):
#         productFound[0]['name'] = request.json['name']
#         productFound[0]['price'] = request.json['price']
#         productFound[0]['quantity'] = request.json['quantity']
#         return jsonify({"message": "producto actualizado"})

#     return jsonify({"message": "producto no encontrado"})

# @app.route('/products/<string:product_name>', methods=['DELETE'])
# def deleteProduct(product_name):
#     productFound = [product for product in products if product['name'] == product_name]
#     if (len(productFound) > 0):
#         products.remove(productFound[0])
#         return jsonify({"message": "producto eliminado"})

#     return jsonify({"message": "producto no encontrado"})

# class Producto:
#     def __init__(self, nombre, precio, cantidad):
#         self.nombre = nombre
#         self.precio = precio
#         self.cantidad = cantidad