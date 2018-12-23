# -*- coding: utf-8 -*-
# @Time    : 2018-12-18 15:23
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : book.py
# @Software: PyCharm
from flask import jsonify, request

from app.forms.book import SearchForm
from app.view_models.book import BookViewModel, BookColloction
from . import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
import json


@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    books = BookColloction()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        return json.dumps(books, default=lambda o: o.__dict__)
        # return jsonify(books)

    else:
        return jsonify(form.errors)
