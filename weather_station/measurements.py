from . import dto


measurements: dict[str, dto.Measurement] = {
    "temp":{
        "name":"Temperature",
        "description":"",
        "unitName":"Kelvin"
    },
    "pressure":{
        "name":"Pressure",
        "description":"Atmospheric pressure on sea level",
        "unitName":"hPa"
    },
    "humidity":{
        "name":"Humidity",
        "description":"Per cent",
        "unitName":"%"
    },
    "visibility":{
        "name":"Visibility",
        "description":"The maximum value of the visibility is 10000 m",
        "unitName":"m"
    },
    "windSpeed":{
        "name":"Wind Speed",
        "description":"",
        "unitName":"meter/sec"
    },
    "windDeg":{
        "name":"Wind Direction",
        "description":"0 is North",
        "unitName":"degrees"
    },
}
