from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Optional, Email
from wtforms.fields.html5 import EmailField

class ContactForm(FlaskForm):
	name = StringField('name', validators=[ Optional() ], default='')
	email = EmailField('email', validators=[ Email(), Optional() ], default='')
	interest = SelectField('interest', choices=[ 'website', 'app', 'enterprise', 'design', 'other' ], default='')
	message = StringField('message', validators=[ Optional() ], default='')