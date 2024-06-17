import logging
import os
from datetime import datetime

# Create a logs directory if it doesn't exist
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Create a log file with a timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Add a console handler to output logs to the console as well
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter("[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"))

logging.getLogger().addHandler(console_handler)

# if __name__ == "__main__":
#     logging.info("Logger is configured and ready to use.")
#     try:
#         x = 1 / 0
#     except ZeroDivisionError as e:
#         logging.error("An error occurred: %s", e)