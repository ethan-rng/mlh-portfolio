from flask import Blueprint, render_template, request
import data

views = Blueprint('views', __name__, template_folder='templates')


# Hero Page
@views.route('/')
def hero():
    return render_template('hero.html')

# About Me
@views.route('/aboutme')
def about_me():
    return render_template('routes/aboutme/about_me.html', navbar=data.NavBarItems, footer=data.FooterItems)


# Blogs
@views.route('/hobbies')
def blog():
    return render_template('routes/hobbies/hobbies.html', navbar=data.NavBarItems, footer=data.FooterItems, data=data.HobbyHeader)

@views.route('/hobbies/<int:post_id>')
def blog_post(post_id):
    return render_template('routes/hobbies/hobby.html', navbar=data.NavBarItems, footer=data.FooterItems, id=post_id)


# Projects
@views.route('/projects')
def project():
    return render_template('routes/projects/projects.html', navbar=data.NavBarItems, footer=data.FooterItems, data=data.ProjectsHeader)

@views.route('/projects/<int:project_id>')
def project_post(project_id):
    return render_template('routes/projects/project.html', navbar=data.NavBarItems, footer=data.FooterItems, id=project_id)

# Experience
@views.route('/experience')
def experience():
    return render_template('routes/experience/experience.html', work_experiences=data.WorkExperience)


