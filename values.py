import os
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret_key = os.getenv('CONSUMER_SECRET_KEY')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')