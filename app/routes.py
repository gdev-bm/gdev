from app.forms import ContactForm
from flask import Blueprint, request, jsonify, abort, render_template, send_from_directory


blueprint = Blueprint('public', __name__)


@blueprint.route('/', methods=['GET', 'POST'])
def route():
	form = ContactForm()

	if form.validate_on_submit():
		print(form.name.data)

	return render_template('index.html.j2', form=form)


@blueprint.route('/mars', methods=['GET'])
def mars():
	print("MARS HERE")
	return send_from_directory('static/mars-game/public', 'index.html')

