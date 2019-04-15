def init_app(app, **kwargs):
    from app.user import resources  # pylint: disable=unused-variable
    app.register_blueprint(resources.api)
