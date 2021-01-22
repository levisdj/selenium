import time
import unittest
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities


class FirstSampleTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        desired_caps = {
            "browserName": 'chrome'  # Change your browser here
        }
        self.driver = webdriver.Remote(
            command_executor="https://selenium.gitlab-builders.alten-dcx.dev/wd/hub",
            desired_capabilities=desired_caps)
        # self.driver = webdriver.Chrome(options=chrome_options)

# tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()

    # """ You can write the test cases here """
    def test_user_is_able_to_perform_a_simple_google_search(self):
        # try:
        driver = self.driver

        driver.maximize_window()
        # time.sleep(10)

        # Url
        driver.get("https://selenium.gitlab-builders.alten-dcx.dev/grid/console")
        time.sleep(5)
        print("Title is: ", self.driver.title)


        # if (self.driver.find_element_by_xpath("//*[@id='introAgreeButton']/span/span").is_displayed()):
        #     self.driver.find_element_by_xpath("//*[@id='introAgreeButton']/span/span").click()

        self.driver.find_element_by_xpath("//*[@id='right-column']/div[1]/div[1]/ul/li[2]/a").click()

        time.sleep(5)
        print("=====>>>> Configuration opened<<<<<=====")

if __name__ == "__main__":
    unittest.main()
