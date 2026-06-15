import re

from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MySeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(MySeleniumTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, reverse('accounts:signin')))
        signin_input = self.selenium.find_element(By.ID, 'formsignin')
        username_input = signin_input.find_element(By.NAME, "username")
        username_input.send_keys('myuser')
        password_input = signin_input.find_element(By.NAME, "password")
        password_input.send_keys('secret')

        signin_input.find_element(By.ID, 'next').click()

        # noSuchUser.text returned an empty string, so we pull the textContent attribute instead, for now anyway.
        noSuchUser = signin_input.find_element(By.CLASS_NAME, "no-such-user").get_attribute("textContent")

        self.assertEqual(noSuchUser, 'User does not exist.')

    def test_register_missing_username(self):
        self.selenium.get('%s%s' % (self.live_server_url, reverse('accounts:signin')))
        register_form = self.selenium.find_element(By.ID, 'formregister')

        self.selenium.find_element(By.XPATH, '//input[@value="CREATE ACCOUNT"]').click()

        noSuchUser = self.selenium.find_element(By.CLASS_NAME, "no-such-user")
        with self.assertRaises(NoSuchElementException):
            noSuchUser.find_element(By.CLASS_NAME, "template")
        self.assertEqual(register_form.find_element(By.CLASS_NAME, 'missing-username').text, 'Missing user name!')

    def test_register_missing_email(self):
        self.selenium.get('%s%s' % (self.live_server_url, reverse('accounts:signin')))
        register_form = self.selenium.find_element(By.ID, 'formregister')
        username_input = register_form.find_element(By.NAME, "username")
        username_input.send_keys('myuser')

        self.selenium.find_element(By.XPATH, '//input[@value="CREATE ACCOUNT"]').click()

        noSuchUser = self.selenium.find_element(By.CLASS_NAME, "missing-email")

        with self.assertRaises(NoSuchElementException):
            noSuchUser.find_element(By.CLASS_NAME, "template")
        self.assertEqual(register_form.find_element(By.CLASS_NAME, 'missing-email').text, 'Missing email address!')

    def test_register_missing_password(self):
        self.selenium.get('%s%s' % (self.live_server_url, reverse('accounts:signin')))
        register_form = self.selenium.find_element(By.ID, 'formregister')
        username_input = register_form.find_element(By.NAME, "username")
        username_input.send_keys('myuser')
        email_input = register_form.find_element(By.NAME, "email")
        email_input.send_keys('email@email.com')

        self.selenium.find_element(By.XPATH, '//input[@value="CREATE ACCOUNT"]').click()

        missingPassword = self.selenium.find_element(By.CLASS_NAME, "missing-password")
        with self.assertRaises(NoSuchElementException):
            missingPassword.find_element(By.CLASS_NAME, "template")
        self.assertEqual(register_form.find_element(By.CLASS_NAME, 'missing-password').text, 'Missing password!')

    def test_register_missing_fullname(self):
        self.selenium.get('%s%s' % (self.live_server_url, reverse('accounts:signin')))
        register_form = self.selenium.find_element(By.ID, 'formregister')
        username_input = register_form.find_element(By.NAME, "username")
        username_input.send_keys('myuser')
        email_input = register_form.find_element(By.NAME, "email")
        email_input.send_keys('email@email.com')
        password_input = register_form.find_element(By.NAME, "password")
        password_input.send_keys('secret')

        self.selenium.find_element(By.XPATH, '//input[@value="CREATE ACCOUNT"]').click()

        missingFullname = self.selenium.find_element(By.CLASS_NAME, "missing-fullname")
        with self.assertRaises(NoSuchElementException):
            missingFullname.find_element(By.CLASS_NAME, "template")
        self.assertEqual(register_form.find_element(By.CLASS_NAME, 'missing-fullname').text, 'Please provide your real name.')

    def test_register_short_password(self):
        self.selenium.get('%s%s' % (self.live_server_url, reverse('accounts:signin')))
        register_form = self.selenium.find_element(By.ID, 'formregister')
        username_input = register_form.find_element(By.NAME, "username")
        username_input.send_keys('myuser')
        email_input = register_form.find_element(By.NAME, "email")
        email_input.send_keys('email@email.com')
        password_input = register_form.find_element(By.NAME, "password")
        password_input.send_keys('123')
        fname_input = register_form.find_element(By.NAME, "fullname")
        fname_input.send_keys('Full Name')

        self.selenium.find_element(By.XPATH, '//input[@value="CREATE ACCOUNT"]').click()

        invalidPassword = self.selenium.find_element(By.CLASS_NAME, "invalid-password")
        with self.assertRaises(NoSuchElementException):
            invalidPassword.find_element(By.CLASS_NAME, "template")
        self.assertEqual(invalidPassword.text, 'Password must be 6 characters or more!')
