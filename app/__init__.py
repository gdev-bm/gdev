import os
import datetime
from config import Config
# from werkzeug.contrib.fixers import ProxyFix
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from jinja2 import select_autoescape


db = SQLAlchemy()
migrate = Migrate()


def create_app(cfg=Config):
	application = Flask(__name__)#, template_folder='dist')
	application.config.from_object(cfg)

	init_app(application)
	db.init_app(application)
	migrate.init_app(application, db)

	# application.wsgi_app = ProxyFix(application.wsgi_app, num_proxies=1)
	
	from app.routes import blueprint
	application.register_blueprint(blueprint)

	ICONS = {}
	ICON_DIR = os.path.join(cfg.APP_ROOT, 'static', 'icons')
	for file in os.listdir(ICON_DIR):
		if file.endswith('svg'):
			key = '.'.join(file.split('.')[:-1])
			with open(os.path.join(ICON_DIR, file)) as f:
				ICONS[key] = f.read()

	application.jinja_env.globals.update(
		icon=lambda key: ICONS[key]
	)
	application.jinja_env.autoescape = select_autoescape(
		default_for_string=True,
		default=True
	)

	return application


def init_app(app):
	@app.shell_context_processor
	def shell_context():
		return { 'app': app, 'db': db }

	@app.context_processor
	def inject_variables():
		return {
			'now': datetime.datetime.utcnow()
		}

	@app.after_request
	def after_request(response):
		return response


from app.models import *
