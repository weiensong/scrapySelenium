from rpa.xiachufang_robot import XiaChuFang_Robot
from constants import TaskType


class RpaMaster:
    def __init__(self, default_config):
        self.config = default_config
        self.task_type = self.config.get('task_type')

    def create_robot(self):
        if self.task_type == TaskType.XIACHUFANG.value:
            XiaChuFang_Robot(self.config).run_task()
