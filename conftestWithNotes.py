
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os
import pytest
driver = None


# to use custom command line name (option name such as "--broswer_name"), must register under this code below
# can be found in https://docs.pytest.org/en/stable/example/simple.html
# the default="chrome" means if all else failed, by default, the value of --browser_name will be "chrome", thus, will open chrome.
# MUST have this code below
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="broswer selection"
    )

# get multiple browsers to open up with "if" statement
# to invoke a specific broswer with name, under terminal to run test, add on option called --browser_name followed by name of browser
# e.g. :  pytest test_e2eFramework.py --browser_name firefox
# Important : --browser_name is a custom option name to be used in terminal, but can be invoked via "request.config.getoption("browser_name")"
# When we run "pytest test_e2eFramework.py --browser_name firefox" in terminal , it will go through this conftest.py and see if its firefox, or whatever we put it

@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browser_name = request.config.getoption("browser_name")    #<- no need --browser_name in getoption. remove the -- . 
    
    if browser_name == "chrome":
        chrome_options = Options()                                  # <- chrome options to disable things in chrome
        chrome_options.add_experimental_option("prefs", {           # <- use ".add_experimental_option("prefs, {}")"  
            "credentials_enable_service": False,                    # <- Turn off the "Save your password?" prompt    
            "profile.password_manager_enabled": False,              # <- Disables password manager completely
            "profile.password_manager_leak_detection": False        # <- Disables "change your password" leak detection bubble completely
        })
        driver = webdriver.Chrome(options=chrome_options)           # <- Apply the (options=chrome_options) to chrome
        
    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()                                                    # <- Firefox options
        firefox_profile = webdriver.FirefoxProfile()                                          # <- Create Firefox profile to store custom preferences
        firefox_profile.set_preference("signon.rememberSignons", False)                       # <- Disable "Remember password" prompt
        firefox_profile.set_preference("extensions.formautofill.creditCards.enabled", False)  # <- Disable the "save credit card" feature (in case it pops up)
        firefox_profile.set_preference("extensions.formautofill.addresses.enabled", False)    # <- Disable the "save addresses" feature

        driver = webdriver.Firefox(firefox_profile=firefox_profile, options=firefox_options)  # <- Apply profile to driver
        
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    yield driver
    driver.quit()
    
    
    
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    
    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        
        if (report.skipped and xfail) or (report.failed and not  xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
            if not os.path.exists(reports_dir):
                os.makedirs(reports_dir)
                
            file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")
            print("file name is " + file_name)
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)
    
    
    
    
    
    
    
    
# all pip installs needed : 
# python -m venv venv         <- in a new environment, run this first -- to run pip install
# pip install selenium  
# pip install pytest
# pip install pytest-xdist   <- to run tests simultaneously
# pip install pytest-asyncio  <- removes warnings with custom mark (need to use ".ini" file)
# pip install pytest-html

# to get html reports use this syntax :
# pytest --html folderName/htmlFile.html