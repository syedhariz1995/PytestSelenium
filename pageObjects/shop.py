
from selenium.webdriver.common.by import By
from pageObjects.checkout_confirmation import CheckoutConfirmation
from utils.browserUtils import BrowserUtils

class ShopPage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link = (By.XPATH, "//a[@href='/angularpractice/shop']")
        self.product_cards = (By.XPATH, "//app-card")
        self.checkout_button = (By.CSS_SELECTOR, ".btn-primary")
        
    def add_product_to_cart(self, product_name):
        
        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.product_cards)
        
        for product in products:
            productName = product.find_element(By.XPATH, "div/div/h4/a").text
            if productName == product_name:
                product.find_element(By.XPATH, "div/div/button").click()
                
    def go_to_cart(self):
        self.driver.find_element(*self.checkout_button).click()
        checkout_confirmation = CheckoutConfirmation(self.driver)
        return checkout_confirmation