from .. import db


class World(db.Model):
	__table__name = 'World'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
