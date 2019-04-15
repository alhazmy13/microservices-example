"""
Logging adapter
---------------
"""
import logging


class Logging(object):
    """
    This is a helper extension, which adjusts logging configuration for the
    application.
    """

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        """
        Common Flask interface to initialize the logging according to the
        application configuration.
        """
        for handler in list(app.logger.handlers):
            app.logger.removeHandler(handler)
        app.logger.propagate = True

        sqla_logger = logging.getLogger('sqlalchemy.engine.base.Engine')
        for hdlr in list(sqla_logger.handlers):
            sqla_logger.removeHandler(hdlr)
        sqla_logger.addHandler(logging.NullHandler())
