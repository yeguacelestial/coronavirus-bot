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

class Coronavirus():

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.worldometers.info/coronavirus/')
    
    def fetch_data(self):
        today_table = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]')
        yesterday_table = self.driver.find_element_by_xpath('//*[@id="main_table_countries_yesterday"]')
        
        country_element = today_table.find_element_by_xpath("//td[contains(text(), 'Mexico')]")
        row = country_element.find_element_by_xpath("./..")
        data = row.text.split(" ")
        return data
    
    def getCountry(self):
        data = self.fetch_data()
        country = data[0]
        return print(country)
        

