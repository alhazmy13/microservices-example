from app.extenstions.flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from sqlalchemy_utils import force_auto_coercion, force_instant_defaults

force_auto_coercion()
force_instant_defaults()

from flask_marshmallow import Marshmallow

marshmallow = Marshmallow()

from app.extenstions.pika import Pika as FPika

fpika = FPika()


from app.extenstions.logging import Logging

logging = Logging()


def init_app(app):
    """
    Application extensions initialization.
    """
    for extension in (
            db,
            marshmallow,
            fpika,
    ):
        extension.init_app(app)

    with app.app_context():
        # your code here
        db.create_all()
