from flask import jsonify, Blueprint, request

from app.user.models import User
from app.user.models import db
from app.user.services.user_event_handler import emit_user_profile_update

api = Blueprint("users", __name__, url_prefix='/users')


@api.route('/')
def get():
    # new_name = request.form['full_name']

    # Update the user in the datastore using a local transaction...

    # emit_user_profile_update("", {'full_name': new_name})

    return "This tree has leaves"


@api.route('/', methods=['POST'])
def create():
    form_request = request.form
    user = User(username=form_request['username'],
                email=form_request['email'],
                name=form_request['name'])
    db.session.add(user)
    db.session.commit()

    emit_user_profile_update(user.to_dict())

    return jsonify(user.to_dict())
