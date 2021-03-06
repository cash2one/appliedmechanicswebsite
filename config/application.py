# -*- coding: utf-8 -*-
import os

AVAILABLE_CONFIGS = {
    'production': 'config.application.ProductionConfig',
    'development': 'config.application.DevelopmentConfig',
    'test': 'config.application.TestConfig'
}
DEFAULT_CONFIG = 'development'


class Config(object):
    _basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = False
    ASSETS_LOAD_PATH = [
        os.path.join(_basedir, 'app', 'assets'),
        os.path.join(_basedir, 'vendor', 'assets')
    ]
    ASSETS_DIRECTORY = (
        os.path.join(_basedir, 'app', 'static', 'assets')
    )
    ASSETS_URL = '/static/assets'
    LESS_EXTRA_ARGS = [
        '--no-color',
        '--include-path=%s' % os.path.join(_basedir, 'vendor', 'assets')
    ]
    # The current non-release version of webassets supports LESS_PATHS
    # LESS_PATHS = os.path.join(_basedir, 'vendor', 'assets')


class DevelopmentConfig(Config):
    SECRET_KEY = 'devkey'
    DEBUG = True
    ASSETS_DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        'sqlite:///%s' %
        os.path.join(Config._basedir, 'db', 'appmechanics.db')
    )


class TestConfig(Config):
    SECRET_KEY = 'testkey'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ASESTS_AUTO_BUILD = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
