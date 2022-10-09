#!/usr/bin/env python

"""
distutils/setuptools install script.
"""
import os
import re

from setuptools import find_packages, setup

ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r"""__version__ = ['"]([0-9.]+)['"]""")


requires = []


def get_version():
    init = open(os.path.join(ROOT, "heimdall", "__init__.py")).read()
    return VERSION_RE.search(init).group(1)


setup(
    name="heimdall",
    version=get_version(),
    description="The communication library for whats-init",
    long_description=open("README.md").read(),
    author="Tony Duran",
    url="https://github.com/TonyDuran/whats-init",
    scripts=[],
    packages=find_packages(exclude=["tests*"]),
    package_data={"heimdall": ["data/heimdall/resources/*.json", "examples/*.rst"]},
    include_package_data=True,
    install_requires=requires,
    license="Apache License 2.0",
    python_requires=">= 3.9",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    project_urls={
        "Documentation": "https://github.com/TonyDuran/whats-init",
        "Source": "https://github.com/TonyDuran/whats-init",
    },
)
