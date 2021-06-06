
from locator import *

from element import BasePageElement


class SearchTextElement(BasePageElement):
    # set locator to q
    locator = "q"


class GoButtonElement(BasePageElement):
    locator = "go"


#object is optional
class BasePage(object):
    def __init__(self, driver):
    #base class for all out pages, any other pages will inherit this page
        self.driver = driver


class MainPage(BasePage):
    # this class will navigate us to the MainPage by assert the title is right and find the button element then click it
    search_text_element = SearchTextElement()
    # searching the id of locator being q
    # this method is gonna tell us if the title of the web page matches what we want to match
    def is_title_matches(self):
        return "Python" in self.driver.title  # tell us script python is in the driver.title
        ## example of using would be  mainPage = page.MainPage() assert mainPage.is_title_matches()

    def click_go_button(self):
        # this is gonna find the element of GO_BUTTON which has the id (summit) and then click it
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()
        # to click

    def click_donate_button(self):
        element = self.driver.find_element(*MainPageLocators.DONATE_BUTTON)
        element.click()

    def click_button(self, button):
        element = self.driver.find_element(*button)
        element.click()

class SearchResultPage(BasePage):
    # another page
    def is_results_found(self):
        # if any results are found
        return "No results found." not in self.driver.page_source
