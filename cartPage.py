from selenium import webdriver
from selenium.webdriver.common.by import By
from basePage import BasePage

class CartPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def add_to_cart(self):
        addToCartButton = self._find_element(By.ID, "add-to-cart-button")
        self._click(addToCartButton)

    def check_if_cart_is_empty(self):
        emptyCart = self._find_element(By.XPATH, "//h1[normalize-space()='Your Amazon Cart is empty.']")
        if self._get_text(emptyCart) == "Your Amazon Cart is empty.":
            print("Your Amazon Cart is empty.")
            self.driver.close()
        else:
            exit(3)








