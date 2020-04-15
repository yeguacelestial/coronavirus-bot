import datetime
import random
import tweepy
from time import sleep
from calculate import covid19_today
from values import consumer_key, consumer_secret_key, access_token, access_token_secret, day, hour


def main():
    auth = auth0(consumer_key, consumer_secret_key, access_token, access_token_secret)
    results = covid19_today()

    today_total_cases = results[0] 
    yesterday_total_cases = results[1] 
    factor = results[2]
    week_cases = results[3]

    new_cases = results[4]
    total_deaths = results[5]

    hashtags = ["COVID19Mx", 
                "QuedateEnCasa", 
                "Coronavirusmx",
                "MexicoEnCuarentena",
                "COVID19Mexico",
                "COVIDー19mx",
                "Coronavirusmexico",
                "Covid_19"]

    first_hashtag = random.choice(hashtags)
    hashtags.pop(hashtags.index(first_hashtag))

    second_hashtag = random.choice(hashtags)
    hashtags.pop(hashtags.index(second_hashtag))

    third_hashtag = random.choice(hashtags)
    hashtags.pop(hashtags.index(third_hashtag))
        

    tweet_text(auth, f"#{first_hashtag} #{second_hashtag} #{third_hashtag}\n\n"+
                     f"Casos hasta el día de ayer: {yesterday_total_cases}\n"+
                     f"Casos nuevos: {new_cases}\n"+
                     f"Casos totales hasta hoy: {today_total_cases}\n"+
                     f"Muertes confirmadas: {total_deaths}\n\n"+
                     f"Si la propagación sigue igual, se esperan {week_cases} casos en el país dentro de una semana.\n")
    print("[+] Tweeted.")

def auth0(consumer_key, consumer_secret_key, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    return auth

def tweet_text(auth, text:str):
    api = tweepy.API(auth)
    api.update_status(text)

if __name__ == '__main__':
    print("[*] Running bot.py...")
    while 1:
        now = datetime.datetime.now()
        if now.hour == 23 and now.minute == 35 and now.second == 00:
            print("[*] Running main function...")
            main()
        sleep(1)