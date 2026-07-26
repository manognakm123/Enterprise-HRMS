import logging
import os


# LOG_FOLDER = "logs"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_FOLDER = os.path.join(BASE_DIR, "logs")

os.makedirs(LOG_FOLDER, exist_ok=True)


def get_logger():

    logger = logging.getLogger("HRMS")

    if logger.handlers:
        return logger
    

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        os.path.join(LOG_FOLDER, "automation.log"),
        mode="a"
    )

    file_handler.setFormatter(formatter)


    #Console Handler

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)


    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


    return logger