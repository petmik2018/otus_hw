from selenium.webdriver.common.by import By
from .BasePage import BasePage


class CategoryPage(BasePage):
    PRODUCTS_LIST = (By.CLASS_NAME, 'product-layout')
    PRODUCT_CATEGORY = (By.ID, 'product-category')
    LEFT_MENU = (By.ID, 'column-left')
    CONTENT = (By.ID, 'content')
    INFO = (By.CLASS_NAME, 'text-right')

    def verify_left_menu(self):
        self._find_element(self.LEFT_MENU)

    def verify_product_category(self):
        self._find_element(self.PRODUCT_CATEGORY)

    def verify_content(self):
        self._find_element(self.CONTENT)

    def verify_products_list(self):
        assert self._find_list_of_elements(self.PRODUCTS_LIST)

    def verify_products_quantity(self):
        products_qty = len(self._find_list_of_elements(self.PRODUCTS_LIST))
        content = self._find_element(self.CONTENT)
        information = self._find_element_in_element(content, self.INFO).text
        quantity_info = int(information.split(' ')[5])
        assert products_qty == quantity_info
