#!venv/bin/python3
# -*- coding:utf8 -*-

import os
from flask import logging
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'pandoo'
    SQLALCHEMY_DATABASE_URI = os.getenv('WINDBLOG_DB_URI') or 'sqlite:///'+os.path.join(basedir, 'blog.db')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    WINDBLOG_POSTS_PER_PAGE = os.getenv('WINDBLOG_POSTS_PER_PAGE') or 10
    WINDBLOG_ADMIN_PASSWORD = os.getenv('WINDBLOG_ADMIN_PASSWORD') or 'panda'
    WINDBLOG_UPLOAD_FOLDER = os.getenv('WINDBLOG_UPLOAD_FOLDER') or 'upload_files'
    WINDBLOG_DOWNLOAD_PROXY_FOLDER = os.getenv('WINDBLOG_DOWNLOAD_PROXY_FOLDER') or 'download_proxy_files'
    WINDBLOG_MAX_FILE_LENGTH = os.getenv('WINDBLOG_MAX_FILE_LENGTH') or 100
    LOG_LEVEL = logging.DEBUG

    SUBJECTS = [
        ('technique', '技术'),
        ('environment', '环境'),
        ('resources', '资源'),
        ('thoughts', '思考')
    ]

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False

    @classmethod
    def init_app(cls, app):
        Config.init_app()
        #concrete error process
        pass


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
