from flask import render_template
from models.language import all_courses
from services.session_info import current_user

def index():
  courses = all_courses()
  return render_template('languages/index.html', courses=courses, current_user=current_user())
