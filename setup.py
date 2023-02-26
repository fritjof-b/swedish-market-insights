# -*- coding: utf-8 -*-
import os

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="insynsregistret",
    version="0.1.0",
    description="Package to scrape the Finansinspektion's registers",
    author="Fritjof Bengtsson",
    url="https://github.com/fritjof-b/insyn",
    packages=find_packages(exclude=("tests", "docs")),
    long_description=read("README.md"),
    license="MIT"
)
