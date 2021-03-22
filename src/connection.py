
import pymongo
import certifi

def obtener_bd():
    client = pymongo.MongoClient("mongodb+srv://rapser:rapser2018@cluster0.5zuzx.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where())
    return client



    # host = "cluster0.5zuzx.mongodb.net"
    # puerto = "27017"
    # usuario = "rapser"
    # palabra_secreta = "rapser2018"
    # base_de_datos = "tienda"
    # mongodb+srv://rapser:<password>@cluster0.5zuzx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority