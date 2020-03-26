# Graph
# x -> TIME
# y -> Personas infectadas
# Nuevos infectados en un dia (DELTA_I)

# D_I7 = I8 - I7
# D_I6 = I7 - I6

# In+1 = In(EP+1)
# F = EP + 1
# Las medidas son para intentar minimizar EP
# F = In+1 / In
# In+1 = In(EP+1)
# In+1 = In*F

# In+1 = 367 -> Infectados martes
# In = 317 -> Infectados lunes
# F-actual = 367 / 317
# F-actual =  1.1613

#I(miercoles) = I(martes) * F-actual
#I(miercoles) = 367 * 1.1613
#I(miercoles) = 426

from selenium import webdriver
import time

class Coronavirus():

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.worldometers.info/coronavirus/')

        tab_position = self.driver.find_element_by_xpath('//*[@id="nav-today-tab"]')
        self.driver.execute_script('arguments[0].scrollIntoView(true);', tab_position)
        time.sleep(2)
    

    def fetch_yesterday_data(self):
        yesterday_btn = self.driver.find_element_by_xpath('//*[@id="nav-yesterday-tab"]')
        yesterday_btn.click()

        yesterday_table = self.driver.find_element_by_xpath('//*[@id="main_table_countries_yesterday"]')
        yesterday_table_text = yesterday_table.text

        row = yesterday_table_text[2405:2440-1]
        data = row.split(" ")

        return data
    

    def fetch_data(self):
        today_btn = self.driver.find_element_by_xpath('//*[@id="nav-today-tab"]')
        bot.driver.execute_script('arguments[0].scrollIntoView(true);', today_btn)
        time.sleep(2)
        today_btn.click()

        today_table = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]')
        
        country_element = today_table.find_element_by_xpath("//td[contains(text(), 'Mexico')]")
        row = country_element.find_element_by_xpath("./..")
        data = row.text.split(" ")
        
        return data
    

    def getCountry(self):
        data = self.fetch_data()
        country = data[0]
        return country
    

    def getTotalCases(self):
        data = self.fetch_data()
        total_cases = data[1]
        return total_cases
    

    def getNewCases(self):
        data = self.fetch_data()
        new_cases = data[2]
        return new_cases
    

    def getTotalDeaths(self):
        data = self.fetch_data()
        total_deaths = data[3]
        return total_deaths
    

    def getNewDeaths(self):
        data = self.fetch_data()
        new_deaths = data[4]
        return new_deaths
    

    def getTotalRecovered(self):
        data = self.fetch_data()
        total_recovered = data[5]
        return total_recovered
    

    def getActiveCases(self):
        data = self.fetch_data()
        active_cases = data[6]
        return active_cases
    

    def getSeriousCriticalCases(self):
        data = self.fetch_data()
        serious_critical_cases = data[7]
        return serious_critical_cases


