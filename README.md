# TwitterPiBot
A Python based bot for Raspberry Pi that grabs tweets with a specific hashtag and reads them out loud.

It was a quick side project that served as a good learning exercise for me. As this was a side project, I've set a limit of 2 days to get it done. Yes, it is sort of hacked together and could use a bit of refactoring. But it still handled the top trending hashtag #StarWars for 24 hours, without breaking. So, it's stable (enough) and working fine. (*famous last words?*)


### How does it work?
This python app connects to Twitter Streaming API and captures tweets with a specific hashtag. Those captured tweets are then processed and stored in a local SQLite database that works like a queue. And lastly (every few seconds), a tweet is picked from that queue and ran through a text-to-speech engine converting the tweet into audio, that is played out through speakers connected to the audio jack.


### What’s inside?
To run, it uses a good chunk of 3rd party modules, such as:
* [Peewee](https://github.com/coleifer/peewee) (to manage models and an SQLite database)
* [Tweepy](https://github.com/tweepy/tweepy) (to access Twitter API)
* [Flite](http://www.festvox.org/flite/) (to synthetise speech from tweets)


### What do you need to make it work?
Essentially, a Raspberry Pi (running Debian) with a USB Wifi dongle attached (and connected to the internet). Then you need some source of power (such as a USB portable battery pack) and one or two speakers connected to the 3.5mm audio jack.


### How do you get this up and running?
To run the instructions below, you have two options (that I can remember):

1. plug your Raspberry Pi to a screen, mouse, keyboard and run in the terminal
2. [connect to your Raspberry via SSH](https://www.raspberrypi.org/documentation/remote-access/ssh/) from your computer and run it remotely (*which is waaay cooler!*)

I recommend the second option. And if you go with the second option, I also recommend using [`screen`](https://en.wikipedia.org/wiki/GNU_Screen) in SSH to allow [resuming your session without having to leave an SSH window open](http://raspi.tv/2012/using-screen-with-raspberry-pi-to-avoid-leaving-ssh-sessions-open). To install `screen` run the following in terminal:

`$ sudo apt-get install screen`


#### 1. Create a Twitter app
Ok, so first things first: you need to create a Twitter app to use their API. Go to https://apps.twitter.com and create a new app. Once that is done, under the "Keys and Access Tokens" tab also generate an Access Token.

#### 2. Update and install packages
Now, let's make sure your Raspberry Pi is up-to-date. In terminal run the following two commands:

`$ sudo apt-get update`

`$ sudo apt-get upgrade`


And one (more) package to install: [Flite](http://www.festvox.org/flite/), the text-to-speech engine that we'll be using. Run this:

`$ sudo apt-get install flite`


#### 3. Install app in your Raspberry Pi

Start by cloning this repository to your Raspberry Pi:

`$ git clone https://github.com/jpescada/TwitterPiBot.git`


Go into that new folder:

`$ cd TwitterPiBot/`


Make sure [`pip`](https://en.wikipedia.org/wiki/Pip_(package_manager)) is up to date:

`$ sudo pip install -U pip`


And install the python modules required for this app ([Peewee](https://github.com/coleifer/peewee) and [Tweepy](https://github.com/tweepy/tweepy)):

`$ sudo pip install -r requirements.txt`


#### 4. Update the app config

Just one last thing to do before running it for the first time. Open the `config.py` file in the root folder to update the Twitter API credentials and the hashtag to search for:

`$ sudo nano config.py`

When you're done, hit `Ctrl+X` to close and save the file.


#### 5. Finally, run the app

Just type the command:

`$ python main.py`

If everything went according to plan, it should connect to Twitter start collecting tweets and reading them out loud every 30 seconds.
 
To exit, hit `Ctrl+C`. 


### How to adjust the volume?

In terminal, run the command:

`$ alsamixer`

Then use keyboard `up` and `down` keys for volume, `m` key to mute and `esc` key to exit.


### Bugs?

What bugs? :) If you found any issues, please report it in the [Issues](https://github.com/jpescada/TwitterPiBot/issues) or, if you can fix it, submit a [Pull request](https://github.com/jpescada/TwitterPiBot/pulls). Thank you!


##### Credits

The original idea behind this project came from a client request (who later dropped it), but it's based on [Hugo the Twitter-Powered Robot](http://paper-leaf.com/hugo/) by [Paper Leaf](http://paper-leaf.com/).

