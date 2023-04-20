from enum import unique, IntEnum, Enum


@unique
class TaskType(IntEnum):
    XIACHUFANG = 1  # 下厨房
    XINSHIPU = 2    # 心食谱
