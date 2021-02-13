import time

from selenium.common.exceptions import NoSuchElementException

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


# function for determination an element
def check_element_is(css, browser):
    try:
        browser.find_element_by_css_selector(css)
    except NoSuchElementException:
        return False
    return True


# checking for 'Add to cart' button
def test_check_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    btn = check_element_is('.btn-add-to-basket', browser)
    assert btn, 'Button \'Add to cart\' is undefined'
