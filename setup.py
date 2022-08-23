#!/usr/bin/env python
import os
import re
import sys

from setuptools import setup


def get_version():
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'is_bot', '__init__.py')
    contents = open(filename).read()
    pattern = r"^__version__ = '(.*?)'$"
    return re.search(pattern, contents, re.MULTILINE).group(1)


def get_long_description():
    with open('README.md', mode='r', encoding='utf8') as f:
        return f.read()


if sys.version_info < (3, 7):
    raise RuntimeError('is-bot requires Python 3.7+')


setup(
    name='is_bot',
    author='Roman Snegirev',
    author_email='snegiryev@gmail.com',
    version=get_version(),
    license='Apache 2',
    url='https://github.com/romis2012/is-bot',
    description='Python package to detect bots/crawlers/spiders via user-agent',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    packages=[
        'is_bot',
    ],
    keywords='python bots crawlers web-crawlers user-agent user-agent-parser',
    install_requires=[
        'regex>=2022.8.17',
    ],
)
