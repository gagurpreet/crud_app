from flask import render_template, redirect, session
from models.language import all_courses, enroll_course
from services.session_info import current_user

def index():
  courses = all_courses()
  return render_template('languages/index.html', courses=courses, current_user=current_user())

def enroll(id):
  enroll_course(id, session['user_id'])
  return redirect('/')
