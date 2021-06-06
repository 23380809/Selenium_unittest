# any css selector any id we locate for the elements should all be gathered

from selenium.webdriver.common.by import By


class MainPageLocators(object):
    GO_BUTTON = (By.ID, "submit")
    # python website has a Go Button and it's id is summit
    DONATE_BUTTON = (By.CLASS_NAME, "donate-button")
    LEARN_MORE_BUTTON = (By.CLASS_NAME, "readmore")



class SearchResultsPageLocators(object):
    pass
