from enum import unique, IntEnum, Enum


@unique
class DEBUG(IntEnum):
    NOT = 0
    IS = 1


@unique
class TaskType(IntEnum):
    XIACHUFANG = 1  # 下厨房
    XINSHIPU = 2  # 心食谱
    MEISHITIANXIA = 3  # 美食天下
    SHUGUOWANG = 4  # 蔬果网


@unique
class TaskUrl(Enum):
    XIACHUFANG = 'https://www.xiachufang.com/explore/?page=1'
    XINSHIPU = 'https://www.xinshipu.com/jiachangzuofa/16485/'
    MEISHITIANXIA = 'https://home.meishichina.com/recipe/guangdongxiaochi/'
    SHUGUOWANG = 'http://www.vegnet.com.cn/Market/477.html?page=1'
