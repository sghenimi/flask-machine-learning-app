import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TEST = False
    CSRF_ENABLED = True
    SECRET_KEY = "this-really-needs-to-be-changed"
    SQLALCHEMY_DATABASE_URI = os.environ["DBHOST"]

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser = os.envrion["DBUSER"],
    dbpass = os.environ["DBPASS"],
    dbhost = os.environ["DBHOST"],
    dbname = os.environ["DBNAME"]
    )

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(config):
    DEVELOPMENT = True
    DEBUG = True