from abc import ABC
from unil import *
from robot import Robot


class ShuGuoWang_Robot(Robot, ABC):
    def __init__(self, default_config, url):
        super().__init__(default_config, url)

    def run_task(self):
        price_list = self.find_eles_xpath('//ul[@id="NongHuaZhuanYongFei1"]/li/a')
        for price in price_list:
            price.click()
            self.switch_last_window()
            self.get_xigua_xianggu()
            if self.find_ele_xpath('//a[text()="下一页"]'):
                self.find_ele_click_xpath('//a[text()="下一页"]')
                data = self.get_xigua_xianggu().split("\n")
                self.close_window()
                self.switch_last_window()
                write_to_excel(data, './output/guoshuwang_data.xlsx')
                print(data)
            else:
                self.close_window()
                self.switch_last_window()

    def get_xigua_xianggu(self):
        rows = self.find_eles_xpath('//div[@class="pri_k"]/p')
        for row in rows:
            if '西瓜' in row.text or '香菇' in row.text:
                return row.text


