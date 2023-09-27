import yaml
from module import Site
import time

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


# site = Site(testdata["address"])

def test_step2(site, selectors_login, selectors_pass, selectors_btn_submit, selectors_err_banner):
    # Вход с невалидными данными
    input1 = site.find_element("xpath", selectors_login)
    input1.send_keys("test")
    input2 = site.find_element("xpath", selectors_pass)
    input2.send_keys("test")
    btn = site.find_element("css", selectors_btn_submit)
    btn.click()
    err_label = site.find_element("xpath", selectors_err_banner)
    assert err_label.text == "401"


def test_step3(site, selectors_login, selectors_pass, selectors_btn_submit, selectors_err_banner, selectors_blog):
    # Вход в систему
    input1 = site.find_element("xpath", selectors_login)
    input1.clear()
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", selectors_pass)
    input2.clear()
    input2.send_keys(testdata["password"])
    btn = site.find_element("css", selectors_btn_submit)
    btn.click()
    blog = site.find_element("xpath", selectors_blog)
    assert blog.text == "Blog"


def test_step4(site, selectors_login, selectors_pass, selectors_btn_submit, selectors_create_post_btn,
               selectors_new_post_title, selectors_new_post_description, selectors_new_post_content,
               selectors_new_post_save_btn, selectors_created_post_title):
    # Создание поста
    login_input = site.find_element("xpath", selectors_login)
    login_input.clear()
    login_input.send_keys(testdata["login"])
    pass_input = site.find_element("xpath", selectors_pass)
    pass_input.clear()
    pass_input.send_keys(testdata["password"])
    login_btn = site.find_element("css", selectors_btn_submit)
    login_btn.click()

    btn_create_post = site.find_element("css", selectors_create_post_btn)
    btn_create_post.click()

    title_post_input = site.find_element("xpath", selectors_new_post_title)
    title_post_input.send_keys(testdata["post_title"])
    description_post_input = site.find_element("xpath", selectors_new_post_description)
    description_post_input.send_keys(testdata["post_description"])
    content_post_input = site.find_element("xpath", selectors_new_post_content)
    content_post_input.send_keys(testdata["post_content"])
    time.sleep(2)

    save_post_btn = site.find_element("xpath", selectors_new_post_save_btn)
    save_post_btn.click()
    time.sleep(2)

    title_post = site.find_element("xpath", selectors_created_post_title)
    assert title_post.text == testdata["post_title"]