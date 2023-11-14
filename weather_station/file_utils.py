from io import TextIOWrapper
import json
import logging
from . import constants
from . import dto


logger = logging.getLogger(__name__)


def read_json() -> list[dto.Metric]:
    data = []
    try:
        with open(constants.FILENAME,'r') as file:
            data = json.load(file)
    except OSError as e:
        logger.warning('Read file error: %s', e)
        create_file()
    return data


def write_json(timestamp: dto.Metric) -> None:
    data = read_json()
    data.append(timestamp)
    with open(constants.FILENAME, 'w') as file:
        json.dump(data, file, indent=2) 
    return None


def flush_json() -> None:
    with open(constants.FILENAME, 'w') as file:
        json.dump([], file, indent=2) 


def create_file() -> TextIOWrapper:
    with open(constants.FILENAME, 'w+') as file:
        json.dump([], file, indent=2)
    logger.info('File created: %s', constants.FILENAME)
    return file