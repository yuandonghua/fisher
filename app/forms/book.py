# -*- coding: utf-8 -*-
# @Time    : 2018-12-18 17:51
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : book.py
# @Software: PyCharm
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
