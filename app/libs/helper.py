# -*- coding: utf-8 -*-
# @Time    : 2018-12-17 18:15
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : helper.py
# @Software: PyCharm
def is_isbn_or_key(word):
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
