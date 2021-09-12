import os
from decouple import config


class Config(object):
	ROOT = os.path.dirname(os.path.abspath(__file__))
	APP_ROOT = os.path.join(ROOT, 'app')

	SECRET_KEY = config('SECRET_KEY')