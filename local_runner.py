from rap_master import RpaMaster

default_config = {
    "task_type": 1,
    "url": "https://www.xiachufang.com/explore/?page=1",
}

if __name__ == '__main__':
    RpaMaster(default_config).create_robot()
