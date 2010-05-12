# -*- coding: utf-8 -*-
"""
    flaskext.urls
    ~~~~~~~~~~~~~

    A collection of URL-related functions for Flask applications.

    :copyright: (c) 2010 by Steve Losh.
    :license: MIT, see LICENSE for more details.
"""

from flask import url_for
from werkzeug.routing import BuildError

def permalink(function):
    def inner(*args, **kwargs):
        endpoint, values = function(*args, **kwargs)
        try:
            return url_for(endpoint, **values)
        except BuildError:
            return
    return inner


