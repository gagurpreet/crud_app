from flask import render_template
from models.language import all_languages
from services.session_info import current_user

def index():
  languages = all_languages()
  return render_template('languages/index.html', languages=languages, current_user=current_user)
