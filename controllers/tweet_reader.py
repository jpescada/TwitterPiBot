
# import external modules
import os
import subprocess
from threading import Timer

# import pyttsx
# import talkey

from config import *
from models import tweet



def initialize():
	# wait 10 seconds to start reading
	Timer( 10.0, read_tweet ).start()
	# read_tweet()

def get_text_sanitized(text):

	#  \ ' " ` < > | ; <Space> <Tab> <Newline> ( ) [ ] ? # $ ^ & * =

	# escape quotes
	text = text.replace('"','\"').replace("'","\'").replace('`','\`')

	# remove special shell characters
	text = text.replace('\\','')
	
	text = text.replace('|','\|')
	text = text.replace('#','\#')
	text = text.replace('$','\$')
	text = text.replace('^','\^')
	text = text.replace('&','\&')
	text = text.replace('*','\*')
	text = text.replace('=','\=')

	text = text.replace(';','\;').replace('?','\?').replace('!','\!')

	text = text.replace('<Space>',' ')
	text = text.replace('<Tab>',' ')
	text = text.replace('<Newline>',' ')

	text = text.replace('<','\<').replace('>','\>')
	text = text.replace('(','\(').replace(')','\)')
	text = text.replace('[','\[').replace(']','\]')
	text = text.replace('{','\{').replace('}','\}')

	return text



def read_tweet():
	# recall this function after 10.0 seconds
	Timer( 10.0, read_tweet ).start()

	print "About to read tweet..."

	# next_tweet_query = tweet.Tweet.select().where(tweet.Tweet.is_valid == True, tweet.Tweet.is_done == False).order_by(tweet.Tweet.created_at.asc()).limit(1)
	# print "Query: {}".format(next_tweet_query)

	# for next_tweet in next_tweet_query:
	# 	print "Tweet to read: {}".format(next_tweet.message.encode('utf-8'))
		# subprocess.call( "flite -voice kal16 -t {}".format( get_text_sanitized( next_tweet.message.encode('utf-8') ) ) )
		# os.system( 'flite -voice kal16 -t "{}"'.format( get_text_sanitized( next_tweet.message.encode('utf-8') ) ))

	try:
		
		next_tweet_query = tweet.Tweet.select().where(tweet.Tweet.is_valid == True, tweet.Tweet.is_done == False).order_by(tweet.Tweet.created_at.asc()).limit(1)

		for next_tweet in next_tweet_query:
			
			print 'Tweet to read: "{}"'.format( get_text_sanitized( next_tweet.message.encode('utf-8') ) )

			# read tweet out loud using Mac OSX "say"
			# os.system("say {}".format(next_tweet.message.encode('utf-8')))

			# read tweet out loud using Festival
			# os.system("echo ""{}"" | festival --tts".format(next_tweet.message.encode('utf-8')))

			# read tweet out loud using Flite
			# os.system("flite -voice kal16 -t ""{}""".format( next_tweet.message.encode('utf-8') ))
			# os.system("aoss flite-2.0.0/bin/flite -voice voices/cmu_us_aew.flitevox -t ""{}""".format(next_tweet.message.encode('utf-8')))
			os.system( 'flite -voice kal16 -t "{}"'.format( get_text_sanitized( next_tweet.message.encode('utf-8') ) ))
			# subprocess.call( "flite -voice kal16 -t {}".format( get_text_sanitized( next_tweet.message.encode('utf-8') ) ))

			# try:
				# read tweet out loud using pyttsx
				# tts = pyttsx.init('espeak', True)
				# tts.say( next_tweet.message )
				# tts.runAndWait()

				# read tweet out loud using talkey
				# tts = talkey.Talkey()
				# tts.say( next_tweet.message )
			# except:
			# 	print "-- Error reading tweet."


			next_tweet.is_done = True
			next_tweet.save()

	except:
		print "-- No tweets found."




