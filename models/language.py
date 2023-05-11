from db.db import sql

def all_languages():
  return sql('SELECT * FROM languages ORDER BY id')