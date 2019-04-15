def init_app(app, **kwargs):
    # pylint: disable=unused-argument,unused-variable
    """
    Init users module.
    """

    # Touch underlying modules
    from app.user import models, resources  # pylint: disable=unused-variable
    app.register_blueprint(resources.api)
