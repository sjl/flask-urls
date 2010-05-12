Welcome to flask-urls' documentation!
=====================================

flask-urls is a collection of useful URL-related functions for `Flask`_
applications.

.. _Flask: http://flask.pocoo.org/

Installation
------------

Install flask-urls with `pip`_::

    pip install -e 'hg+http://bitbucket.org/sjl/flask-urls@v0.9.0#egg=flask-urls'

Prefer `git`_ to `Mercurial`_?

::

    pip install -e 'git+http://github.com/sjl/flask-urls.git@v0.9.0#egg=flask-urls'

.. _pip: http://pip.openplans.org/
.. _git: http://git-scm.com/
.. _Mercurial: http://hg-scm.org/

Usage
-----

flask-urls currently provides one function to make dealing with URLs in Flask
applications a bit easier.

permalink
_________

The ``permalink`` decorator was taken from `this snippet`_ on the Flask site.
It's used to wrap functions so they only need to return the arguments to
Flask's ``url_for`` function, instead of calling the function themselves.

.. _this snippet: http://flask.pocoo.org/snippets/6/

For example, say you have several classes that represents items on your site::

    from flask import url_for
    
    class Event(object):
        def __init__(self, event_id):
            self.event_id = event_id
    
        def link(self):
            return url_for('event', event_id=self.event_id)
    
    class User(object):
        def __init__(self, username):
            self.username = username
    
        def link(self):
            return url_for('profile', username=self.username)

Using the permalink decorator can make the ``link`` functions a bit cleaner::

    from flaskext.urls import permalink
    
    class Event(object):
        def __init__(self, event_id):
            self.event_id = event_id
    
        @permalink
        def link(self):
            return 'event', { 'event_id': self.event_id }
    
    class User(object):
        def __init__(self, username):
            self.username = username
    
        @permalink
        def link(self):
            return 'profile', { 'username': self.username }

Contribute
----------

If you want to contribute feel free to fork the `Mercurial repository`_ or `git
repository`_ and send a pull request.

.. _Mercurial repository: http://bitbucket.org/sjl/flask-urls/
.. _git repository: http://github.com/sjl/flask-urls/
