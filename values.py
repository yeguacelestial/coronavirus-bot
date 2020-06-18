import os
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret_key = os.getenv('CONSUMER_SECRET_KEY')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

GOOGLE_CHROME_BIN = os.getenv('GOOGLE_CHROME_BIN')
CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH')

minute = 60
hour = minute * 60
day = hour * 24
week = day * 7

global hashtags = ["COVID19Mx", 
            "QuedateEnCasa", 
            "Coronavirusmx",
            "COVID19Mexico",
            "COVIDー19mx",
            "Coronavirusmexico",
            "Covid_19",
            "COVID-MX",
            "SanaDistancia",
            "NuevaNormalidad",
            "QuédateEnCasa",
            "COVID19",
            "LavadoDeManos",
            "SalvaVidas"]