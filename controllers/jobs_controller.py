from flask import render_template, redirect, request, session
from models.job import all_jobs, get_job, create_job,update_job, delete_job, like_job, comment_job, get_comment, get_job_by_id
from services.session_info import current_user

def index():
  jobs = all_jobs()
  return render_template('jobs/index.html', jobs=jobs, current_user=current_user())

def new():
  return render_template('jobs/new.html')

def create():
  company_name = request.form.get('company_name')
  job_link = request.form.get('job_link')
  job_level = request.form.get('job_level')
  create_job(company_name, job_link, job_level)
  return redirect('/')

def edit(id):
  job = get_job(id)
  return render_template('jobs/edit.html', job=job)

def update(id):
  company_name = request.form.get('company_name')
  job_link = request.form.get('job_link')
  job_level = request.form.get('job_level')
  update_job(id, company_name, job_link, job_level )
  return redirect('/')

def delete(id):
  delete_job(id)
  return redirect('/')

def like(id):
  like_job(id, session['user_id'])
  return redirect('/')

def comment(id):
  content = request.form.get('content')
  comment_job(id, session['user_id'], content)
  return redirect('/')

def more(id):
  comment = get_comment(id)
  job = get_job_by_id(id)
  return render_template('jobs/more.html', comment=comment, current_user=current_user(), job= job)
  

