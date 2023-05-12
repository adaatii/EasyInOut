from flask import Blueprint, render_template

Home = Blueprint('home', __name__)

@Home.route('/')
@Home.route('/home')
def index():
  return render_template('home.html')
