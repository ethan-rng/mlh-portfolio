from flask import Flask, jsonify, request
from playhouse.shortcuts import model_to_dict
from app.views import views
from app.util_func import *
from utils.db import mydb
from models.Timeline import TimelinePost
import datetime
import os
from dotenv import load_dotenv


load_dotenv()
print(os.getenv('API_URL'))

# Initializing App
app = Flask(__name__)


mydb.connect()
mydb.create_tables([TimelinePost])


# Database Paths
@app.route("/api/timeline_post", methods=['GET'])
def getTimelinePost():
    return { 'timeline_posts' : [ model_to_dict(p, exclude=[TimelinePost.password]) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc()) ] }


@app.route("/api/timeline_post", methods=['POST'])
def postTimelinePost():

    # Validate the information
    if "name" not in request.form or len(request.form['name']) == 0:
        return {"result": "Invalid name"}, 400
    if "email" not in request.form or len(request.form['email']) == 0:
        return {"result": "Invalid email"}, 400
    if "content" not in request.form or len(request.form['content']) == 0:
        return {"result": "Invalid content"}, 400
    if "password" not in request.form or len(request.form['password']) == 0:
        return {"result": "Invalid password"}, 400
    
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    password = request.form['password']

    if not validate_email(email):
        return {"result": "Invalid email"}, 400

    timeline_post = TimelinePost.create(name=name, email=email, content=content, password=hash_password(password).decode('utf-8'))

    return model_to_dict(timeline_post, exclude=[TimelinePost.password])
 

@app.route("/api/timeline_post", methods=['DELETE'])
def deleteTimelinePost():
    name = request.form['name']
    startDate = request.form['start'].strip('"')
    endDate = request.form['end'].strip('"')
    password = request.form['password']
    print(password)

    if password == os.getenv("ULT_PASSWORD"):
         query = TimelinePost.delete()
    else:
        if not verify_password(TimelinePost, name, password):
            return {"result": "Password verification failed"}, 400

        # Convert start_date and end_date to datetime objects
        start_date = datetime.datetime.strptime(startDate, '%a, %d %b %Y %H:%M:%S %Z')
        end_date = datetime.datetime.strptime(endDate, '%a, %d %b %Y %H:%M:%S %Z')
        
        query = TimelinePost.delete().where(
            (TimelinePost.name == name) & 
            (TimelinePost.created_at.between(start_date, end_date))
        )

    count = query.execute()
    print(count)
    return jsonify({ "result": "Success", "delete_count": count })



app.register_blueprint(views)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)