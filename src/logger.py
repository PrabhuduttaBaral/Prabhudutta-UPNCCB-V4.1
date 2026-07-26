"""
==========================================================
Prabhudutta-UPNCCB V4.1
Logger
==========================================================
"""

import logging
import os

import config

# ---------------------------------------------------------
# Create log folder
# ---------------------------------------------------------

os.makedirs(config.LOG_FOLDER, exist_ok=True)

# ---------------------------------------------------------
# Logger
# ---------------------------------------------------------

logger = logging.getLogger("UPNCCB")

logger.setLevel(logging.INFO)

logger.handlers.clear()

# ---------------------------------------------------------
# File Handler
# ---------------------------------------------------------

file_handler = logging.FileHandler(
    config.LOG_FILE,
    encoding="utf-8"
)

file_handler.setLevel(logging.INFO)

# ---------------------------------------------------------
# Console Handler
# ---------------------------------------------------------

console_handler = logging.StreamHandler()

console_handler.setLevel(logging.INFO)

# ---------------------------------------------------------
# Formatter
# ---------------------------------------------------------

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s",
    "%d-%m-%Y %H:%M:%S"
)

file_handler.setFormatter(formatter)

console_handler.setFormatter(formatter)

# ---------------------------------------------------------
# Add Handlers
# ---------------------------------------------------------

logger.addHandler(file_handler)

logger.addHandler(console_handler)

# ---------------------------------------------------------
# Test
# ---------------------------------------------------------

logger.info("Logger Initialized")