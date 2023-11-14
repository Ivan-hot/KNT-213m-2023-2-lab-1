import random
import requests
import logging
from . import file_utils
from . import urls
from . import weather_provider
from .locations import locations


logger = logging.getLogger(__name__)


def get_weather_task() -> None:
    logger.info('TASK: get weather')
    timestamp = weather_provider.get_weather_data(random.choice(locations))
    if timestamp is not None:
        file_utils.write_json(timestamp)
    return None


def send_weather_task() -> None:
    logger.info('TASK: send weather')
    resp = requests.post(urls.BAZA_URL, json=file_utils.read_json())
    if resp.status_code == 200:
        file_utils.flush_json()
    else:
        logger.info('Failed to send metrics to BAZA')
    return None