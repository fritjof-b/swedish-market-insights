# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name="insynsregistret",
    version="0.1.0",
    description="Package to scrape the Finansinspektion's registers",
    author="Fritjof Bengtsson",
    url="https://github.com/fritjof-b/insyn",
    packages=find_packages(exclude=("tests", "docs")),
)
