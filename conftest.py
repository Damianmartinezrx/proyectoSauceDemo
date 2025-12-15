from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pages.loginPage import login_page as login
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import pathlib
target = pathlib.Path("reports/screenshots")
target.mkdir(parents=True, exist_ok=True)

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")
    #Comentar estas lineas para ver el proceso de los test
    options.add_argument("--no-sandbox") # github
    options.add_argument("--disable-gpu") # github
    options.add_argument("--window-size=1920,1080") # github
    options.add_argument("--headless=new") # github

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    login(driver).abrir_pagina()
    return driver

@pytest.fixture
def url_base():
    return "https://reqres.in/api/users"

@pytest.fixture
def header_request():
    return {"x-api-key": "reqres-free-v1"}

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    
    report = outcome.get_result()

    if report.when in ("setup", "call") and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            timestamp_comun = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            timestamp_unix = int(time.time())
            file_name = target / f"{report.when}_{item.name}_{timestamp_comun}.png"
            driver.save_screenshot(str(file_name))

