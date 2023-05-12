from flask import Blueprint
from controllers.languages_controller import index, enroll

languages_routes = Blueprint('languages_routes', __name__)

languages_routes.route('')(index)
languages_routes.route('/<id>/enroll',methods=["POST"] )(enroll)
