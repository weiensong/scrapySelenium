from enum import unique, IntEnum, Enum


@unique
class TaskType(IntEnum):
    XIACHUFANG = 1  # 下厨房
    XINSHIPU = 2  # 心食谱
    MEISHITIANXIA = 3  # 美食天下


@unique
class TaskUrl(Enum):
    XIACHUFANG = 'https://www.xiachufang.com/explore/?page=1'
    XINSHIPU = 'https://www.xinshipu.com/jiachangzuofa/16485/'
    MEISHITIANXIA = 'https://home.meishichina.com/recipe/guangdongxiaochi/'
