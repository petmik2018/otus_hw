from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    GO_HOME = (By.CLASS_NAME, 'fa-home')

    def __init__(self, browser):
        self.browser = browser

    def _click_element(self, locator):
        try:
            element = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(locator))
            element.click()
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))
        return element

    def _find_element(self, locator):
        try:
            element = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))
        return element

    def _find_list_of_elements(self, locator):
        try:
            elements_list = WebDriverWait(self.browser, 2).until(EC.visibility_of_any_elements_located(locator))
        except TimeoutException:
            raise AssertionError("Cant find elements by locator: {}".format(locator))
        return elements_list

    def _find_element_in_element(self, element, locator: tuple):
        time_limit = 2
        delta_time = 0.1
        curr_time = 0
        while True:
            if curr_time > time_limit:
                raise AssertionError("Cant find elements by locator: {}".format(locator))
            try:
                sub_element = element.find_element(*locator)
                return sub_element
            except NoSuchElementException:
                curr_time += delta_time

    def _find_list_of_elements_in_element(self, element, locator: tuple):
        time_limit = 2
        delta_time = 0.1
        curr_time = 0
        while True:
            if curr_time > time_limit:
                raise AssertionError("Cant find list of elements by locator: {}".format(locator))
            elements_list = element.find_elements(*locator)
            if elements_list:
                return elements_list
            else:
                curr_time += delta_time

    def go_to_main_page(self):
        self._click_element(self.GO_HOME)
