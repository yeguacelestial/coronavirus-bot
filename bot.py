import datetime
import random
import tweepy
from time import sleep
from calculate import covid19_today
from values import consumer_key, consumer_secret_key, access_token, access_token_secret, day, hour, hashtags
from screenshot import capture


def main(auth):
    results = covid19_today()

    today_total_cases = results[0] 
    yesterday_total_cases = results[1] 
    factor = results[2]
    week_cases = results[3]

    new_cases = results[4]
    total_deaths = results[5]

    global hashtags
    hashtags = hashtags.copy()

    first_hashtag = random.choice(hashtags)
    hashtags.pop(hashtags.index(first_hashtag))

    second_hashtag = random.choice(hashtags)
    hashtags.pop(hashtags.index(second_hashtag))

    third_hashtag = random.choice(hashtags)
    hashtags.pop(hashtags.index(third_hashtag))
        

    tweet_text(auth, f"#{first_hashtag} #{second_hashtag} #{third_hashtag}\n\n"+
                     f"Casos hasta el día de ayer: {yesterday_total_cases}\n"+
                     f"Casos nuevos: {new_cases}\n"+
                     f"Casos totales: {today_total_cases}\n"+
                     f"Muertes confirmadas: {total_deaths}\n\n"+
                     f"Se esperan {week_cases} casos en el país dentro de una semana.\n")
    print("[+] Tweeted.")


def auth0(consumer_key, consumer_secret_key, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    return auth


def tweet_text(auth, text:str):
    api = tweepy.API(auth)
    api.update_status(text)


def traducir_mes(numero):
    meses = {
        1: 'enero',
        2: 'febrero',
        3: 'marzo',
        4: 'abril',
        5: 'mayo',
        6: 'junio',
        7: 'julio',
        8: 'agosto',
        9: 'septiembre',
        10: 'octubre',
        11: 'noviembre',
        12: 'diciembre'
    }

    return meses[numero]


def tweet_screenshot_estados(auth):
    dt = datetime.datetime.today()
    year = dt.year
    month = traducir_mes(dt.month)
    day = dt.day

    global hashtags
    hashtags = hashtags.copy()

    first_hashtag = random.choice(hashtags)
    hashtags.pop(hashtags.index(first_hashtag))

    second_hashtag = random.choice(hashtags)
    hashtags.pop(hashtags.index(second_hashtag))

    third_hashtag = random.choice(hashtags)
    hashtags.pop(hashtags.index(third_hashtag))

    capture('https://e.infogram.com/ebc14900-0984-47df-8c99-3d0aabc01d17?src=embed', '/html/body/div[2]/div/div[2]')
    tweet = 

    api = tweepy.API(auth)
    api.update_with_media('cifras_por_estado.png', status=f"Reporte - {day} de {month} del {year}\n"+
                                                           "Cifras COVID de hoy, clasificadas por estado (Fuente: Verificovid @covidmx)\n"+
                                                          f"#{first_hashtag} #{second_hashtag} #{third_hashtag}")

    print("[+] Tweeted cifras por estado.")


if __name__ == '__main__':
    auth = auth0(consumer_key, consumer_secret_key, access_token, access_token_secret)
    print("[*] Running bot.py...")

    while 1:
        now = datetime.datetime.now()

        # Tweetear cifras de hoy
        if now.hour == 10 and now.minute == 47 and now.second == 1:
            print("[*] Running main function...")
            main(auth)

        # Tweetear cifras por estado
        if now.hour == 10 and now.minute == 50 and now.second == 1:
            print("[*] Running screenshot function...")
            tweet_screenshot_estados(auth)

        sleep(1)