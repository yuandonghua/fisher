# -*- coding: utf-8 -*-
# @Time    : 2018-12-18 14:33
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : yushu_book.py
# @Software: PyCharm
from app.libs.httper import Httper
from flask import current_app


class YuShuBook():
    per_page = 15
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)
        else:
            self.total = 0

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = Httper.get(url)
        self.__fill_single(result)

    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'], self.calculate_start(page))
        result = Httper.get(url)
        self.__fill_collection(result)

    def calculate_start(self, page):
        return (page - 1) * current_app.config['PER_PAGE']
