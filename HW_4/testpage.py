from BaseApp import BasePage
from selenium.webdriver.common.by import By
import yaml
import logging
import requests


class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exeption while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exeption with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Eception while get test from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

    # ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="Login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="Password form")

    def enter_title(self, post_title):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_NEW_POST_TITLE"], post_title,
                                   description="Enter Post Title")

    def enter_description(self, post_description):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_NEW_POST_DESCRIPTION"], post_description,
                                   description="Enter Post Descriptionn")

    def enter_content(self, post_content):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_NEW_POST_CONTENT"], post_content,
                                   description="Enter Post Content")

    def enter_name_contact(self, contact_name):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACTUS_NAME_FIELD"], contact_name,
                                   description="Enter Contact Name")

    def enter_email_contact(self, contact_email):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACTUS_EMAIL_FIELD"], contact_email,
                                   description="Enter Contact Email")

    def enter_content_contact(self, contact_content):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACTUS_CONTENT_FIELD"], contact_content,
                                   description="Enter Contact Content")

    def download_image(self):
        download_img = self.find_element(TestSearchLocators.ids["LOCATOR_DOWNLOAD_IMAGE"])
        download_img.send_keys(r"C:\Users\Дмитрий\Desktop\2023-04-30_22-31-39.png")

    # CLICK
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="Click login button")

    def click_create_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_POST_BTN"], description="Click create post (+) button")

    def click_save_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_NEW_POST_SAVE_BTN"], description='Click "SAVE" button')

    def click_contact_link(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_LINK"], description='Click "contact" link')

    def click_contactus_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACTUS_BTN"], description='Click "CONTACT US" button')

    # GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_BANNER"], description="error")

    def get_blog_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_BLOG"], description="blog")

    def get_post_title(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_CREATED_POST_TITLE"],
                                          description="post title")

    def get_allert_text(self):
        alert_text = self.switch_to_alert().text
        logging.info(f'We find text {alert_text} in title alert on site "Contact Us"')
        return alert_text

    # GET PROPERTY
    def get_email_label_color(self):
        email_label_color = self.get_element_property(TestSearchLocators.ids["LOCATOR_CONTACTUS_LABEL_EMAIL"], "color")
        logging.info(f'We find err color label {email_label_color} when entered not valid email')
        return email_label_color

    #API
    def get_post_data(self, token):
        with open("./testdata.yaml") as f:
            testdata = yaml.safe_load(f)
        resource = requests.get(testdata["url_posts"], headers={"X-Auth-Token": token})
        logging.debug(f'We get posts data')
        return resource.json()