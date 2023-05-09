import pymongo
import pandas as pd
from datetime import datetime

# Conexión a mongo, creando la base de datos y una colección
connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection["demo001"]
collection = db["tennis"]

# Extracción de la data del csv y conversión a un diccionario de python
data = pd.read_csv("atp_tennis.csv").to_dict(orient="records")

if collection.count_documents({}) == 0:
    # Inserción o migración de la data del csv a la base de datos creada en mongo
    collection.insert_many(data)
else:
    # Consulta de todos los registros ingresados a la base de datos
    docs = collection.find()
    for doc in docs:
        print(doc)

connection.close()