from flask import Blueprint, render_template, request
from app import data
import os
from dotenv import load_dotenv


load_dotenv()
views = Blueprint('views', __name__, template_folder='templates')


# Hero Page
@views.route('/')
def hero():
    return render_template('hero.html')

# About Me
@views.route('/aboutme')
def about_me():
    return render_template('routes/aboutme/about_me.html', navbar=data.NavBarItems, footer=data.FooterItems, timeline=data.WorkExperience)

# Hobbies
@views.route('/hobbies')
def hobbies():
    return render_template('routes/hobbies/hobbies.html', navbar=data.NavBarItems, footer=data.FooterItems, data=data.HobbyHeader, hobbies=data.Hobby)

# Timeline
@views.route('/timeline')
def blog():
    return render_template('routes/blog/timeline.html', navbar=data.NavBarItems, footer=data.FooterItems, data=data.TimelineHeader, api_url=os.getenv('API_URL'))

# Projects
@views.route('/projects')
def project():
    return render_template('routes/projects/projects.html', navbar=data.NavBarItems, footer=data.FooterItems, data=data.ProjectsHeader, projects=data.Projects )

# Test
@views.route('/test')
def test():
    return render_template('routes/projects/projects.html', navbar=data.NavBarItems, footer=data.FooterItems, data=data.ProjectsHeader, projects=data.Projects )