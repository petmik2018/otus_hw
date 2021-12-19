from page_objects.AdminPage import AdminPage
from page_objects.MainPage import MainPage
from page_objects.CategoryPage import CategoryPage


def test_main_page_elements_verification(browser):
    MainPage(browser).verify_top()
    MainPage(browser).verify_top_links()
    MainPage(browser).verify_common_home()
    MainPage(browser).verify_content()
    MainPage(browser).verify_slideshow()
    MainPage(browser).verify_featured_products()


def test_admin_navigation(browser, url):
    browser.get(url + 'admin')
    AdminPage(browser).login_admin()
    AdminPage(browser).verify_element_by_ID('navigation')
    AdminPage(browser).verify_element_by_ID('menu')
    AdminPage(browser).logout_admin()


def test_category(browser, url):
    DESKTOPS_CATEGORY_URL = url + "index.php?route=product/category&path=20"
    LAPTOPS_CATEGORY_URL = url + "index.php?route=product/category&path=18"
    TABLETS_CATEGORY_URL = url + "index.php?route=product/category&path=57"
    browser.get(TABLETS_CATEGORY_URL)
    CategoryPage(browser).verify_product_category()
    CategoryPage(browser).verify_left_menu()
    CategoryPage(browser).verify_content()
    CategoryPage(browser).verify_products_list()
    CategoryPage(browser).verify_products_quantity()





