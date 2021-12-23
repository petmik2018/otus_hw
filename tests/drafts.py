from page_objects.AdminPage import AdminPage
from page_objects.MainPage import MainPage
from page_objects.ProductPage import ProductPage
from page_objects.UserPage import UserPage
from page_objects.WishListPage import WishListPage
from page_objects.CartPage import CartPage
from page_objects.elements.Alerts import SuccessAlert

import time


def test_admin_filter_products(browser, url):
    page = AdminPage(browser).open()
    page\
        .login_admin()\
        .go_to_products_list()
    featured_product_name = page.get_product_name(1)
    page\
        .open_filter_form()\
        .fill_name_field(featured_product_name)\
        .submit_filter()
    filtered_product_name = page.get_product_name(1)
    page.logout_admin()
    assert filtered_product_name == featured_product_name


def test_add_product_to_wish_list(browser, number=2):
    main_page = MainPage(browser).open()
    product_name = main_page.get_featured_product_name(number)
    main_page.click_featured_product(number)
    ProductPage(browser).add_to_wish_list()
    SuccessAlert(browser).click_login()
    UserPage(browser)\
        .login_with("test2@mail.ru", "test")\
        .go_to_wish_list()
    WishListPage(browser)\
        .logout()\
        .go_to_main_page()
    CartPage(browser).verify_product(product_name)


def test_delete_product_from_wish_list(browser):
    MainPage(browser)\
        .open()\
        .go_to_wish_list()
    UserPage(browser).login_with("test2@mail.ru", "test")
    WishListPage(browser).remove_first_product()


def test_add_products_and_clear_wish_list(browser):
    test_add_product_to_wish_list(browser, number=1)
    test_add_product_to_wish_list(browser, number=3)

    MainPage(browser).open().go_to_wish_list()
    time.sleep(1)
    UserPage(browser).login_with("test2@mail.ru", "test")
    time.sleep(1)
    WishListPage(browser)\
        .remove_first_product()\
        .remove_first_product()

    wish_list_info = WishListPage(browser).get_text_from_wishlist_link()
    assert wish_list_info == 'Wish List (0)'

