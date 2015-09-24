import oauth2 as oauth
import json
import indicoio

indicoio.config.api_key = 'cefbad22a7e5ec30249944224c23ac7f'

CONSUMER_KEY = "zmXuYNAB8FqxUjlnWG5pZVtvR"
CONSUMER_SECRET = "6jyvdvVPNN8xfml3YgWQCq2o1mayZlZM82aEPp72DplkxZHmmm"
ACCESS_KEY = "77296006-bur7KzSwTjRjuliWYkh8YhaAB5uRaPFgp2sSTosxi"
ACCESS_SECRET = "iykekxTsyKl1yOq0xGxjnpB5y0fai5dxDkuVKcTgYv09a"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

screen_name = "wordpress"
#timeline_endpoint = "https://api.twitter.com/1.1/statuses/home_timeline.json"
timeline_endpoint = "https://api.twitter.com/1.1/search/tweets.json?q=%23superbowl&result_type=recent"
response, data = client.request(timeline_endpoint)

tweets = json.loads(data)
for tweet in tweets:
    print tweet['text'].encode('utf-8')
    # print(indicoio.sentiment(tweet['text'].encode('utf-8')))



