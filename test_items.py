import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_item_has_add_to_cart_button(browser):
    browser.get(link)
    button = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert button, "Should be a button"

