from flask import Flask, jsonify, request
from playhouse.shortcuts import model_to_dict
from app.views import views
from peewee import *
import os
import datetime

# Initializing App
app = Flask(__name__)

# Setup of Database
mydb = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)


# ORM Models
class TimelinePost(Model):
    name = CharField( )
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])


# Database Paths
@app.route("/api/timeline_post", methods=['GET'])
def getTimelinePost():
    return { 'timeline_posts' : [ model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc()) ] }


@app.route("/api/timeline_post", methods=['POST'])
def postTimelinePost():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)
 


@app.route("/api/timeline_post", methods=['DELETE'])
def deleteTimelinePost():
    name = request.form['name']
    startDate = request.form['start'].strip('"')
    endDate = request.form['end'].strip('"')
    print(startDate, endDate)
    # Convert start_date and end_date to datetime objects
    start_date = datetime.datetime.strptime(startDate, '%a, %d %b %Y %H:%M:%S %Z')
    end_date = datetime.datetime.strptime(endDate, '%a, %d %b %Y %H:%M:%S %Z')

    query = TimelinePost.delete().where(
        (TimelinePost.name == name) & 
        (TimelinePost.created_at.between(start_date, end_date))
    )

    return jsonify({ "delete_count": query.execute() })



app.register_blueprint(views)
app.run(debug=True, port=5001)
