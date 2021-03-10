
from pymongo import pymongo

def obtener_bd():
    host = "cluster0.5zuzx.mongodb.net"
    puerto = "27017"
    usuario = "rapser"
    palabra_secreta = "rapser2018"
    base_de_datos = "tienda"
    # mongodb+srv://rapser:<password>@cluster0.5zuzx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
    client = pymongo.MongoClient("mongodb+srv://rapser:rapser2018@cluster0.5zuzx.mongodb.net/tienda?retryWrites=true&w=majority")
    return client.test