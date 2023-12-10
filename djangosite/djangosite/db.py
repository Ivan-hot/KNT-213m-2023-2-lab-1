from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import ConnectionFailure, OperationFailure
from constants import *


def connect_db() -> Database:
    try:
        client = MongoClient(DB_ADRESS, DB_PORT)
        db = client[DB_NAME]
        print("Connection success", db)
        return db
    except ConnectionFailure as e:
        print(f'Connection error: {e}')
    except OperationFailure as e:
        print(f'Operatin error: {e}')
    except Exception as e:
        print(f'Error: {e}')


def get_document_by_id(Coll_Name: str, id: int):
    try:
        db = connect_db()
        collection = db[Coll_Name]
        document = collection.find_one({"_id": id})
        return document
    except Exception as e:
        print(f"Error: {e}")


def get_document_by_name(Coll_Name: str, name: str):
    try:
        db = connect_db()
        collection = db[Coll_Name]
        document = collection.find_one({"name": name})
        return document
    except Exception as e:
        print(f"Error: {e}")


def insert_location(name: str, latitude: str,  longitude: str):
    try:
        db = connect_db()
        collection = db[COLL_LOCATION]
        result = collection.insert_one(
            {'name': name, 'latitude': latitude, "longitude": longitude})
        return result.inserted_id
    except Exception as e:
        print(f"Error: {e}")


def get_location_by_id(id: int):
    get_document_by_id(COLL_LOCATION, id)


def get_location_by_name(name: str):
    get_document_by_name(COLL_LOCATION, name)


def insert_measurement(name: str, description: str,  unit: str):
    try:
        db = connect_db()
        collection = db[COLL_MEASUREMENT]
        result = collection.insert_one(
            {'name': Metric_Dict[name], 'description': description, "unit": unit})
        return result.inserted_id
    except Exception as e:
        print(f"Error: {e}")


def get_measurement_by_id(id: int):
    get_document_by_id(COLL_MEASUREMENT, id)


def get_location_by_name(name: str):
    get_document_by_name(COLL_MEASUREMENT, name)
