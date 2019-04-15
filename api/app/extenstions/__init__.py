from app.extenstions.pika import Pika as FPika

fpika = FPika()

from app.extenstions.logging import Logging

logging = Logging()


def init_app(app):
    """
    Application extensions initialization.
    """
    for extension in (
            logging,
            fpika,
    ):
        extension.init_app(app)
