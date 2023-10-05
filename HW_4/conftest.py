import logging
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import requests

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]

sess = requests.Session()

@pytest.fixture(scope="session")
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture()
def login_api():
    try:
        response = sess.post(testdata["url_login"],
                             data={'username': testdata["login"], 'password': testdata["password"]})
        token = response.json()['token']
    except:
        logging.exception("Get token exeption")
        token = None
    logging.debug("Token return success")
    return token

