from page_objects.AdminPage import AdminPage
from page_objects.MainPage import MainPage
from page_objects.ProductPage import ProductPage
from page_objects.UserPage import UserPage
from page_objects.WishListPage import WishListPage
from page_objects.CartPage import CartPage
from page_objects.elements.Alerts import SuccessAlert


def test_admin_products(browser, url):
    # admin page test  - choose one product from products list and filter the list by its name
    browser.get(url + 'admin')
    AdminPage(browser)\
        .login_admin()\
        .go_to_products_list()
    featured_product_name = AdminPage(browser).get_product_name(1)
    AdminPage(browser)\
        .open_filter_form()\
        .fill_name_field(featured_product_name)\
        .submit_filter()
    filtered_product_name = AdminPage(browser).get_product_name(1)
    AdminPage(browser).logout_admin()
    assert filtered_product_name == featured_product_name


def test_add_product_to_wish_list(browser, number=2):
    # main page test add to wishlist - add one of the featured products to wishlist
    product_name = MainPage(browser).get_featured_product_name(number)
    MainPage(browser).click_featured_product(number)
    ProductPage(browser).add_to_wish_list()
    SuccessAlert(browser).click_login()
    UserPage(browser)\
        .login_with("test2@mail.ru", "test")\
        .go_to_wish_list()
    WishListPage(browser)\
        .logout()\
        .go_to_main_page()
    CartPage(browser).verify_product(product_name)


def test_to_clear_wish_list(browser):
    # add some of featured products to wishlist and then clear wishlist
    test_add_product_to_wish_list(browser, number=1)
    test_add_product_to_wish_list(browser, number=3)
    test_add_product_to_wish_list(browser, number=4)

    MainPage(browser).go_to_wish_list()
    UserPage(browser).login_with("test2@mail.ru", "test")
    while True:
        try:
            WishListPage(browser).remove_first_product()
        except:
            break
    wish_list_info = WishListPage(browser).get_text_from_wishlist_link()
    assert wish_list_info == 'Wish List (0)'

