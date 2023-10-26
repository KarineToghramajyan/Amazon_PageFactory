from time import sleep
from selenium import webdriver
from loginPage import LoginPage
from navigationBar import NavigationBar
from searchResultPage import SearchResults
from cartPage import CartPage
from productDetailsPage import ProductDetailsPage

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

loginPageObject = LoginPage(driver)
if loginPageObject._get_title() != "Amazon Sign-In":
    print("ERROR: Invalid page")
    exit(2)
loginPageObject.fill_username_field("testamazon117@gmail.com")
loginPageObject.click_continue_button()
loginPageObject.fill_password_field("molotok123")
sleep(7)
loginPageObject.click_signin_button()
navigationBarObject = NavigationBar(driver)
navigationBarObject.fill_search_box("iphone charger")
navigationBarObject.click_search_icon()
sleep(2)
searchResultsPageObject = SearchResults(driver)
searchResultsPageObject.click_first_result()
sleep(2)
cartPageObject = CartPage(driver)
cartPageObject.add_to_cart()
productDetailsPageObj = ProductDetailsPage(driver)
productDetailsPageObj.go_to_cart()
sleep(2)
productDetailsPageObj.delete_item()
sleep(5)
cartPageObject.check_if_cart_is_empty()
sleep(2)




