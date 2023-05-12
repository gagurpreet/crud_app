from db.db import sql

def all_courses():
  return sql('SELECT * FROM courses ORDER BY id')

def get_course(id):
  courses = sql("SELECT * FROM courses WHERE id = %s", [id])
  return courses[0]