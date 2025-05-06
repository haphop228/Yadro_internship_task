#!/usr/bin/env python3
import requests
import logging
import sys

# Логирование в терминал
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

# Функция делает запрос и обрабатывает исключения, если что-то пошло не так
def make_request(url):
    try:
        response = requests.get(url)
        
        if 100 <= response.status_code < 400:
            logger.info(f"Success response - Status: {response.status_code}, Body: {response.text}")
        elif 400 <= response.status_code < 600:
            logger.error(f"Error response - Status: {response.status_code}, Body: {response.text}")
            raise Exception(f"HTTP Error {response.status_code}: {response.text}") # Кидаем исключение для 4хх и 5хх
            
        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {str(e)}")
        raise

def main():
    # Тестовые URL для запросов
    urls = [
        "https://httpstat.us/200",
        "https://httpstat.us/201",
        "https://httpstat.us/301",
        "https://httpstat.us/404",
        "https://httpstat.us/500"
    ]
    
    for url in urls:
        try:
            logger.info(f"Making request to {url}")
            make_request(url)
        except Exception as e:
            logger.error(f"Exception occurred while processing {url}: {str(e)}")

if __name__ == "__main__":
    main()