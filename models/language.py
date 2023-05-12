from db.db import sql

def all_courses():
  return sql('SELECT * FROM courses ORDER BY id')

def get_course(id):
  courses = sql("SELECT * FROM courses WHERE id = %s", [id])
  return courses[0]

def enroll_course(course_id, user_id):
  sql("INSERT INTO likes(user_id, food_id) VALUES(%s, %s) RETURNING *", [user_id, course_id])
