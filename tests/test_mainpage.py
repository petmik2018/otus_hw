# main page test

def test_mp(browser, url):
    browser.get(url)
    browser.find_element_by_id("top")
    browser.find_element_by_id("top-links")
    browser.find_element_by_tag_name("header")
    browser.find_element_by_id("common-home")
    browser.find_element_by_tag_name("footer")