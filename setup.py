"""
flask-urls
----------

A collection of URL-related functions for Flask applications.

Links
`````

* `documentation <http://sjl.bitbucket.org/flask-urls/>`_
* `development version
  <http://bitbucket.org/sjl/flask-urls/get/tip.gz#egg=flask-urls-dev`_


"""
from setuptools import setup


setup(
    name='flask-urls',
    version='0.9.2',
    url='http://sjl.bitbucket.org/flask-urls/',
    license='MIT',
    author='Steve Losh',
    author_email='steve@stevelosh.com',
    description='A collection of URL-related functions for Flask applications.',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
