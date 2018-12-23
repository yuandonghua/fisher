# -*- coding: utf-8 -*-
# @Time    : 2018-12-17 18:26
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : httper.py
# @Software: PyCharm
import requests


class Httper():
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)

        if r.status_code == 200:
            return r.json() if return_json else r.text
        return {} if return_json else ''
