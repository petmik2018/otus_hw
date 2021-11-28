# admin page test
import time

def test_laptops_catalogue(browser, url):
    browser.get(url + 'admin')

    # browser.find_element_by_css_selector("#container #header")
    # browser.find_element_by_css_selector("#container #content")
    # browser.find_element_by_css_selector("#container #footer")
    # browser.find_element_by_css_selector(".panel")
    # browser.find_element_by_css_selector(".panel-body")
    # browser.find_element_by_css_selector(".form-group")
    # browser.find_element_by_css_selector(".panel-body .text-right .btn")

    sub_button = browser.find_element_by_css_selector(".btn")
    sub_button.click()
    menu_sale = browser.find_element_by_id("menu-sale")
    menu_sale.click()
    sales = browser.find_elements_by_css_selector("#collapse26 li")
    sales[0].click()

    clients_data = browser.find_elements_by_tag_name("tr")
    assert len(clients_data) == 45
    time.sleep(1)




