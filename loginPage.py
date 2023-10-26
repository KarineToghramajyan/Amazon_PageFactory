from selenium import webdriver
from selenium.webdriver.common.by import By
from basePage import BasePage

class LoginPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_signin_field(self):
        signInField = self._find_element(By.XPATH, "//a[@id ='nav-link-accountList']")
        self._click(signInField)

    def fill_username_field(self, username):
        userNameFieldElement = self._find_element(By.ID, "ap_email")
        self._fill_element(userNameFieldElement, username)

    def click_continue_button(self):
        continueButtonElement = self._find_element(By.ID, "continue")
        self._click(continueButtonElement)

    def fill_password_field(self, password):
        passwordFieldElement = self._find_element(By.ID, "ap_password")
        self._fill_element(passwordFieldElement, password)

    def click_signin_button(self):
        signInButtonElement = self._find_element(By.ID, "signInSubmit")
        self._click(signInButtonElement)

