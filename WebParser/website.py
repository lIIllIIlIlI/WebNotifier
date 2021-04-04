# imports ---------------------
import logging
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
        options = Options()
        # options.set_headless(headless=True)
        options.binary = self.browser
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = True #optional
        driver = Firefox(firefox_options=options, capabilities=cap, executable_path=self.webDriver)
        driver.get(self.URL)
        driver.implicitly_wait(10)
        sleep(5)
        driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()
        languageSelection = driver.find_element_by_class_name("js-product-model-selector")
        sleep(4)
        driver.find_element_by_xpath('/html/body/div[1]/div/main/div[1]/div/div[12]/section/div/div/div[2]/div/div[4]/div[1]/ul/li[2]/button').click()
        sleep(4)
        dropdownMenu = Select(languageSelection)
        dropdownMenu.select_by_value("deutsch(qwertz)")
        clickSelection = driver.find_elements_by_class_name("js-product-model-selector")
        actualClickSelection = clickSelection[1]
        dropdownMenu = Select(actualClickSelection)
        dropdownMenu.select_by_value("clicky")
        colors = driver.find_elements_by_class_name("color-swatch js-color-swatch disabled")
        print("hello")

        # <button class="color-swatch js-color-swatch disabled" data-color-id="white" data-hexes="" data-bg-img="https://resource.logitechg.com/w_677,ar_1:1,c_limit,b_rgb:2f3132,q_auto:best,f_auto,dpr_auto/content/dam/gaming/en/products/swatch/white.jpg?v=1" aria-label="Weiß">
		# 		<span class="swatch js-swatch" style="background-image: url(&quot;https://resource.logitechg.com/w_677,ar_1:1,c_limit,b_rgb:2f3132,q_auto:best,f_auto,dpr_auto/content/dam/gaming/en/products/swatch/white.jpg?v=1&quot;);">
		# 			<span class="swatch-color-1 js-color-1"></span>
		# 			<span class="swatch-color-2 js-color-2"></span>
		# 		</span>
		# 		</button>
# <select class="js-product-model-selector" aria-label="EINEN STIL AUSWÄHLEN" data-error-text="Stil wählen" data-facet-key="dr.style">
# <select class="js-product-model-selector" aria-label="EINEN STIL AUSWÄHLEN" data-error-text="Stil wählen" data-facet-key="dr.style">
# <select class="js-product-model-selector" aria-label="EINEN STIL AUSWÄHLEN" data-error-text="Stil wählen" data-facet-key="dr.style">
# 			<option value="">EINEN STIL AUSWÄHLEN</option>
# 			<option value="tactile" data-label="Tactile">Tactile</option>
# <option value="linear" data-label="Linear">Linear</option>
# <option value="clicky" data-label="Clicky">Clicky</option>

        if False:
            self.isChanged = True

# class train(commuteClass):
#     def __init__(self, config):
#         self.name = "TRAIN"
#         self._TRAIN_STATION_START = config["TRAIN_STATION_START"]
#         self._TRAIN_STATION_DESTINATION = config["TRAIN_STATION_DESTINATION"]
#         self._TRAIN_ID = config["TRAIN_ID"]
#         tresholds = []
#         tresholds.append(treshold("TRESHOLD_LATENESS", config["TRESHOLD_LATENESS"]))
#         super().__init__(tresholds)
#         return

#     def calculateCommute(self):
#         #searchBox.send_keys(Keys.RETURN)
#         binary = r'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
#         options = Options()
#         # reenable to run headless
#         # options.set_headless(headless=True)
#         options.binary = binary
#         cap = DesiredCapabilities().FIREFOX
#         cap["marionette"] = True #optional
#         driver = Firefox(firefox_options=options, capabilities=cap, executable_path="C:\\Users\\lukas\\Documents\\Skripte\\geckodriver.exe")
#         driver.get("https://reiseauskunft.bahn.de/bin/query.exe/dn?protocol=https:")
#         searchTrainstationStart = driver.find_element_by_id("locS0")
#         searchTrainstationStart.send_keys(self._TRAIN_STATION_START)
#         searchTrainstationDestination = driver.find_element_by_id("locZ0")
#         searchTrainstationDestination.send_keys(self._TRAIN_STATION_DESTINATION)
#         searchButton = driver.find_element_by_id("searchConnectionButton")
#         searchButton.click()
#         try:
#             i = 0
#             results = []
#             while(i < 3):
#                 resultBody = WebDriverWait(driver, 10).until(
#                              EC.presence_of_element_located((By.ID, "overview_updateC1-" + str(i))))
#                 results.append(resultBody)
#                 i += 1
#         finally:
#             pass
#         for result in results:
#             # check if the result is suitable
#             time = result.find_elements_by_class_name("time")[0].text
#             duration = result.find_elements_by_class_name("duration.lastrow")[0].text
#             trainId = result.find_elements_by_class_name("products.lastrow")[0].text
#             changges = result.find_elements_by_class_name("changes.lastrow")[0].text
#             if changes != "0":
#                 continue
#             if duration >= self._TRESHOLD_DURATION:
#                 continue
#             timeStart = ..
#             timeDelayedStart = ..
#             currentTime = ..
#             if timeStart - currentTime > 1h:
#                 continue

#         driver.quit()
#         return

#     def getCommuteSummary(self):
#         return