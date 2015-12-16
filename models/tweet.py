
# import external modules
import datetime

from peewee import *

from models import base_model


class Tweet(base_model.BaseModel):
	message = CharField()
	author = CharField()
	is_valid = BooleanField(default=True)
	is_done = BooleanField(default=False)
	json_data = TextField()
	created_at = DateTimeField(default=datetime.datetime.now)
	updated_at = DateTimeField(default=datetime.datetime.now)

	class Meta:
		order_by = ('-created_at',)



def initialize():
	base_model.DATABASE.connect()
	# DATABASE.create_tables([Tweet], safe=True)
	Tweet.create_table(True)
	base_model.DATABASE.close()