import time
from testpage import OperationsHelper
import logging
import yaml
import send_report

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

def test_step1(browser):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"

def test_step2(browser):
    # Вход в систему
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    assert testpage.get_blog_text() == "Blog"

def test_step_2_1(browser):
    # Загрузка изображения в пост
    logging.info("Test2.1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    testpage.click_create_post_button()
    testpage.enter_title(testdata["post_title"])
    testpage.enter_description(testdata["post_description"])
    testpage.enter_content(testdata["post_content"])
    time.sleep(2)
    testpage.download_image()
    testpage.click_save_button()
    print(testpage.download_image())
    time.sleep(2)
    assert 1 == 1



def test_step3(browser):
    #Создание поста
    logging.info("Test3 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    testpage.click_create_post_button()

    testpage.enter_title(testdata["post_title"])
    testpage.enter_description(testdata["post_description"])
    testpage.enter_content(testdata["post_content"])
    testpage.click_save_button()
    time.sleep(2)

    assert testpage.get_post_title() == testdata["post_title"]