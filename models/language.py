from db.db import sql

def all_languages():
  return sql('SELECT * FROM languages ORDER BY id')

def get_language(id):
  languages = sql("SELECT * FROM languages WHERE id = %s", [id])
  return languages[0]