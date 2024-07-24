from peewee import *
import datetime
from utils.db import mydb


# ORM Models
class TimelinePost(Model):
    name = CharField( )
    email = CharField()
    content = TextField()
    password = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb
