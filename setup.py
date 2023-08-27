#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup
from bigquery_orm import __version__


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="bigquery-orm",
    version=__version__,
    author="Fernando Celmer",
    author_email="email@fernandocelmer.com",
    description="BigQuery ORM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FernandoCelmer/python-bigquery-orm",
    classifiers=[
        'Development Status :: 4 - Beta',
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    packages=['bigquery_orm'],
    include_package_data=True,
    install_requires=[
        'google-auth==2.22.0',
        'google-cloud-bigquery==3.11.4'
    ],
    python_requires=">=3.6",
    zip_safe=True,
    fullname='bigquery-orm',
)
