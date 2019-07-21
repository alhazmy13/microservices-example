class BaseConfig(object):
    SECRET_KEY = 'this-really-needs-to-be-changed'

    # Pika Configuration
    FLASK_PIKA_PARAMS = {
        'host': 'localhost',
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
