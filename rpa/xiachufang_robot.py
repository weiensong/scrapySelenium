from abc import ABC

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from robot import Robot


class XiaChuFang_Robot(Robot, ABC):
    def __init__(self, default_config):
        super().__init__(default_config)

    def run_task(self):
        food_list = self.find_eles_xpath('//div[@class="info pure-u"]/p[@class="name"]/a')
        for food in food_list:

            food.click()
            self.switch_last_window()
            try:
                self.wait_ele_by_xpath('//h1', 20)

            except TimeoutException:
                self.refresh()
                self.wait_ele_by_xpath('//h1', 20)
            food_name = self.get_ele_text('//h1')
            # todo 获取用料
            food_ma_list = []
            food_kg_list = []
            food_matril = self.find_eles_xpath('//table//tr/td[1]')
            # 遍历，
            for i, food_ma in enumerate(food_matril):
                if food_ma.text == '':
                    food_ma_list.append(self.get_ele_text(f'//table//tr[{i}]/td[1]/a'))
                else:
                    food_ma_list.append(food_ma.text)
            food_matril = self.find_eles_xpath('//table//tr/td[2]')
            for i, food_ma in enumerate(food_matril):
                food_kg_list.append(food_ma.find_element(By.XPATH, '//table//tr/td[2]').text)
                # print(food_m)
            print(food_ma_list,food_kg_list)



            self.close_window()
            self.switch_default_windows()
