# admin page test

def test_laptops_catalogue(browser, url):
    browser.get(url + 'admin')

    browser.find_element_by_css_selector("#container #header")
    browser.find_element_by_css_selector("#container #content")
    browser.find_element_by_css_selector("#container #footer")
    browser.find_element_by_css_selector(".panel")
    browser.find_element_by_css_selector(".panel-body")
    browser.find_element_by_css_selector(".form-group")
    browser.find_element_by_css_selector(".panel-body .text-right .btn")