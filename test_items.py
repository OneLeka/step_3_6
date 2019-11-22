import time
from selenium.common.exceptions import NoSuchElementException

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_basket(browser):
    browser.get(link)
    time.sleep(5)
    try:
        browser.find_element_by_css_selector('button.btn-add-to-basket')
    except NoSuchElementException:
        assert False, 'No button "Add to basket" on this page'
