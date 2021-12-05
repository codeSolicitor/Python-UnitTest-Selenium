from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import os
import unittest
import sys

username = os.environ.get("LT_USERNAME")
password = os.environ.get("LT_ACCESS_KEY")

class FirstRealDeviceAppAutomation(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            "platformName":"ios",
            "deviceName":"iPhone X",
            "platformVersion":"14",
            "isRealMobile":"TRUE",
            "network":"TRUE",
            "visual":"TRUE",
            "crashlog":"TRUE",
            "devicelog":"TRUE",
            "video":"TRUE",
            "app":"lt://APP10016241638715538137988"
        }
        self.driver = webdriver.Remote("https://{}:{}@beta-hub.lambdatest.com:80/wd/hub".format(username,password),
            desired_capabilities=desired_caps)

    def tearDown(self):
        self.drive.quit()

    def test_user_should_be_able_add_item(self):
        driver = self.driver

        title = driver.find_elements_by_xpath("//XCUIElementTypeStaticText[@name=\"LambdaTest Sample App\"]")

        driver.find_elements_by_xpath("(//*[@type='XCUIElementTypeSwitch'])[1]")
        driver.find_elements_by_xpath("(//*[@type='XCUIElementTypeSwitch'])[2]")

if __name__ == "__main__":
    unittest.main()
