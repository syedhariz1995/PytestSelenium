# this is Selenium with Pytest's examples
# this file's code is taken from e2eTest.py, put under def test_e2e()
# it is then modified to follow pytest's standards and practice


from selenium.webdriver.remote.webdriver import WebDriver  # use this to get auto-suggest for "driver." 
from pageObjects.login import LoginPage    # <- "from folder.fileName import ClassName"
import time
import json    # <- to use .json file to call data later
import pytest




# all the data that'll be use such as username and password, must be stored in JSON file.
# store the path to a variable
# then use "with open(path variable) as f"
# under it, use "json.load(f)" and assign a variable to it. now the JSON file is Python readable, and can be access inside other def
# store the key in a variable. the key here is "data" from JSON file.
# dictionary for Python/JSON format is like : {"data" : [...]  }    <- "data" is the key, the array "[...]" is the value
test_data_path = "../Selenium and Pytest/data/test_e2eFrameworkWithNotes.json"
with open(test_data_path) as f:                                                         
    test_data = json.load(f)
    test_list = test_data["data"]   # the full values in the list/array, 


# "pytest.mark.parametrize()" expects a list. inside the "()" the syntax is ("variable to store test_list and iterate them", test_list)
# imagine : for test_list_item in test_list
# then, put the "test_list_item" inside the def's () but no quote mark 
# then, on any occasion we need to use the data, the syntax is :  test_list_item["keyName in JSON file under "data" "]  <- in this case test_list_item["userEmail"], etc
# in JSON, if there 3 data sets for each {} under "data"'s array, then the test will run 3 times with each different data.
@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item",test_list)
def test_e2e(browserInstance: WebDriver, test_list_item):  # <- this will check fixture in conftest.py. "driver" will now be used. use WebDriver to get auto-suggest for "driver."
    driver = browserInstance    # <- no more driver blueprint. All in conftest.py being injected here.
    
    login_page = LoginPage(driver)  # <- use the class from login.py, under pageObjects folder. Pass "driver" to the class LoginPage.
    
    print(login_page.getTitle())       # <- get the page title via LoginPage's parent class
    
    shop_page = login_page.login(test_list_item["userEmail"], test_list_item["userPassword"])  # <- call this method within the LoginPage() class (eventually will open up shop page)
    shop_page.add_product_to_cart(test_list_item["productName"])
    print(login_page.getTitle())
    
    checkout_confirmation = shop_page.go_to_cart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_order()
    

    time.sleep(2)

    # driver.close()
    
    
    
# run all in one line
# also execute shell in Jenkins 
# cd '.\Selenium and Pytest\' pytest -n 2 -m smoke --browser_name firefox --html=reports/report.html