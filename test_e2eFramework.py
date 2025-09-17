from selenium.webdriver.remote.webdriver import WebDriver  
from pageObjects.login import LoginPage    
import time
import json    
import pytest

# JSON
test_data_path = "../Selenium and Pytest/data/test_e2eFrameworkWithNotes.json"
with open(test_data_path) as f:                                                         
    test_data = json.load(f)
    test_list = test_data["data"]   

#JSON
@pytest.mark.parametrize("test_list_item",test_list)
def test_e2e(browserInstance: WebDriver, test_list_item):  
    
    #conftest.py
    driver = browserInstance    
    
    #login.py
    login_page = LoginPage(driver)  
    
    #shop.py
    shop_page = login_page.login(test_list_item["userEmail"], test_list_item["userPassword"])  
    shop_page.add_product_to_cart(test_list_item["productName"])
    
    #checkout_confirmation.py
    checkout_confirmation = shop_page.go_to_cart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_order()
    

    time.sleep(2)

    # driver.close()