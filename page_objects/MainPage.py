from selenium.webdriver.common.by import By
from .BasePage import BasePage


class MainPage(BasePage):
    CONTENT = (By.ID, 'content')
    FEATURE_PRODUCTS = (By.CLASS_NAME, 'product-layout')
    FEATURE_PRODUCT_NAME = (By.CSS_SELECTOR, '.caption h4 a')
    GO_TO_WISHLIST = (By.ID, 'wishlist-total')

    def verify_element_by_ID(self, element_ID):
        self._find_element((By.ID, element_ID))

    def get_featured_product_by_number(self, number):
        index = number - 1
        content = self._find_element(self.CONTENT)
        products_list = self._find_list_of_elements_in_element(content, self.FEATURE_PRODUCTS)
        if number > len(products_list):
            raise AssertionError("Out of range in list by locator: {}".format(self.FEATURE_PRODUCTS))
        else:
            return products_list[index]

    def get_featured_product_name(self, number):
        featured_product = self.get_featured_product_by_number(number)
        product_name = self._find_element_in_element(featured_product, self.FEATURE_PRODUCT_NAME).text
        return product_name

    def click_featured_product(self, number):
        featured_product = self.get_featured_product_by_number(number)
        featured_product.click()
        return self

    def go_to_all_laptops(self):
        nav_menu = self.browser.find_element(*self.MAIN_MENU)
        nav_menu.find_elements(*self.DROPDOWN_MENU_LIST)[1].click()
        self.browser.find_elements(*self.OPENED_DROPDOWN_MENU)[2].click()

    def go_to_wish_list(self):
        self._click_element(self.GO_TO_WISHLIST)
