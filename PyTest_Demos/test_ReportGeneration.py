from selenium import webdriver
import pytest

class TestOrangeHRM():
    global driver

    @pytest.fixture()
    def setup(self):

        self.driver.webdriver.Chrome(executable_path="C:\\Users\\acer\\OneDrive\\Desktop\\chorme\\chromedriver")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homepageTitle(self,setup):

        assert self.driver.title=="OrangeHRM"

    def test_Login(self,setup):

        self.driver.find_element_by_id("txtUsername").send_key("Admin")
        self.driver.find_element_by_id("txtPassword").send_key("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        assert self.driver.title=="OrangeHRM"






