# -*- coding: utf-8 -*-
# @Time    : 2018-12-17 16:22
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : fisher.py
# @Software: PyCharm
from flask import Flask

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], threaded=True)
