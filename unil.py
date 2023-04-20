import logging
from enum import unique, IntEnum, Enum
from datetime import datetime
import pytz


def log_t(args):
    logger = logging.getLogger('rpa')
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(filename='rpa.log',
                                       encoding='UTF-8')
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    logger.debug(f"{args}")
    logger.removeHandler(file_handler)
    logger.removeHandler(console_handler)


def get_time_now() -> datetime:
    return datetime.now(pytz.timezone('Asia/Shanghai')).now()


def get_time_now_str(args: datetime) -> str:
    return args.strftime('%Y-%m-%d %H:%M:%S')

