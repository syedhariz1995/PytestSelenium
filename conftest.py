
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pytest
import os
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="broswer selection"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    broswer_name = request.config.getoption("browser_name")
    
    if broswer_name == "chrome":
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        })
        driver = webdriver.Chrome(options=chrome_options)
        
    elif broswer_name == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.set_preference("signon.rememberSignons", False)
        driver = webdriver.Firefox(options=firefox_options)
        
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    yield driver
    driver.quit()
    

# this def below is for taking screenshots. Use this template
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