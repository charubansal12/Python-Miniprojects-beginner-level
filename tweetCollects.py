from twython import Twython
from twython import TwythonStreamer


twitter = Twython(app_key='xxxx',
    app_secret='xxxx',
    oauth_token='xxxx',
    oauth_token_secret='xxxx')


user_timeline = twitter.get_user_timeline(screen_name="charu201",count=200)
str="RT"
for tweet in user_timeline:
	if tweet['lang'] =="en" :
		if (not tweet['text'].startswith(str)):
			print tweet['text']
			cnt=cnt+1

print cnt
