import dto


measurements: dict[str, dto.Measurement] = {
    "temp": {
        "name": "temp",
        "description": "The Temperature refers to the actual temperature at a specific location or time",
        "unit": "Kelvin"
    },
    "feels_like": {
        "name":  "feels_like",
        "description": "Temperature Feels Like represents the perceived temperature, which may vary from the actual temperature due to factors like humidity and wind.",
        "unit": "Kelvin"
    },
    "temp_min": {
        "name": "temp_min",
        "description": "Temperature Min signifies the minimum temperature recorded within a specific period, providing insights into the coldest conditions.",
        "unit": "Kelvin"
    },
    "temp_max": {
        "name": "temp_max",
        "description": "Temperature Max indicates the maximum temperature observed within a specific timeframe, offering information about the warmest conditions.",
        "unit": "Kelvin"
    },
    "pressure": {
        "name":  "pressure",
        "description": "Pressure refers to the atmospheric pressure at sea level, representing the force exerted by the air molecules in the atmosphere.",
        "unit": "hPa"
    },
    "humidity": {
        "name":  "humidity",
        "description": "Humidity indicates the amount of water vapor present in the air, expressed as a percentage. It reflects the air's moisture content.",
        "unit": "%"
    },

    "wind_speed": {
        "name": "wind_speed",
        "description": "Wind Speed represents the rate at which air is moving horizontally. It provides information about how fast the wind is blowing.",
        "unit": "meter/sec"
    },
    "wind_deg": {
        "name": "wind_deg",
        "description": "Wind Direction indicates the compass direction from which the wind is blowing. It provides insights into the orientation of the wind.",
        "unit": "degrees"
    },
    "rain_1h": {
        "name": "rain_1h",
        "description": "Rain_1h represents the amount of rainfall recorded in the last hour.",
        "unit": "mm/h"
    },
    "snow_1h": {
        "name":  "snow_1h",
        "description": "Snow_1h indicates the amount of snowfall observed in the last hour.",
        "unit": "mm/h"
    },
    "clouds_all": {
        "name": "clouds_all",
        "description": "Clouds_All refers to the percentage of the sky covered by clouds, indicating the extent of cloud coverage.",
        "unit": "%"
    },
    "weather_main": {
        "name": "weather_main",
        "description": "Weather_Main represents the main weather condition or category, such as Clear, Clouds, Rain, etc. It provides a general description of the current weather.",
        "unit": "degrees"
    }

}
