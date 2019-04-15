from app.extenstions.pika import Pika as FPika

fpika = FPika()


def init_app(app):
    """
    Application extensions initialization.
    """
    for extension in (
            fpika,
    ):
        extension.init_app(app)
