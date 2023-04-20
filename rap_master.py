from rpa.xiachufang_robot import XiaChuFang_Robot
from constants import TaskType
from rpa.xinshipu_robot import XinShiPu_Robot
from rpa.meishitianxia_robot import MeiShiTianXia_Robot


class RpaMaster:
    def __init__(self, default_config):
        self.config = default_config
        self.task_type = self.config.get('task_type')

    def create_robot(self):
        if self.task_type == TaskType.XIACHUFANG.value:
            XiaChuFang_Robot(self.config).run_task()
        if self.task_type == TaskType.XINSHIPU.value:
            XinShiPu_Robot(self.config).run_task()
        if self.task_type == TaskType.MEISHITIANXIA.value:
            MeiShiTianXia_Robot(self.config).run_task()
