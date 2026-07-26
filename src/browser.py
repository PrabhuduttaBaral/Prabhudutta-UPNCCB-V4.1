"""
==========================================================
Prabhudutta-UPNCCB V4.1
Browser Module
==========================================================
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import config
from logger import logger


class Browser:

    def __init__(self):

        self.driver = None

    def start_browser(self):

        logger.info("Starting Chrome Browser...")

        options = Options()

        if config.MAXIMIZE_WINDOW:
            options.add_argument("--start-maximized")

        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")

        self.driver = webdriver.Chrome(options=options)

        self.driver.implicitly_wait(config.IMPLICIT_WAIT)

        self.driver.set_page_load_timeout(
            config.PAGE_LOAD_TIMEOUT
        )

        logger.info("Chrome Browser Started Successfully")

        return self.driver

    def close_browser(self):

        if self.driver:

            logger.info("Closing Browser")

            self.driver.quit()

            logger.info("Browser Closed")