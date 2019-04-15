import os


class BaseConfig(object):
    SECRET_KEY = 'this-really-needs-to-be-changed'
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

    TESTING = False

    # Database Configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % (os.path.join(PROJECT_ROOT, "user.db"))
    SQLALCHEMY_ECHO = True

    # Pika Configuration
    FLASK_PIKA_PARAMS = {
        'host': 'rabbitmq-server',
        'username': 'guest',
        'password': 'guest',
        'port': 5672
    }

    # optional pooling params
    FLASK_PIKA_POOL_PARAMS = {
        'pool_size': 8,
        'pool_recycle': 600
    }


class ProductionConfig(BaseConfig):
    pass


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass
