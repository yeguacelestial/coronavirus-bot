import tweepy
from calculate import covid19_today
from values import consumer_key, consumer_secret_key, access_token, access_token_secret


def main():
    auth = auth0(consumer_key, consumer_secret_key, access_token, access_token_secret)
    results = covid19_today()

    today_total_cases = results[0] 
    yesterday_total_cases = results[1] 
    factor = results[2]

    estimated_tomorrow = int(today_total_cases * factor)
    estimated_tomorrow_plus_one = int(estimated_tomorrow * factor)
    estimated_tomorrow_plus_two = int(estimated_tomorrow_plus_one * factor)

    tweet_text(auth, f"COVID19 Bot Test\nCasos de ayer: {yesterday_total_cases}\n"+
                     f"Casos de hoy: {today_total_cases}\n"+
                     f"Casos esperados mañana: {estimated_tomorrow}\n"+
                     f"Casos esperados el viernes: {estimated_tomorrow_plus_one}\n"+
                     f"Casos esperados el sábado: {estimated_tomorrow_plus_two}")

def auth0(consumer_key, consumer_secret_key, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    return auth

def tweet_text(auth, text:str):
    api = tweepy.API(auth)
    api.update_status(text)

if __name__ == '__main__':
    main()