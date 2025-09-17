from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

def test_sort(browserInstance: WebDriver):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    driver.implicitly_wait(2)


    driver.find_element(By.XPATH, "//span[text() = 'Veg/fruit name']").click()

    browserListAfterClick = []
    veggies = driver.find_elements(By.XPATH, "//tr/td[1]")
    for veg in veggies:
        browserListAfterClick.append(veg.text)

    sortedByPython = browserListAfterClick.copy()

    sortedByPython.sort()

    assert browserListAfterClick == sortedByPython