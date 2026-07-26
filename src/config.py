"""
==========================================================
Prabhudutta-UPNCCB V4.1 Professional
Configuration File
==========================================================
"""

import os
from dotenv import load_dotenv

# ---------------------------------------------------------
# Load Environment Variables
# ---------------------------------------------------------

load_dotenv()

# ---------------------------------------------------------
# Login
# ---------------------------------------------------------

LOGIN_URL = "https://upn.odishadccb.in:9004/vantagepointUI/index.jsp"

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# ---------------------------------------------------------
# Browser
# ---------------------------------------------------------

HEADLESS = False

IMPLICIT_WAIT = 10

EXPLICIT_WAIT = 30

PAGE_LOAD_TIMEOUT = 60

# ---------------------------------------------------------
# Chrome
# ---------------------------------------------------------

MAXIMIZE_WINDOW = True

# ---------------------------------------------------------
# Folders
# ---------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_FOLDER = os.path.join(BASE_DIR, "data")

LOG_FOLDER = os.path.join(BASE_DIR, "logs")

SCREENSHOT_FOLDER = os.path.join(BASE_DIR, "screenshots")

# ---------------------------------------------------------
# Excel
# ---------------------------------------------------------

EXCEL_FILE = os.path.join(
    DATA_FOLDER,
    "transactions.xlsx"
)

# ---------------------------------------------------------
# Logging
# ---------------------------------------------------------

LOG_FILE = os.path.join(
    LOG_FOLDER,
    "automation.log"
)