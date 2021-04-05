# imports ---------------------
import logging
import re
from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


# Globals ---------------------
logger = logging.getLogger(__name__)


# Public ---------------------
class website():
    def __init__(self, URL, webDriver, browser):
        self.URL = URL
        self.webDriver = webDriver
        self.browser = browser
        self.isChanged = False

    def update(self):
        """

        Notes:
        - Solution might be unstable. If black is no longer available, the algorithm
        might assume that white is. This is due to logitechs strange web app which
        automatically switches the selected color.
        - Currently, no error handling available. If logitech website breaks, the whole
          script crashes
        - WebDriverWait doesnt seem to do a thing
        - implicit wait is a cleaner solution than sleep, but tutorials only show how
          to wait for an element with given id. Solution could be something like
          "WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,
          '//*[@id="onetrust-accept-btn-handler"]')))" but it doesnt seem to work
          out.
        """
        driver = self.getWebDriver()
        # waits until website is available, max 10 seconds
        driver.implicitly_wait(10)
        # -------- Accept all cookies
        # cookies might bob up after the page is fully loaded already
        sleep(5)
        driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()
        # -------- select switches and keyboard layout
        # find_element_by_class_name returns only the first element of find_elements_by_class_name
        # unfortunately, all dropdown menus share the same class name.
        # sleep(5)
        clickSelection = driver.find_elements_by_class_name("js-product-model-selector")
        languageSelection = clickSelection[0]
        languageDropdownMenu = Select(languageSelection)
        languageDropdownMenu.select_by_value("deutsch(qwertz)")
        switchSelection = clickSelection[1]
        switchDropdownMenu = Select(switchSelection)
        switchDropdownMenu.select_by_value("clicky")
        sleep(5)
        # -------- Check availability
        # The white button has a disabled attribute. Unfortunately, i failed to extract it.
        # Furthermore, clicking the disabled button doesnt throw an error because logitech redirects it
        # Furthermore, selecting a layout/switch combination that is not available in the current color
        # changes the color automatically.
        picture = driver.find_element_by_xpath('/html/body/div[1]/div/main/div[1]/div/div[12]/section/div/div/div[1]/div[17]/div[1]/div/ul/div/div/li[1]/div')
        colorsWhite = driver.find_element_by_xpath('/html/body/div[1]/div/main/div[1]/div/div[12]/section/div/div/div[2]/div/div[4]/div[1]/ul/li[2]/button').is_enabled()
        colorBlack = driver.find_element_by_xpath('/html/body/div[1]/div/main/div[1]/div/div[12]/section/div/div/div[2]/div/div[4]/div[1]/ul/li[1]/button').is_enabled()
        outerHtml = driver.find_element_by_xpath('/html/body/div[1]/div/main/div[1]/div/div[12]/section/div/div/div[1]/div[12]/div[1]/div/ul/div/div/li[1]/div/img').get_attribute('outerHTML')
        if re.search(r'tkl-carbon-gallery' ,outerHtml):
            self.isChanged = False
        else:
            self.isChanged = True
        # There are other options like .dispense() or .close(). Yet quit() is the only one that
        # closes all tabs and frees memory.
        driver.quit()

    def getWebDriver(self):
        options = Options()
        # options.set_headless(headless=True)
        options.binary = self.browser
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = True
        driver = Firefox(firefox_options=options, capabilities=cap, executable_path=self.webDriver)
        driver.get(self.URL)
        return driver