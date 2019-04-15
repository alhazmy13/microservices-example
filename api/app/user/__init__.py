def init_app(app, **kwargs):
    from app.user import route  # pylint: disable=unused-variable
    app.register_blueprint(route.api)
