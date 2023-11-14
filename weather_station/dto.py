from typing import TypedDict
from datetime import date, time


class Location(TypedDict):
    name: str
    latitude: str
    longtitude: str


class Measurement(TypedDict):
    name: str
    description: str
    unitName: str
    value: float | int


class Metric(TypedDict):
    location: Location
    measurment: Measurement
    date: date
    time: time