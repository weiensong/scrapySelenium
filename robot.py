from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from unil import *


class Robot:

    def __init__(self, default_config):
        self.task = default_config
        self.url = self.task['url']
        self.task_type = default_config['task_type']
        self.time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("disable-blink-features=AutomationControlled")
        self.options.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.driver = webdriver.Chrome(options=self.options,
                                       executable_path='./webdriver/chromedriver_windows_111.exe')

        self.driver.get(self.url)
        self.driver.maximize_window()

    def run_task(self):
        raise NotImplementedError

    def kill_robot(self):
        self.driver.quit()

    def wait_ele_click_xpath_safe(self, xpath, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((By.XPATH, xpath)))
            self.driver.find_element(By.XPATH, xpath).click()
        except TimeoutException:
            ...

    def wait_ele_xpath_safe(self, xpath, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((By.XPATH, xpath)))
            if self.driver.find_element(By.XPATH, xpath):
                return True
        except TimeoutException:
            return False

    def wait_click_xpath(self, xpath, timeout=5):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((By.XPATH, xpath)))
        self.find_ele_click_xpath(xpath)

    def find_ele_click_xpath(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()

    def send_keys_xpath(self, xpath, keys):
        self.driver.find_element(By.XPATH, xpath).clear()
        self.driver.find_element(By.XPATH, xpath).send_keys(keys)

    def find_eles_xpath(self, xpath):
        eles = self.driver.find_elements(By.XPATH, xpath)
        if eles:
            return eles
        return []

    def click_to_last_window_xpath(self, xpath):
        self.find_ele_click_xpath(xpath)
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[-1])

    def get_ele_text(self, xpath):
        text = None
        try:
            text = self.driver.find_element(By.XPATH, xpath).text
        except Exception as e:
            ...
        return text

    def input_clear_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath).clear()

    def switch_last_window(self):
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[-1])

    def refresh(self):
        self.driver.refresh()

    def find_ele_xpath(self, xpath):
        try:
            ele = self.driver.find_element(By.XPATH, xpath)
            if ele:
                return True
        except Exception:
            return False

    def close_window(self):
        self.driver.close()

    def wait_ele_by_xpath(self, xpath, timeout=5):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((By.XPATH, xpath)))

    def switch_default_windows(self):
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[0])
