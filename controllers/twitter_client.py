
# import external modules
import json
import re

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

from config import *
from models import tweet


# write stream to database
class TwitterStreamListener(StreamListener):

	def on_data(self, data):
		
		# print "tweet.data:\n{}".format(data)

		if data:
			tweet_json = json.loads(data)

			# print "tweet.json_data:\n{}".format(tweet_json)

			if tweet_json:

				# ignore retweets
				if not tweet_json['text'].strip().startswith('RT '):

					# clean tweet text
					clean_tweet = get_text_cleaned(tweet_json)

					# check if tweet is not empty after cleanup
					if clean_tweet:

						# register tweet in database
						tweet.Tweet.create(
							message=clean_tweet.strip(),
							author=tweet_json['user']['screen_name'],
							json_data=data
							)

		return True

	def on_error(self, status):
		print status
		if status == 420:
			# disconnect from Twitter if being Rate Limited (https://dev.twitter.com/rest/public/rate-limiting)
			return False


# clean up tweet text from urls, mentions, hashtags, etc
def get_text_cleaned(tweet):
	# source: https://gist.github.com/timothyrenner/dd487b9fd8081530509c
	text = tweet['text']

	slices = []
	# Strip out the urls
	if 'urls' in tweet['entities']:
		for url in tweet['entities']['urls']:
			slices += [{'start': url['indices'][0], 'stop': url['indices'][1]}]

	# Strip out the hashtags (except if it's the one we're using to filter).
	if 'hashtags' in tweet['entities']:
		for tag in tweet['entities']['hashtags']:
			if not tag == TWITTER_HASHTAG:
				slices += [{'start': tag['indices'][0], 'stop': tag['indices'][1]}]

	# Strip out the user mentions.
	# if 'user_mentions' in tweet['entities']:
	# 	for men in tweet['entities']['user_mentions']:
	# 		slices += [{'start': men['indices'][0], 'stop': men['indices'][1]}]

	# Strip out the media.
	if 'media' in tweet['entities']:
		for med in tweet['entities']['media']:
			slices += [{'start': med['indices'][0], 'stop': med['indices'][1]}]

	# Strip out the symbols.
	if 'symbols' in tweet['entities']:
		for sym in tweet['entities']['symbols']:
			slices += [{'start': sym['indices'][0], 'stop': sym['indices'][1]}]

	# Sort the slices from highest start to lowest.
	slices = sorted(slices, key=lambda x: -x['start'])

	# No offsets, since we're sorted from highest to lowest.
	for s in slices:
		text = text[:s['start']] + text[s['stop']:]
	
	# remove "dot space" remains from beginning when mentioning someone
	if text.startswith('. '):
		text = text[2:]

	# replace other entities
	text = text.replace('&amp;', 'and')
	text = text.replace('&gt;', 'greater than')
	text = text.replace('&lt;', 'lower than')

	# remove new lines
	text = text.replace('\n','')

	# remove whitespaces before and after string
	text = text.strip()

	return text


# connect to Twitter API
def initialize():

	output = TwitterStreamListener()

	# setup Twitter API connection details
	twitter_auth = OAuthHandler( TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET )
	twitter_auth.set_access_token( TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET )
	
	# connect to Twitter Streaming API
	twitter_stream = Stream( twitter_auth, output )

	# filter tweets using track, follow and/or location parameters
	# https://dev.twitter.com/streaming/reference/post/statuses/filter
	twitter_stream.filter(track=[ TWITTER_HASHTAG ])


# def cleanup():
# 	twitter_stream.disconnect()
