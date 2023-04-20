from rap_master import RpaMaster

default_config = {
    # "task_type": 1,
    # "url": "https://www.xiachufang.com/explore/?page=1",
    # "task_type": 2,
    # "url": "https://www.xinshipu.com/jiachangzuofa/16485/",
    "task_type": 3,
    "url": "https://home.meishichina.com/recipe/guangdongxiaochi/",
}

if __name__ == '__main__':
    RpaMaster(default_config).create_robot()
