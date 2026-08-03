import requests
import time

from utilities.logger import get_logger


logger = get_logger()


class APIClient:

    @staticmethod
    def get(url):
        logger.info(f"Sending GET request to {url}")
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()

        response_time = round((end_time - start_time) * 1000, 2)

        logger.info(f"Response Time: {response_time} ms")
        logger.info(f"Status Code: {response.status_code}")

        return response


    @staticmethod
    def post(url, payload):


        logger.info(f"Sending POST request to {url}")

        start_time = time.time()

        response = requests.post(url, json=payload)
        
        end_time = time.time()

        response_time = round((end_time - start_time) * 1000, 2)

        logger.info(f"Response Time: {response_time} ms")
        logger.info(f"Status Code: {response.status_code}")

        return response