import tweepy
from calculate import operations
from values import consumer_key, consumer_secret_key, access_token, access_token_secret


def main():
    auth = auth0(consumer_key, consumer_secret_key, access_token, access_token_secret)
    (today_total_cases, yesterday_total_cases, factor) = operations()

    tweet_text(auth, f"COVID19 Bot Test\nCasos de ayer: {yesterday_total_cases}\n"+
                     f"Casos de hoy: {today_total_cases}\n"+
                     f"Factor: {factor}")

def auth0(consumer_key, consumer_secret_key, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    return auth

def tweet_text(auth, text:str):
    api = tweepy.API(auth)
    api.update_status(text)

if __name__ == '__main__':
    main()