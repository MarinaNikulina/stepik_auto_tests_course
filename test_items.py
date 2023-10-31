import time
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_is_there_btn_add_to_basket(browser):
    browser.get(link)
    button_submit = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert (button_submit), "It is not Correct! There is not this button."
    