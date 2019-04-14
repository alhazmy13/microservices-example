from sqlalchemy import inspect

from user.app.extenstions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR, default='')
    email = db.Column(db.VARCHAR, default='')
    username = db.Column(db.VARCHAR, default='')

    def __repr__(self):
        return '<User %r>' % self.username

    def to_dict(self):
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}
