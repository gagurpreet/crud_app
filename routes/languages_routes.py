from flask import Blueprint
from controllers.languages_controller import index

languages_routes = Blueprint('languages_routes', __name__)

languages_routes.route('')(index)