import logging
import requests
import yaml
from testpage import OperationsHelper
from send_report import send_email

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

sess = requests.Session()

def test_create_post(login_api):
    logging.info("Test create post starting")
    response = sess.post(testdata["url_posts"],
                   headers={"X-Auth-Token": login_api},
                   params={"title": testdata["title_post_api"],
                           "description": testdata["description_post_api"],
                           "content": testdata["content_post_api"]})
    assert str(response) == "<Response [200]>"


def test_check_post(login_api):
    logging.info("Test check post starting")
    testpage = OperationsHelper(login_api)
    posts = testpage.get_post_data(login_api)
    lst = posts["data"]
    posts_descriptions = [el["description"] for el in lst]
    send_email()
    assert testdata["description_post_api"] in posts_descriptions