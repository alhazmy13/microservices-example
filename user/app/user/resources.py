import json

from flask import jsonify

from app.user.models import User
from app.user.models import db


def signup(ch, method, properties, body):
    print("Hola signup!!")
    try:
        print(body)
        print("body")
        user_form = json.loads(body.decode('UTF-8'))
        user = User(username=user_form['username'],
                    email=user_form['email'],
                    name=user_form['name'])

        db.session.add(user)
        db.session.commit()

        ch.basic_ack(delivery_tag=method.delivery_tag)
        return jsonify(user.to_dict())
    except Exception as ex:
        print("Exception")
        print(ex)
