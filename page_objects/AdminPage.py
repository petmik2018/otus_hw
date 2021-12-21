from selenium.webdriver.common.by import By

from .BasePage import BasePage


class AdminPage(BasePage):
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.btn.btn-primary')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '.fa-sign-out')
    CATALOG = (By.ID, "menu-catalog")
    PRODUCTS_LINK = (By.LINK_TEXT, "Products")
    FILTER_ICON = (By.CSS_SELECTOR, '[data-original-title="Filter"]')
    INPUT_NAME = (By.ID, "input-name")
    SUBMIT_FILTER = (By.ID, "button-filter")

    def login_admin(self):
        self._find_element(self.LOGIN_BUTTON).click()
        return self

    def logout_admin(self):
        self._find_element(self.LOGOUT_BUTTON).click()

    def verify_element_by_ID(self, element_ID):
        self._find_element((By.ID, element_ID))

    def go_to_products_list(self):
        self._click_element(self.CATALOG)
        self._click_element(self.PRODUCTS_LINK)

    def get_products_quantity(self):
        return len(BasePage(self.browser)._find_list_of_elements((By.TAG_NAME, "tr")))

    def get_product_name(self, number):
        form_products = self._find_element((By.ID, "form-product"))
        products_block = self._find_element_in_element(form_products, (By.TAG_NAME, "tbody"))
        products = self._find_list_of_elements_in_element(products_block, (By.TAG_NAME, "tr"))
        titles = self._find_list_of_elements_in_element(products[number-1], (By.TAG_NAME, "td"))
        return titles[2].text

    def open_filter_form(self):
        try:
            self._find_element((By.ID, "filter-product"))
        except:
            self._click_element(self.FILTER_ICON)
        return self

    def fill_name_field(self, data):
        self._click_element(self.INPUT_NAME).send_keys(data)
        return self

    def submit_filter(self):
        self._click_element(self.SUBMIT_FILTER)
