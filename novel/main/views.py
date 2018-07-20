# -*- coding: utf-8 -*-
"""
    novel.views
    -----------

    novel website basic views
    :copyright: (c) 2018-07-20 by buglan
"""

from . import main


@main.route('/')
def index():
    return 'Hello, World'
