from abc import ABC

from robot import Robot


class XiaChuFang_Robot(Robot, ABC):
    def __init__(self, default_config):
        super().__init__(default_config)

    def run_task(self):
        food_list = self.find_eles_xpath('//div[@class="info pure-u"]/p[@class="name"]/a')
        for food in food_list:
            food.click()
            self.switch_last_window()
            self.close_window()
            self.switch_default_windows()
