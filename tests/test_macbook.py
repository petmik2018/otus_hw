# macbook product page test

def test_macbook(browser, url):
    browser.get(url)

    elements = browser.find_elements_by_css_selector(".product-layout a")
    elements[0].click()

    browser.find_element_by_css_selector("#product-product")
    browser.find_element_by_link_text("Description")
    browser.find_element_by_link_text("Specification")
    browser.find_element_by_link_text("Reviews (0)")