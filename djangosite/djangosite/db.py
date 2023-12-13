from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import ConnectionFailure, OperationFailure
from .constants import *
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


def get_document(Coll_Name: str, id: str, name: str):
    try:
        document = []
        db = connect_db()
        collection = db[Coll_Name]
        if id:
            document = collection.find_one({"_id": id})
        elif name:
            document = list(collection.find({"name": name}))
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
        return get_location(id=result.inserted_id)
    except Exception as e:
        print(f"Error: {e}")


def get_location(id=None, name=None):
    return get_document(COLL_LOCATION, id, name)


def get_all_locations():
    return get_document(COLL_LOCATION, None, None)


def get_measurement(id=None, name=None):
    return get_document(COLL_MEASUREMENT, id, name)


def get_all_measurements():
    return get_document(COLL_MEASUREMENT, None, None)


def insert_measurement(name: str, description: str,  unit: str):
    try:
        db = connect_db()
        collection = db[COLL_MEASUREMENT]
        result = collection.insert_one(
            {'name': name, 'description': description, "unit": unit})

        return get_measurement(id=result.inserted_id)
    except Exception as e:
        print(f"Error: {e}")


def get_or_create_location(object):
    result = get_location(name=object["name"])
    if not result:
        result = insert_location(
            **object)
    else:
        result = result[0]
    return result


def get_or_create_measurement(object):
    result = get_measurement(name=object["name"])
    if len(result):
        if len(result) > 1:
            result = list(
                filter(lambda obj: obj["unit"] == object["unit"], result))[0]
        else:
            result = result[0]
    else:
        result = insert_measurement(
            **object)

    return result


def insert_timestamp(measurement, value, location, date, time):
    try:
        db = connect_db()
        collection = db[COLL_TIMESTAMPS]
        result = collection.insert_one(
            {'measurement': measurement, 'value': value, "location": location, "date": date, "time": time})
        return get_timestamp_by_params(id=result.inserted_id)
    except Exception as e:
        print(f"Error: {e}")


def get_timestamp_by_params(id=None, location_id=None, measurement_id=None, date=None, start_date=None, end_date=None):

    filter = {
        'measurement.id': measurement_id,
        'location.id': location_id,
        'value': {'$ne': ''}
    }
    if id:
        filter['id'] = id
    if date:
        filter['date'] = date
    else:
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
