import logging
import inspect

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    GO_HOME = (By.CLASS_NAME, 'fa-home')
    LOGGER_FORMAT ='%(asctime)s  - %(levelname)s - %(name)s - %(message)s'
    LOG_LEVEL = logging.INFO

    def __init__(self, browser):
        self.browser = browser
        self.base_url = browser.base_url
        self.__config_logger()

    def __config_logger(self):
        self.logger = logging.getLogger(type(self).__name__)
        formatter = logging.Formatter(self.LOGGER_FORMAT)
        f = logging.FileHandler(f"logs/{self.browser.test_name}.log")
        f.setFormatter(formatter)
        self.logger.addHandler(f)
        self.logger.setLevel(level=self.LOG_LEVEL)

    @property
    def __method_name(self):
        return inspect.stack()[2][3]

    def __make_screenshot(self):
        self.browser.save_screenshot(f'logs/{inspect.stack()[2][3]}.png')

    def _open(self, path=""):
        url = self.base_url + path
        self.logger.info("{} - Opening url: {}".format(self.__method_name, url))
        self.browser.get(url)

    def _click_element(self, locator):
        self.logger.info("{} - Clicking element: {}".format(self.__method_name, locator))
        try:
            element = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(locator))
            element.click()
        except TimeoutException:
            self.logger.error("{} - Error with clicking element: {}".format(self.__method_name, locator))
            self.__make_screenshot()
            raise AssertionError("Cant find element by locator: {}".format(locator))
        return element

    def _find_element(self, locator):
        self.logger.info("{} - Finding element: {}".format(self.__method_name, locator))
        try:
            element = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.error("{} - Error with finding element: {}".format(self.__method_name, locator))
            self.__make_screenshot()
            raise AssertionError("Cant find element: {}".format(locator))
        return element

    def _find_list_of_elements(self, locator):
        self.logger.info("{} - Finding list of elements: {}".format(self.__method_name, locator))
        try:
            elements_list = WebDriverWait(self.browser, 2).until(EC.visibility_of_any_elements_located(locator))
        except TimeoutException:
            self.logger.error("{} - Error with finding list of elements: {}".format(self.__method_name, locator))
            self.__make_screenshot()
            raise AssertionError("Cant find elements by locator: {}".format(locator))
        return elements_list

    def _find_element_in_element(self, element, locator: tuple):
        self.logger.info("{} - Finding element {} inside the parent element".format(self.__method_name, locator))
        time_limit = 2
        delta_time = 0.1
        curr_time = 0
        while True:
            if curr_time > time_limit:
                self.logger.error("{} - Error with finding element: {} inside the mother element".format(self.__method_name, locator))
                self.__make_screenshot()
                raise AssertionError("Cant find elements by locator: {}".format(locator))
            try:
                sub_element = element.find_element(*locator)
                return sub_element
            except NoSuchElementException:
                curr_time += delta_time

    def _find_list_of_elements_in_element(self, element, locator: tuple):
        self.logger.info("{} - Finding list of element by locator {} inside the parent element".format(self.__method_name, locator))
        time_limit = 2
        delta_time = 0.1
        curr_time = 0
        while True:
            if curr_time > time_limit:
                self.logger.error("{} - Error with finding list of elements: {} inside the mother element".format(self.__method_name, locator))
                self.__make_screenshot()
                raise AssertionError("Cant find list of elements by locator: {}".format(locator))
            elements_list = element.find_elements(*locator)
            if elements_list:
                return elements_list
            else:
                curr_time += delta_time

    def go_to_main_page(self):
        self._click_element(self.GO_HOME)
