# -*- coding: utf-8 -*-
# @Time    : 2018-12-18 15:22
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Flask
from app.models.book import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('setting')
    app.config.from_object('secure')
    register_blueprint(app)
    db.init_app(app)
    db.create_all(app=app)
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
