from rpa.xiachufang_robot import XiaChuFang_Robot
from constants import TaskType, TaskUrl, SqlState
from rpa.xinshipu_robot import XinShiPu_Robot
from rpa.meishitianxia_robot import MeiShiTianXia_Robot
from rpa.shuguowang_robot import ShuGuoWang_Robot
from unil import log_t, SqlMaster


class RpaMaster:
    def __init__(self, default_config):
        self.config = default_config
        log_t(f'default_config = {self.config}')
        self.task_type = self.config.get('task_type')
        self.sql_state = self.config.get('sql_info').get('state')
        # todo 需要sql
        # self.sql_state = None
        # if self.sql_state == SqlState.ON:
        #     self.sql_master = SqlMaster(self.config)


    def create_robot(self):
        try:
            if self.task_type == TaskType.XIACHUFANG.value:
                XiaChuFang_Robot(self.config, TaskUrl.XIACHUFANG.value, self.sql_master).run_task()
            elif self.task_type == TaskType.XINSHIPU.value:
                XinShiPu_Robot(self.config, TaskUrl.XINSHIPU.value, self.sql_master).run_task()
            elif self.task_type == TaskType.MEISHITIANXIA.value:
                MeiShiTianXia_Robot(self.config, TaskUrl.MEISHITIANXIA.value, self.sql_master).run_task()
            elif self.task_type == TaskType.SHUGUOWANG.value:
                ShuGuoWang_Robot(self.config, TaskUrl.SHUGUOWANG.value, self.sql_master).run_task()
        except Exception as e:
            log_t(e)
