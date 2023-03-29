#!/usr/bin/env python

from setuptools import setup

VERSION = "0.1.2"

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="tap-exchangeratehost",
    version=VERSION,
    description="Singer.io tap for extracting currency exchange rate data from the exchangerate.host API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Daigo Tanaka, Anelen Co., LLC",
    url="http://github.com/anelendata/tap-exchangeratehost",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",

        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",

        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    install_requires=[
        "singer-python>=5.3.0",
        "requests>=2.23.0",
    ],
    entry_points="""
    [console_scripts]
    tap-exchangeratehost=tap_exchangeratehost:main
    """,
    packages=["tap_exchangeratehost"],
    package_data={
        # Use MANIFEST.ini
    },
    include_package_data=True
)
