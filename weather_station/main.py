import time
import logging

import constants
import tasks

if __name__ == "__main__":
    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.INFO)
    c_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)

    logging.basicConfig(level=logging.DEBUG, handlers=[c_handler])
    logger = logging.getLogger(__name__)
    logger.addHandler(c_handler)
    logging.debug('Start')


def main():
    TASK_LIST = [tasks.get_weather_task] * constants.GET_WEATHER_WEIGHT + \
                [tasks.send_weather_task] * constants.SEND_METRICS_WEIGHT
    logger.debug(f'{constants.GET_WEATHER_WEIGHT=}')
    logger.debug(f'{constants.SEND_METRICS_WEIGHT=}')
    logger.info('Task list generated')
    while True:
        for task in TASK_LIST:
            try:
                task()
            except Exception as e:
                logger.error(
                    'While processing task an error was occurred: %s', e)
            time.sleep(constants.COOLDOWN_SEC)


if __name__ == "__main__":
    main()
