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
    print("Todas los registros:")
    print("Cantidad de registros", collection.count_documents({}))
    docs = collection.find()
    for doc in docs:
        print(doc)

    # Consulta especifica en la base de datos de los registros
    print("Registros de la fecha 2015-01-05")
    print("Cantidad de registros:", collection.count_documents({"Date": "2015-01-05"}))
    docs1 = collection.find({"Date": "2015-01-05"})
    for doc in docs1:
        print(doc)

connection.close()