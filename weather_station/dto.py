from typing import TypedDict
from datetime import date, time


class Location(TypedDict):
    name: str
    latitude: str
    longtitude: str


class Measurement(TypedDict):
    name: str
    description: str
    unit: str
    value: float | int


class Metric(TypedDict):
    location: Location
    measurement: Measurement
    date: date
    time: time
