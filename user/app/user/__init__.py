from app.extenstions.pika.channels import Queues


def init_app(app, **kwargs):
    # pylint: disable=unused-argument,unused-variable
    """
    Init users module.
    """
    print("Hola init_app!!")

    from app.extenstions import fpika

    with app.app_context():
        from app.user.resources import signup
        channel = fpika.channel()
        # List of queues

        channel.queue_declare(queue=Queues.user_signup_queue.name, durable=True)

        # List of queues for each function to start consuming on
        channel.basic_consume(signup, queue=Queues.user_signup_queue.name)
        channel.start_consuming()
