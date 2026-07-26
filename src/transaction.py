"""
Prabhudutta-UPNCCB V4.1
transaction.py
"""

from logger import logger


class Transaction:

    def __init__(self, driver):
        self.driver = driver

    def start(self):
        logger.info("=" * 50)
        logger.info("Transaction Module Started")
        logger.info("=" * 50)

    def click_wings(self):
        logger.info("Clicking WINGS Card...")
        # Code will be added in Build 2

    def open_cash_withdrawal(self):
        logger.info("Opening Cash Withdrawal...")
        # Code will be added in Build 2

    def process_transaction(self, account_no, amount, token_no):
        """
        Process a single transaction
        """

        logger.info("-" * 50)
        logger.info(f"Account : {account_no}")
        logger.info(f"Amount  : {amount}")
        logger.info(f"Token   : {token_no}")

        # Build 3
        # Enter Account Number
        # Enter Amount
        # Enter Token Number
        # Submit
        # Read Voucher Number

        voucher_no = ""

        logger.info(f"Voucher : {voucher_no}")

        return voucher_no

    def stop(self):
        logger.info("Transaction Module Stopped")