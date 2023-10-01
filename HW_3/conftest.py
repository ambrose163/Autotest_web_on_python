import pytest
import yaml
from module import Site

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

@pytest.fixture()
def selectors_login():
    return """//*[@id="login"]/div[1]/label/input"""

@pytest.fixture()
def selectors_pass():
    return """//*[@id="login"]/div[2]/label/input"""

@pytest.fixture()
def selectors_btn_submit():
    return "button"

@pytest.fixture()
def selectors_err_banner():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""

@pytest.fixture()
def selectors_blog():
    return """//*[@id="app"]/main/div/div[1]/h1"""

@pytest.fixture()
def selectors_create_post_btn():
    return "#create-btn"

@pytest.fixture()
def selectors_new_post_title():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""

@pytest.fixture()
def selectors_new_post_description():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""

@pytest.fixture()
def selectors_new_post_content():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""

@pytest.fixture()
def selectors_new_post_save_btn():
    return """//*[@id="create-item"]/div/div/div[7]/div/button"""

@pytest.fixture()
def selectors_created_post_title():
    return """//*[@id="app"]/main/div/div[1]/h1"""

@pytest.fixture()
def site():
    site_instance = Site(testdata["address"])
    yield site_instance
    site_instance.driver.quit()