# contact page test

def test_contact(browser, url):
    browser.get(url)

    element = browser.find_element_by_css_selector("#top-links a")
    element.click()

    browser.find_element_by_css_selector("#information-contact #content .panel")
    browser.find_element_by_css_selector("#information-contact #content .form-horizontal")
    browser.find_element_by_css_selector("#information-contact #content .form-horizontal .buttons")