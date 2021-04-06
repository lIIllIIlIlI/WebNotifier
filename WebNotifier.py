# imports ---------------------
import logging
import sys
import configparser

from pathlib import Path
from time import sleep

import Email.email as email
import Lib.password as password
import WebParser.logitech as logitechWebsite
import WebParser.gpu as gpuWebsite


# Globals ---------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Private functions ---------------------
def checkEnvironment():
    if not sys.version_info.major == 3 and sys.version_info.minor >= 5:
        logger.critical("You are using Python %s.%s."\
                        ,sys.version_info.major, sys.version_info.minor)
        logger.critical("At least python 3.5 is required. Exiting ...")
        sys.exit(1)

def readConfigs():
    config = configparser.ConfigParser()
    iniFile = str(Path(__file__) / ".." / "config.ini")
    config.read(iniFile)
    return config

if __name__ == "__main__":
    checkEnvironment()
    config = readConfigs()
    emailAddress = config["GENERAL"]["EMAIL_ADDRESS"]
    emailPasswort = password.getEmailPassword(emailAddress)
    email = email.email(emailAddress, emailPasswort)
    webDriver = config["GENERAL"]["WEBDRIVER"]
    browser = config["GENERAL"]["BROWSER"]
    logitech = logitechWebsite.logitech(webDriver, browser)
    gpu = gpuWebsite.gpu(webDriver, browser)
    while True:
        logitech.update()
        if logitech.isChanged:
            email.sendEmail(logitech.URL, "Logitech keyboard is available")
            sleep(60*60*24)
        gpu.update()
        if gpu.changedWebsites:
            for website in gpu.changedWebsites:
                email.sendEmail(website, "Gpu ist available")
        sleep(110)