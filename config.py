class Configuration(object):
    CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///simulator.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_SECRET_KEY = 'lalala'

