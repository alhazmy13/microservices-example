from flask import jsonify, Blueprint

api = Blueprint("users", __name__, url_prefix='/users')


@api.route('/')
def get():
    return "This tree has leaves"


@api.route('/', methods=['POST'])
def create():
    return jsonify({})
