import os
import datetime
from config import Config
from flask import Flask, request, redirect
from jinja2 import select_autoescape


def create_app(cfg=Config):
	application = Flask(__name__)#, template_folder='dist')
	application.config.from_object(cfg)

	init_app(application)

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
		return { 'app': app }

	@app.before_request
	def before_request():
		if not request.is_secure:
			url = request.url.replace('http://', 'https://', 1)
			code = 301
			return redirect(url, code=code)


	@app.context_processor
	def inject_variables():
		return {
			'now': datetime.datetime.utcnow()
		}

	@app.after_request
	def after_request(response):
		return response
