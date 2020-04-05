import tweepy
from calculate import covid19_today
from values import consumer_key, consumer_secret_key, access_token, access_token_secret


def main():
    auth = auth0(consumer_key, consumer_secret_key, access_token, access_token_secret)
    results = covid19_today()

    today_total_cases = results[0] 
    yesterday_total_cases = results[1] 
    factor = results[2]
    week_cases = results[3]

    new_cases = results[4]
    total_deaths = results[5]

    tweet_text(auth, f"#COVID19Mx\n\n"+
                     f"Casos hasta el día de ayer: {yesterday_total_cases}\n"+
                     f"Casos nuevos: {new_cases}\n"+
                     f"Casos totales hasta hoy: {today_total_cases}\n"+
                     f"Muertes confirmadas: {total_deaths}\n\n"+
                     f"Si la propagación sigue el mismo ritmo, en una semana se esperan {week_cases} casos en el país.\n")

def auth0(consumer_key, consumer_secret_key, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    return auth

def tweet_text(auth, text:str):
    api = tweepy.API(auth)
    api.update_status(text)

if __name__ == '__main__':
    main()