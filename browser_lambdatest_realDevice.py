from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import os
import unittest
import sys

username = os.environ.get("LT_USERNAME")
access_key = os.environ.get("LT_ACCESS_KEY")

class FirstRealDeviceBrowserAutomation(unittest.TestCase):

    # setUp runs before each test case
    def setUp(self):
        desired_caps = {
           "platformName":"ios",
           "deviceName":"iPhone X",
           "platformVersion":"14",
           "isRealMobile":"true",
           "tunnel":"false",
           "network":"true",
           "visual":"true"
        }
        self.driver = webdriver.Remote(
           command_executor="http://{}:{}@beta-hub.lambdatest.com:80/wd/hub".format(username, access_key),
           desired_capabilities= desired_caps)


# tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()

    def test_unit_user_should_able_to_add_item(self):
        # try:
        driver = self.driver

        # Url
        driver.get("https://lambdatest.github.io/sample-todo-app/")

        # Click on check box
        check_box_one = driver.find_element_by_name("li1")
        check_box_one.click()

        # Click on check box
        check_box_two = driver.find_element_by_name("li2")
        check_box_two.click()

        # Enter item in textfield
        textfield = driver.find_element_by_id("sampletodotext")
        textfield.send_keys("Yey, Let's add it to list")

        # Click on add button
        add_button = driver.find_element_by_id("addbutton")
        add_button.click()

        # Verified added item
        added_item = driver.find_element_by_xpath("//span[@class='done-false']").text
        print (added_item)

if __name__ == "__main__":
    unittest.main()
