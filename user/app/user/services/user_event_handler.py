import pika
import json

from user.app.extenstions import fpika


def emit_user_profile_update(user):
    exchange_name = 'user_updates'
    routing_key = 'user.profile.update'

    channel = fpika.channel()
    channel.exchange_declare(exchange=exchange_name, exchange_type='topic', durable=True)

    channel.basic_publish(exchange=exchange_name,
                          routing_key=routing_key,
                          body=json.dumps(user),
                          # Delivery mode 2 makes the broker save the message to disk.
                          # This will ensure that the message be restored on reboot even
                          # if RabbitMQ crashes before having forwarded the message.
                          properties=pika.BasicProperties(
                              delivery_mode=2,
                          ))

    print("%r sent to exchange %r with data: %r" % (routing_key, exchange_name, user))
