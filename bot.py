import tweepy
from values import consumer_key, consumer_secret_key, access_token, access_token_secret


def main():
    auth = auth0(consumer_key, consumer_secret_key, access_token, access_token_secret)
    tweet_text(auth, 'COVID19 Bot test')

def auth0(consumer_key, consumer_secret_key, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    return auth

def tweet_text(auth, text:str):
    api = tweepy.API(auth)
    api.update_status(text)

if __name__ == '__main__':
    main()