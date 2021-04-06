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
        self.newGpuPosts = {}
        self.oldRxPostCount = ""
        self.old3070PostCount = ""
        self.old3080PostCount = ""
        self.old3090PostCount = ""

    def update(self):
        """
        """
        self.newGpuPosts = {}
        xpath = '/html/body/div[2]/div[4]/div[1]/div[2]/div[2]/div/div[1]/div[4]/div'
        className = 'bbWrapper'
        RX_WEBSITE = 'https://www.hardwareluxx.de/community/threads/rx-gpu-verf%C3%BCgbarkeitshinweise.1282621/page-1000'
        RTX3070_WEBSITE = 'https://www.hardwareluxx.de/community/threads/rtx-3070-gpu-verf%C3%BCgbarkeitshinweise.1284024/page-1000'
        RTX3080_WEBSITE = 'https://www.hardwareluxx.de/community/threads/rtx-3080-gpu-verf%C3%BCgbarkeitshinweise.1281755/page-1000'
        RTX3090_WEBSITE = 'https://www.hardwareluxx.de/community/threads/rtx-3090-gpu-verf%C3%BCgbarkeitshinweise.1283956/page-1000'

        # check for new RX cards
        driverRX = self.getWebDriver(RX_WEBSITE)
        driverRX.implicitly_wait(10)
        sleep(3)
        rxPosts = driverRX.find_elements_by_class_name('bbWrapper')
        rxPostCount = len(rxPosts)
        if rxPostCount != self.oldRxPostCount:
          if self.oldRxPostCount:
            self.newGpuPosts["Radeon"] = rxPosts[-1].text
          self.oldRxPostCount = rxPostCount
        else:
          logger.info("No new RX cards found")
        driverRX.quit()

        # check for new 3070 cards
        driver3070 = self.getWebDriver(RTX3070_WEBSITE)
        driver3070.implicitly_wait(10)
        sleep(3)
        rtx3070Posts = driver3070.find_elements_by_class_name('bbWrapper')
        rtx3070PostCount = len(rtx3070Posts)
        if rtx3070PostCount != self.old3070PostCount:
          if self.old3070PostCount:
            self.newGpuPosts["RTX3070"] = rtx3070Posts[-1].text
          self.old3070PostCount = rtx3070PostCount
        else:
          logger.info("No new 3070 cards found")
        driver3070.quit()

        # check for new 3080 cards
        driver3080 = self.getWebDriver(RTX3080_WEBSITE)
        driver3080.implicitly_wait(10)
        sleep(3)
        rtx3080Posts = driver3080.find_elements_by_class_name('bbWrapper')
        rtx3080PostCount = len(rtx3080Posts)
        if rtx3080PostCount != self.old3080PostCount:
          if self.old3080PostCount:
            self.newGpuPosts["RTX3080"] = rtx3080Posts[-1].text
          self.old3080PostCount = rtx3080PostCount
        else:
          logger.info("No new 3080 cards found")
        driver3080.quit()

        # check for new 3070 cards
        driver3090 = self.getWebDriver(RTX3090_WEBSITE)
        driver3090.implicitly_wait(10)
        sleep(3)
        rtx3090Posts = driver3090.find_elements_by_class_name('bbWrapper')
        rtx3090PostCount = len(rtx3090Posts)
        if rtx3090PostCount != self.old3090PostCount:
          if self.old3090PostCount:
            self.newGpuPosts["RTX3090"] = rtx3090Posts[-1].text
          self.old3090PostCount = rtx3090PostCount
        else:
          logger.info("No new 3090 cards found")
        driver3090.quit()
