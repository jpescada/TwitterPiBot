#!/usr/bin/env python

# import external modules

# import os
# import json
# import threading


from config import *
from models import tweet
from controllers import twitter_client
from controllers import tweet_reader




# run default process
if __name__ == '__main__':

	print "Bot starting... Press Ctrl+C to stop."

	tweet.initialize()

	tweet_reader.initialize()
	
	twitter_client.initialize()

	


	



