from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class website():
    def __init__(self, URL, webDriver, browser):
        self.URL = URL
        self.webDriver = webDriver
        self.browser = browser
        self.isChanged = False

    def update(self):
        return

    def getWebDriver(self, URL):
        options = Options()
        options.set_headless(headless=True)
        options.binary = self.browser
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = True
        driver = Firefox(firefox_options=options, capabilities=cap, executable_path=self.webDriver)
        driver.get(URL)
        return driver