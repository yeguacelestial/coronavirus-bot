import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from dotenv import load_dotenv
from values import GOOGLE_CHROME_BIN, CHROMEDRIVER_PATH

class Coronavirus():

    def __init__(self):
        print("[*] Creating ChromeDriver instance...")
        options = webdriver.ChromeOptions()
        options.headless = True
        options.binary_location = GOOGLE_CHROME_BIN
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument("--window-size=1920,1080")

        # Capabilities
        capabilities = DesiredCapabilities.GOOGLECHROME
        capabilities.update({'VERSION':'80'})

        self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options, desired_capabilities=capabilities)
        print("[+] Chromedriver instance done.")

        print("[*] Going to URL and positioning....")
        self.driver.get('https://www.worldometers.info/coronavirus/')

        tab_position = self.driver.find_element_by_xpath('//*[@id="nav-today-tab"]')
        self.driver.execute_script('arguments[0].scrollIntoView(true);', tab_position)
        time.sleep(2)
        print("[+] Page loaded.")
    
    def quit(self):
        self.driver.quit()
        print("[+] Quitted page.")


    def fetch_yesterday_data(self):
        yesterday_btn = self.driver.find_element_by_xpath('//*[@id="nav-yesterday-tab"]')
        yesterday_btn.click()

        sort_by_country = self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[3]/div[2]/div/table/thead/tr/th[1]')
        sort_by_country.click()

        yesterday_table = self.driver.find_element_by_xpath('//*[@id="main_table_countries_yesterday"]')
        yesterday_table_text = yesterday_table.text

        starting_slice = yesterday_table_text.find('Mexico')
        ending_slice = yesterday_table_text.find('Moldova')

        row = yesterday_table_text[starting_slice:ending_slice-1]
        data = row.split(" ")

        return data
    

    def getYesterdayTotalCases(self):
        data = self.fetch_yesterday_data()
        yesterday_total_cases = data[1]
        yesterday_total_cases = yesterday_total_cases.replace(',','')
        yesterday_total_cases = int(yesterday_total_cases)
        return yesterday_total_cases


    def fetch_data(self):
        today_btn = self.driver.find_element_by_xpath('//*[@id="nav-today-tab"]')
        self.driver.execute_script('arguments[0].scrollIntoView(true);', today_btn)
        time.sleep(2)
        today_btn.click()

        sort_by_country = self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[3]/div[1]/div/table/thead/tr/th[1]')
        #sort_by_country.click()

        today_table = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]')
        today_table_text = today_table.text

        starting_slice = today_table_text.find('Mexico')
        ending_slice = today_table_text.find('Moldova')

        row = today_table_text[starting_slice:ending_slice-1]
        data = row.split(" ")
        
        return data
    

    def getCountry(self):
        data = self.fetch_data()
        country = data[0]
        return country
    

    def getTotalCases(self):
        data = self.fetch_data()
        total_cases = data[1]
        total_cases = total_cases.replace(',','')

        total_cases = int(total_cases)
        return total_cases
    

    def getNewCases(self):
        data = self.fetch_data()
        new_cases = int(data[2])
        return new_cases
    

    def getTotalDeaths(self):
        data = self.fetch_data()
        total_deaths = int(data[3])
        return total_deaths
    

    def getNewDeaths(self):
        data = self.fetch_data()
        new_deaths = int(data[4])
        return new_deaths
    

    def getTotalRecovered(self):
        data = self.fetch_data()
        total_recovered = int(data[5])
        return total_recovered
    

    def getActiveCases(self):
        data = self.fetch_data()
        active_cases = int(data[6])
        return active_cases
    

    def getSeriousCriticalCases(self):
        data = self.fetch_data()
        serious_critical_cases = int(data[7])
        return serious_critical_cases