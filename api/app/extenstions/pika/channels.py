from enum import Enum

from flask import g

from app.extenstions import fpika


class Queues(Enum):
    user_signup_queue = "user_signup_queue"
    user_login_queue = "user_login_queue"
    user_get_queue = "user_get_queue"


def get_queue(queue=""):
    if not hasattr(g, queue):
        channel = fpika.channel()
        channel.queue_declare(queue=queue, durable=True)
        channel.queue_bind(exchange='amq.direct', queue=queue)
        g.user_signup_queue = channel
    return g.user_signup_queue
