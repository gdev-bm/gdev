from app import db
import datetime

"""
class Model(db.Model):
	__tablename__ = 'model'


	id = db.Column(db.Integer, primary_key=True)

	entity_id = db.Column(db.Integer, db.ForeignKey('entity.id'), nullable=False)
	entity = db.relationship('Entity', back_populates='model')

	def __repr__(self):
		return f'<Model #{self.id}>'

	def serialize():
		return {
			'id': self.id
		}
"""