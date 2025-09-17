# page Object Models (POM)
# put all locators of a page in a class
# can use all locators in a page here.
# for example : this file is the login page of "https://rahulshettyacademy.com/loginpagePractise/"
# all locators can be stored here, to be used for many test cases relating to this page
# this file is to be practice with test_e2eFramework.py

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pageObjects.shop import ShopPage
from utils.browserUtils import BrowserUtils

class LoginPage(BrowserUtils):                             # BroswerUtils is the parent class. To be used to get Title (or anything common for all classes to get)
    #the locators
    def __init__(self, driver):                             # <- driver passed from test_e2eFramework.py
        super().__init__(driver)                            # <- driver passed to parent class BrowserUtils , to get Title of page in this case
        self.driver = driver                                # <- "self.driver" is now the driver from e2eFramework.py, which comes from the conftest.py
        self.username_input = (By.ID, "username")           # <- "self" can be used in the whole class. and use a tuple (By.ID, "username") and assign it a variabe with "self"
        self.password = (By.NAME, "password")
        self.signIn_button = (By.ID, "signInBtn")
    
    
    # the actions method
    # use "self" to use the __init__ locators
    # use the (*) to "unpack" the tuple from __init__, making it 2 argument -> e.g. By.ID , "username"
    # if no (*), then it'll be the whole tuple itself as an argument, considered as one. -> e.g. (By.ID , "username")
    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)       # <- use "self.variable" from __init__
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.signIn_button).click()
        shop_page = ShopPage(self.driver)
        return shop_page