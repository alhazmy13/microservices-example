import json

import pika
from flask import jsonify, Blueprint, request

from app.extenstions.pika.channels import get_queue, Queues

api = Blueprint("users", __name__, url_prefix='/users')


@api.route('/', methods=['POST'])
def create():
    request_body = request.json
    q = get_queue(Queues.user_signup_queue.name)
    q.basic_publish(
        exchange='amq.direct',
        routing_key=Queues.user_signup_queue.name,
        body=json.dumps(request_body),
        properties=pika.BasicProperties(
            delivery_mode=2
        )
    )
    return jsonify({})
