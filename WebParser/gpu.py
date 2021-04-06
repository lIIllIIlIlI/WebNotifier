# imports ---------------------
import logging
import re
from time import sleep
from WebParser.website import website
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


# Globals ---------------------
logger = logging.getLogger(__name__)


# Public ---------------------
class gpu(website):
    def __init__(self, webDriver, browser):
        super().__init__(self, webDriver, browser)
        self.changedWebsites = []
        self.oldRxPageContent = ""
        self.old3070PageContent = ""
        self.old3080PageContent = ""
        self.old3090PageContent = ""

    def update(self):
        """
        """
        self.changedWebsites = []
        xpath = '/html/body/div[2]/div[4]/div[1]/div[2]/div[2]/div/div[1]/div[4]/div'
        RX_WEBSITE = 'https://www.hardwareluxx.de/community/threads/rx-gpu-verf%C3%BCgbarkeitshinweise.1282621/page-1000'
        RTX3070_WEBSITE = 'https://www.hardwareluxx.de/community/threads/rtx-3070-gpu-verf%C3%BCgbarkeitshinweise.1284024/page-1000'
        RTX3080_WEBSITE = 'https://www.hardwareluxx.de/community/threads/rtx-3080-gpu-verf%C3%BCgbarkeitshinweise.1281755/page-1000'
        RTX3090_WEBSITE = 'https://www.hardwareluxx.de/community/threads/rtx-3090-gpu-verf%C3%BCgbarkeitshinweise.1283956/page-1000'

        # check for new RX cards
        driverRX = self.getWebDriver(RX_WEBSITE)
        driverRX.implicitly_wait(10)
        sleep(3)
        rxPageContent = driverRX.find_element_by_xpath(xpath).text
        if rxPageContent != self.oldRxPageContent:
          if self.oldRxPageContent:
            self.changedWebsites.append(RX_WEBSITE)
          self.oldRxPageContent = rxPageContent
        else:
          logger.info("No new RX cards found")
        driverRX.quit()

        # check for new 3070 cards
        driver3070 = self.getWebDriver(RTX3070_WEBSITE)
        driver3070.implicitly_wait(10)
        sleep(3)
        rtx3070PageContent = driver3070.find_element_by_xpath(xpath).text
        if rtx3070PageContent != self.old3070PageContent:
          if self.old3070PageContent:
            self.changedWebsites.append(RTX3070_WEBSITE)
          self.old3070PageContent = rtx3070PageContent
        else:
          logger.info("No new 3070 cards found")
        driver3070.quit()

        # check for new 3080 cards
        driver3080 = self.getWebDriver(RTX3080_WEBSITE)
        driver3080.implicitly_wait(10)
        sleep(3)
        rtx3080PageContent = driver3080.find_element_by_xpath(xpath).text
        if rtx3080PageContent != self.old3080PageContent:
          if self.old3080PageContent:
            self.changedWebsites.append(RTX3080_WEBSITE)
          self.old3080PageContent = rtx3080PageContent
        else:
          logger.info("No new 3080 cards found")
        driver3080.quit()

        # check for new 3070 cards
        driver3090 = self.getWebDriver(RTX3090_WEBSITE)
        driver3090.implicitly_wait(10)
        sleep(3)
        rtx3090PageContent = driver3090.find_element_by_xpath(xpath).text
        if rtx3090PageContent != self.old3090PageContent:
          if self.old3090PageContent:
            self.changedWebsites.append(RTX3090_WEBSITE)
          self.old3090PageContent = rtx3090PageContent
        else:
          logger.info("No new 3090 cards found")
        driver3090.quit()
