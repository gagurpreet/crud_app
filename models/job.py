from db.db import sql

def all_jobs():
  return sql(" SELECT * FROM jobs ORDER BY id")

def get_job(id):
  jobs = sql("SELECT * FROM jobs WHERE id = %s", [id])
  return jobs[0]

def create_job(company_name, job_link, job_level):
  sql('INSERT INTO jobs(company_name, job_link, job_level) VALUES(%s, %s, %s) RETURNING *', [company_name, job_link, job_level ])

def update_job(id, company_name, job_link, job_level ):
  sql('UPDATE jobs SET company_name=%s, job_link=%s, job_level=%s  WHERE id=%s RETURNING *',[company_name, job_link, job_level, id])

def delete_job(id):
  sql('DELETE FROM jobs WHERE id=%s RETURNING *', [id])

def like_job(job_id, user_id):
  sql("INSERT INTO likes(user_id, job_id) VALUES(%s, %s) RETURNING *", [user_id, job_id])

def comment_job(job_id, user_id, content):
  sql("INSERT INTO comments(user_id, job_id, content) VALUES(%s, %s, %s) RETURNING *", [user_id, job_id, content])

def get_comment(id):
  comment = sql("SELECT * FROM comments WHERE id = %s", [id])
  return comment[0]

def get_job_by_id(id):
  job = sql("SELECT * FROM jobs WHERE id = %s", [id])
  return job[0]

