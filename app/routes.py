from app import db
from app.models import *
from flask import Blueprint, request, jsonify, abort, render_template


blueprint = Blueprint('public', __name__)


@blueprint.route('/', methods=['GET'])
def route():
	return render_template('index.html.j2')