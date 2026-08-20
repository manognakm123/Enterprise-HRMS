import requests
import time

from config.config import Config
from utilities.logger import get_logger


logger = get_logger()


class APIClient:


    @staticmethod
    def get(endpoint):

        url = f"{Config.BASE_URL}{endpoint}"

        logger.info(f"Sending GET request to {url}")

        response = requests.get(url)

        logger.info(f"Response Time: {response.elapsed.total_seconds() * 1000:.2f} ms")
        logger.info(f"Status Code: {response.status_code}")

        return response



    @staticmethod
    def post(endpoint, payload):

        url = f"{Config.BASE_URL}{endpoint}"

        logger.info(f"Sending POST request to {url}")

        start_time = time.time()

        response = requests.post(url, json=payload)

        end_time = time.time()

        response_time = round((end_time - start_time) * 1000, 2)

        logger.info(f"Response Time: {response_time} ms")
        logger.info(f"Status Code: {response.status_code}")

        return response


    @staticmethod
    def put(endpoint, payload):

        url = f"{Config.BASE_URL}{endpoint}"

        logger.info(f"Sending PUT request to {url}")

        start_time = time.time()

        response = requests.put(url, json=payload)

        end_time = time.time()

        response_time = round((end_time - start_time) * 1000, 2)

        logger.info(f"Response Time: {response_time} ms")
        logger.info(f"Status Code: {response.status_code}")

        return response



    @staticmethod
    def delete(endpoint):
        
        url = f"{Config.BASE_URL}{endpoint}"

        logger.info(f"Sending DELETE request to {url}")

        start_time = time.time()

        response = requests.delete(url)

        end_time = time.time()

        response_time = round((end_time - start_time) * 1000, 2)

        logger.info(f"Response Time: {response_time} ms")
        logger.info(f"Status Code: {response.status_code}")

        return response