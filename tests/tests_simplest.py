from page_objects.AdminPage import AdminPage
from page_objects.MainPage import MainPage
from page_objects.CategoryPage import CategoryPage


def test_main_page_elements_verification(browser):
    # main page elements verification
    MainPage(browser).verify_element_by_ID("top")
    MainPage(browser).verify_element_by_ID("top-links")
    MainPage(browser).verify_element_by_ID("common-home")


def test_admin_navigation(browser, url):
    # admin page elements verification
    browser.get(url + 'admin')
    AdminPage(browser).login_admin()
    AdminPage(browser).verify_element_by_ID('navigation')
    AdminPage(browser).verify_element_by_ID('menu')
    AdminPage(browser).logout_admin()


def test_laptops_catalogue(browser, url):
    # laptops catalogue test, check products quantity
    browser.get(url + "index.php?route=product/category&path=18")
    CategoryPage(browser).verify_element_by_ID("column-left")
    CategoryPage(browser).verify_element_by_ID("content")
    CategoryPage(browser).verify_element_by_ID("product-category")
    products = CategoryPage(browser).find_products_list()
    assert len(products) == 5




