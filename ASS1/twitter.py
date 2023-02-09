from dotenv import dotenv_values
import tweepy
import csv
config = dotenv_values("ASS1/.env")
print(config["API_KEY"])

api_key = config["API_KEY"]
api_key_secret = config["API_KEY_SECRET"]
bearer_token = config['BEARER_TOKEN']
access_token = config['ACCESS_TOKEN']
access_token_secret = config['ACCESS_TOKEN_SECRET']

# Authenticate
auth = tweepy.Client(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user2 = api.get_user(screen_name="sumithemmadi")

# print(user2.id)

api = tweepy.API(auth)
hashtag = "#environment"

tweets = tweepy.Cursor(api.search_tweets, hashtag).items(1000)
with open('tweets.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
writer.writerow(["Username", "Tweet Text", "Timestamp"])

for tweet in tweets:
    writer.writerow([tweet.user.screen_name, tweet.text, tweet.created_at])
