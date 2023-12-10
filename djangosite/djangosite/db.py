from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import ConnectionFailure, OperationFailure
from constants import *
from datetime import datetime


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


def get_document(Coll_Name: str, id: int, name: str):
    try:
        db = connect_db()
        collection = db[Coll_Name]
        if id:
            document = collection.find_one({"_id": id})
        elif name:
            document = collection.find_one({"name": name})
            print(document)
        else:
            document = list(collection.find())
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


def get_location(id=None, name=None):
    get_document(COLL_LOCATION, id, name)


def get_measurement(id=None, name=None):
    get_document(COLL_MEASUREMENT, id, name)


def insert_measurement(name: str, description: str,  unit: str):
    try:
        db = connect_db()
        collection = db[COLL_MEASUREMENT]
        result = collection.insert_one(
            {'name': name, 'description': description, "unit": unit})
        return result
    except Exception as e:
        print(f"Error: {e}")


def insert_timestamp(measurement_id: int, value: str, location_id: int, date: datetime.now().date(), time: datetime.now().time()):
    try:
        db = connect_db()
        collection = db[COLL_MEASUREMENT]
        measurement = get_measurement(id=measurement_id)
        location = get_location(id=location_id)
        result = collection.insert_one(
            {'measurement': measurement, 'value': value, "location": location, "date": date, "time": time})
        return result
    except Exception as e:
        print(f"Error: {e}")


def get_timestamp(location_id=None, measurement_id=None, date=datetime.now().date()):
    filter = {}

    if location_id is not None:
        filter['location.id'] = location_id

    if measurement_id is not None:
        filter['measurement.id'] = measurement_id

    filter['date'] = date
    try:
        db = connect_db()
        collection = db[COLL_TIMESTAMPS]
        documents = list(collection.find(
            filter).sort([('date', -1), ('time', 1)]))
        return documents

    except Exception as e:
        print(f"Error: {e}")


def get_timestamp_between_date(location_id=None, measurement_id=None, start_date=None, end_date=None):
    filter = {
        'measurement.id': measurement_id,
        'location.id': location_id,
        'value': {'$ne': ''}
    }
    if start_date is not None:
        filter['date']['$gte'] = start_date

    if end_date is not None:
        filter['date']['$lte'] = end_date

    try:
        db = connect_db()
        collection = db[COLL_TIMESTAMPS]
        documents = list(collection.find(filter))
        return documents

    except Exception as e:
        print(f"Error: {e}")
