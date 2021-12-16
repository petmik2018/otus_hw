from selenium.webdriver.common.by import By
from .BasePage import BasePage


class CategoryPage(BasePage):
    PRODUCTS_LIST = (By.CLASS_NAME, 'product-layout')

    def verify_element_by_ID(self, element_ID):
        self._find_element((By.ID, element_ID))

    def find_products_list(self):
        return self._find_list_of_elements(self.PRODUCTS_LIST)
