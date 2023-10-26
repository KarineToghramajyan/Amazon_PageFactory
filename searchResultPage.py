from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from basePage import BasePage

class SearchResults(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_first_result(self):
        firstResult = self._find_element(By.XPATH, "//*[@data-image-index='1']")
        self._click(firstResult)
