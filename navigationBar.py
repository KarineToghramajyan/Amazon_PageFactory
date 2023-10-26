from selenium import webdriver
from selenium.webdriver.common.by import By
from basePage import BasePage

class NavigationBar(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def fill_search_box(self, product):
        searchFieldElement = self._find_element(By.ID, "twotabsearchtextbox")
        self._click(searchFieldElement)
        self._fill_element(searchFieldElement, product)

    def click_search_icon(self):
        searchIconElement = self._find_element(By. ID, "nav-search-submit-button")
        self._click(searchIconElement)

    def click_cart_button(self):
        cartButtonElement = self._find_element(By.ID, "nav-cart-count")
        self._click(cartButtonElement)

