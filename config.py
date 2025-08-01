import configparser

config = configparser.ConfigParser()
config.read('config.ini')

flask_config = config['flask']
db_config = config['database']

FLASK_APP = flask_config.get('FLASK_APP', 'app')
FLASK_ENV = flask_config.get('FLASK_ENV', fallback='production')
DEBUG = flask_config.getboolean('DEBUG', fallback=False)

SQLALCHEMY_DATABASE_URI = db_config.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = db_config.get('SQLALCHEMY_TRACK_MODIFICATIONS', fallback=False)
