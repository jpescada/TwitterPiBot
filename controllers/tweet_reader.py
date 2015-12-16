
# import external modules
import os
from threading import Timer

import pyttsx
import talkey

from config import *
from models import tweet



def initialize():
	# wait 10 seconds to start reading
	# Timer( 10.0, read_tweet ).start()
	read_tweet()


def read_tweet():
	# recall this function after 20.0 seconds
	# Timer( 30.0, read_tweet ).start()

	print "About to read tweet..."

	# next_tweet_query = tweet.Tweet.select().where(tweet.Tweet.is_valid == True, tweet.Tweet.is_done == False).order_by(tweet.Tweet.created_at.asc()).limit(1)
	# print "Query: {}".format(next_tweet_query)

	# for next_tweet in next_tweet_query:
	# 	print "Tweet to read: {}".format(next_tweet.message.encode('utf-8'))

	try:
		# next_tweet = tweet.Tweet.get(tweet.Tweet.is_done == False)
		for next_tweet in tweet.Tweet.select().where(tweet.Tweet.is_valid == True, tweet.Tweet.is_done == False).order_by(tweet.Tweet.created_at.asc()).limit(1):
			
			print "Tweet to read: {}".format(next_tweet.message.encode('utf-8'))

			# read tweet out loud using Mac OSX "say"
			# os.system("say {}".format(next_tweet.message.encode('utf-8')))

			try:
				# read tweet out loud using pyttsx
				# tts = pyttsx.init('espeak', True)
				# tts.say( next_tweet.message.encode('utf-8') )
				# tts.runAndWait()

				# read tweet out loud using talkey
				tts = talkey.Talkey()
				tts.say( next_tweet.message )
			except:
				print "-- Error reading tweet."


			next_tweet.is_done = True
			next_tweet.save()

	except:
		print "-- No tweets found."




