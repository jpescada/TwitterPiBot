
# import exterma; modules
from peewee import *

DATABASE = SqliteDatabase('tweets.db')

class BaseModel(Model):
	class Meta:
		database = DATABASE
	
		