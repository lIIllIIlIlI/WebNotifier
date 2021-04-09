import logging
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Globals ---------------------
logger = logging.getLogger(__name__)


class website():
    def __init__(self, URL, webDriver, browser):
        self.URL = URL
        self.webDriver = webDriver
        self.browser = browser
        self.isChanged = False

    def update(self):
        return

    def getWebDriver(self, URL):
        driver = None
        options = Options()
        options.set_headless(headless=True)
        options.binary = self.browser
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = True
        try:
            driver = Firefox(firefox_options=options, capabilities=cap, executable_path=self.webDriver)
            driver.get(URL)
        except:
            logger.error("Failed to generate driver to parse {}, driver: {}".format(URL, driver))
        return driver