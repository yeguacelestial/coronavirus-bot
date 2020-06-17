import time, os
from selenium import webdriver
from dotenv import load_dotenv

def capture(link, xpath):
    load_dotenv()
    GOOGLE_CHROME_BIN = os.getenv('GOOGLE_CHROME_BIN')
    CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH')

    options = webdriver.ChromeOptions()
    options.headless = True
    options.binary_location = GOOGLE_CHROME_BIN
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')

    with webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options) as driver:
        driver.set_window_size(826, 736)
        driver.get(link)
        time.sleep(1)
        element = driver.find_element_by_xpath(xpath)
        element_png = element.screenshot_as_png

        with open('cifras_por_estado.png', 'wb') as file:
            file.write(element_png)