from page_objects.AdminPage import AdminPage
from page_objects.MainPage import MainPage
from page_objects.CategoryPage import CategoryPage


def test_main_page_elements(browser):
    page = MainPage(browser).open()
    page.verify_top()
    page.verify_top_links()
    page.verify_common_home()
    page.verify_content()
    page.verify_slideshow()
    page.verify_featured_products()


def test_admin_navigation(browser):
    page = AdminPage(browser).open()
    page.login_admin()
    page.verify_navigation()
    page.verify_menu()
    page.logout_admin()


def test_category(browser):
    page = CategoryPage(browser)
    page.open_components_category()
    page.verify_product_category()
    page.verify_left_menu()
    page.verify_content()
    page.verify_products_list()
    page.verify_products_quantity()





