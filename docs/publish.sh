#!/usr/bin/env bash

make html
rsync --delete -az _build/html/ ~/src/sjl.bitbucket.org/flask-urls
hg -R ~/src/sjl.bitbucket.org commit -Am 'flask-urls: Update documentation.'
hg -R ~/src/sjl.bitbucket.org push
