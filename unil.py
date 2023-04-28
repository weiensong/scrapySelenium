import logging
from enum import unique, IntEnum, Enum
from datetime import datetime

import pymysql
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


# 将字典数据写入本地MySQL，传入字典与表即可
def write_tolocal_mysql(dc, table):
    keys = ','.join(dc.keys())
    values = list(dc.values())
    values = str(values).split("[")[1]
    values = values.split("]")[0]
    conn = pymysql.connect(host='localhost', user='root', password='root', db='food', port=3306,
                           charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    sql = f'INSERT INTO {table}({keys}) VALUES ({values});'.format(table, keys, values)
    cursor.execute(sql)
    conn.commit()
    conn.close()
