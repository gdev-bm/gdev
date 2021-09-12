import os
from decouple import config


class Config(object):
	ROOT = os.path.dirname(os.path.abspath(__file__))
	APP_ROOT = os.path.join(ROOT, 'app')

	SECRET_KEY = config('SECRET_KEY')

	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = config('DATABASE_URL')
	SQLALCHEMY_MIGRATE_REPO = os.path.join(ROOT, 'db_repository')

	REDIS_URL = config('REDIS_URL')
	CELERY_BROKER_URL = REDIS_URL
	CELERY_RESULT_BACKEND = REDIS_URL
	