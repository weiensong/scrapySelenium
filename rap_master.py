from rpa.xiachufang_robot import XiaChuFang_Robot
from constants import TaskType, TaskUrl
from rpa.xinshipu_robot import XinShiPu_Robot
from rpa.meishitianxia_robot import MeiShiTianXia_Robot
from rpa.shuguowang_robot import ShuGuoWang_Robot
from unil import log_t


class RpaMaster:
    def __init__(self, default_config):
        self.config = default_config
        log_t(self.config)
        self.task_type = self.config.get('task_type')

    def create_robot(self):
        try:
            if self.task_type == TaskType.XIACHUFANG.value:
                XiaChuFang_Robot(self.config, TaskUrl.XIACHUFANG.value).run_task()
            elif self.task_type == TaskType.XINSHIPU.value:
                XinShiPu_Robot(self.config, TaskUrl.XINSHIPU.value).run_task()
            elif self.task_type == TaskType.MEISHITIANXIA.value:
                MeiShiTianXia_Robot(self.config, TaskUrl.MEISHITIANXIA.value).run_task()
            elif self.task_type == TaskType.SHUGUOWANG.value:
                ShuGuoWang_Robot(self.config, TaskUrl.SHUGUOWANG.value).run_task()
        except Exception as e:
            log_t(e)
