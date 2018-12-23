# -*- coding: utf-8 -*-
# @Time    : 2018-12-18 16:08
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : __init__.py
# @Software: PyCharm
from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import book
