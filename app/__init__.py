import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/experience')
def experience():
    # Define the data
    data = {
        'work_experiences': [
            {
                'company': 'Company A',
                'position': 'Software Engineer',
                'duration': '2018-2020',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
            },
            {
                'company': 'Company B',
                'position': 'Data Analyst',
                'duration': '2020-2022',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
            }
        ],
        'educations': [
            {
                'institution': 'University A',
                'degree': 'Bachelor of Science',
                'duration': '2014-2018'
            },
            {
                'institution': 'University B',
                'degree': 'Master of Science',
                'duration': '2018-2020'
            }
        ]
    }

    return render_template('experience.html', **data)

@app.route('/hobbies')
def hobbies():
    data = {
        'hobbies': [
            {
                'name': 'Gaming',
                'image': 'path/to/image'
            },
            {
                'name': 'Working out',
                'image': 'path/to/image'
            },
            {
                'name': 'Eating',
                'image': 'path/to/image'
            },

        ]
    }

    return render_template('hobbies.html', **data)    

