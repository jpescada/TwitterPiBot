#!/usr/bin/env python

# import external modules

import atexit

from config import *
from models import tweet
from controllers import twitter_client
from controllers import tweet_reader




def goodbye():
	print "See you later!"
	tweet_reader.cleanup()
	# twitter_client.cleanup()


atexit.register(goodbye)


# run default process
if __name__ == '__main__':

	print "Bot starting... Press Ctrl+C to stop."

	tweet.initialize()

	tweet_reader.initialize()

	twitter_client.initialize()

	


	



