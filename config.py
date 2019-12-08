import os


basedir = os.path.abspath(os.path.dirname(__file__))
instance_dir = os.path.join(basedir, 'instance')


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-nerver-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(instance_dir, 'flaskr.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'development': Config,
    'default': Config
}
