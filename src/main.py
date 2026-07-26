"""
Prabhudutta-UPNCCB V4.1
main.py
"""

import threading

import config
from browser import Browser
from login import Login
from logger import logger
from ui import AppUI


class CashWithdrawalApp:

    def __init__(self):
        self.ui = AppUI()

        # Connect button events
        self.ui.btn_start.config(command=self.start)
        self.ui.btn_stop.config(command=self.stop)

        self.browser = None
        self.driver = None

    def start(self):
        threading.Thread(target=self.run_process, daemon=True).start()

    def run_process(self):

        try:
            self.ui.set_status("Starting Browser...")
            self.ui.write_log("Starting Chrome Browser...")

            self.browser = Browser()
            self.driver = self.browser.start_browser()

            self.ui.write_log("Chrome Started")

            login = Login(self.driver)

            self.ui.write_log("Opening Login Page")
            login.open_login()

            self.ui.write_log("Logging In")

            result = login.login(
                config.USERNAME,
                config.PASSWORD
            )

            if result:
                self.ui.set_status("Dashboard Loaded")
                self.ui.write_log("Login Successful")
            else:
                self.ui.set_status("Login Failed")
                self.ui.write_log("Login Failed")

        except Exception as e:
            logger.exception(e)
            self.ui.write_log(str(e))
            self.ui.set_status("Error")

    def stop(self):

        try:
            if self.driver:
                self.driver.quit()

            self.ui.set_status("Stopped")
            self.ui.write_log("Application Stopped")

        except Exception as e:
            logger.exception(e)

    def run(self):
        self.ui.run()