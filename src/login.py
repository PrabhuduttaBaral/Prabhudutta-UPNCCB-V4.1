"""
Prabhudutta-UPNCCB V4.1 - login.py
"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
from logger import logger

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.EXPLICIT_WAIT)

    def open_login(self):
        logger.info("Opening Login Page")
        self.driver.get(config.LOGIN_URL)

    def login(self, username, password):
        try:
            user=self.wait.until(EC.element_to_be_clickable((By.ID,"username")))
            user.clear()
            user.send_keys(username)
            user.send_keys(Keys.ENTER)

            pwd=self.wait.until(EC.element_to_be_clickable((By.ID,"password")))
            pwd.clear()
            pwd.send_keys(password)
            pwd.send_keys(Keys.ENTER)

            logger.info("Complete OTP manually")
            self.wait_for_dashboard()
            return True
        except Exception as e:
            logger.exception(e)
            return False

    def wait_for_dashboard(self):
        current=self.driver.current_url
        while self.driver.current_url==current:
            time.sleep(1)
        logger.info("Dashboard Loaded")

    def click_wings(self):
        for xp in (
            "//b[normalize-space()='Wings']",
            "//h4[.//b[normalize-space()='Wings']]",
            "//*[normalize-space()='Wings']",
        ):
            try:
                el=self.wait.until(EC.element_to_be_clickable((By.XPATH,xp)))
                self.driver.execute_script("arguments[0].click();",el)
                return True
            except Exception:
                pass
        return False

    def wait_for_cash_withdrawal(self):
        tabs=len(self.driver.window_handles)
        while len(self.driver.window_handles)==tabs:
            time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait.until(EC.presence_of_element_located((By.ID,"txtAccNo")))
