from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):
# represent one element in the page  ex: it will represent a search bar or a text field
    def __set__(self, obj, value):
        # we want to set some value, this following process will do
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            #wait until lambda function is true, until we find the locator
            lambda driver: driver.find_element_by_name(self.locator))

        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        # get the value of the object
        #everytime we try to access a new element we use this def
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            # wait the element to exist on the page
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        # get the attribute from html
        return element.get_attribute("value")

