# imports ---------------------
import logging
import sys
import configparser

from pathlib import Path
from time import sleep

import Email.email as email
import Lib.password as password
import WebParser.website as website


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
    url = config["GENERAL"]["TRACKED_WEBSITE"]
    webDriver = config["GENERAL"]["WEBDRIVER"]
    browser = config["GENERAL"]["BROWSER"]
    website = website.website(url, webDriver, browser)
    while True:
        website.update()
        if website.isChanged:
            email.sendEmail(website.URL, "Logitech keyboard is available")
        sleep(9000)