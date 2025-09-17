

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from utils.browserUtils import BrowserUtils


class CheckoutConfirmation(BrowserUtils):
    def __init__(self,driver):
        super().__init__(BrowserUtils)
        self.driver = driver
        self.checkout_button = (By.CSS_SELECTOR, ".btn-success")
        self.country_input = (By.ID, "country")
        self.country_option = (By.LINK_TEXT, "India")
        self.checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.submit_button = (By.CSS_SELECTOR, '.btn-success')
        self.success_message = (By.CSS_SELECTOR, ".alert-success")
        
    
    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()
    
    
    def enter_delivery_address(self, countryName):
        self.driver.find_element(*self.country_input).send_keys(countryName)
        
        wait = WebDriverWait(self.driver,10)
        wait.until(expected_conditions.presence_of_element_located(self.country_option))
    
        self.driver.find_element(*self.country_option).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit_button).click()
    
    
    def validate_order(self):
        successText = self.driver.find_element(*self.success_message).text
        assert "Success! Thank you!" in successText
    