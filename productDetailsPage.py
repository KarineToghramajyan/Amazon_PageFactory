from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from basePage import BasePage

class ProductDetailsPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def go_to_cart(self):
        goToCartButton = self._find_element(By.XPATH, "//*[@data-csa-c-content-id='sw-gtc_CONTENT']")
        self._click(goToCartButton)

    def delete_item(self):
        deleteButton = self._find_element(By.XPATH, "//*[@value='Delete']")
        self._click(deleteButton)



