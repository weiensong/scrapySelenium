from rpa.xiachufang_robot import XiaChuFang_Robot
from constants import TaskType, TaskUrl, SqlState
from rpa.xinshipu_robot import XinShiPu_Robot
from rpa.meishitianxia_robot import MeiShiTianXia_Robot
from rpa.shuguowang_robot import ShuGuoWang_Robot
from unil import log_t
from abc import ABC


class RpaMaster(ABC):
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
            if self.task_type == TaskType.XIA_CHU_FANG.value:
                XiaChuFang_Robot(self.config, TaskUrl.XIA_CHU_FANG.value).run_task()
            elif self.task_type == TaskType.XIN_SHI_PU.value:
                XinShiPu_Robot(self.config, TaskUrl.XIN_SHI_PU.value).run_task()
            elif self.task_type == TaskType.MEI_SHI_TIAN_XIA.value:
                MeiShiTianXia_Robot(self.config, TaskUrl.MEI_SHI_TIAN_XIA.value).run_task()
            elif self.task_type == TaskType.SHU_GUO_WANG.value:
                ShuGuoWang_Robot(self.config, TaskUrl.SHU_GUO_WANG.value).run_task()
        except Exception as e:
            log_t(e)
