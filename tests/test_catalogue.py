# laptops catalogue test

def test_laptops_catalogue(browser, url):
    browser.get(url + "index.php?route=product/category&path=18")
    browser.find_element_by_id("column-left")
    browser.find_element_by_id("content")
    browser.find_element_by_id("product-category")
    products = browser.find_elements_by_class_name("product-layout")
    assert len(products) == 5