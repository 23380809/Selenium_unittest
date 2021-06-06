import unittest
from selenium import webdriver
import page
import locator
from element import BasePageElement
elements = locator.MainPageLocators()

class PythonOrgSearch(unittest.TestCase):
    #inherit from unittest.testcase first

    # this setUp will run every time we call a unittest
    def setUp(self):
        # a bit like an init method to set up everything
        # a path to chromedriver
        self.driver = webdriver.Chrome("/Users/shawn/Desktop/chrome/chromedriver")
        # python website for testing
        self.driver.get("http://www.python.org")

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        #these assertion says whether our tests fail or pass
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def test_donate_button(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.click_donate_button()

    #I tried a different approach to clicking buttons
    def test_button(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.click_button(elements.LEARN_MORE_BUTTON)




    # this is not gonna work since it starts with not_a_test instead of test
    def not_a_test(self):
        print("this won't print")

    def tearDown(self):
        #like cleaning up after eveything is done and tearDown eveything
        pass
        #self.driver.close()


# run the module run all the unittest we define
if __name__ == "__main__":
    unittest.main()