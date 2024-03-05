import pytest
from selenium.webdriver.common.by import By
import time

class TestDisplayBtn():
    def test_display_btn(self, browser):
        browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        time.sleep(15)
        btn_basket = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
        assert btn_basket

