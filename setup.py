#!/usr/bin/env python
# coding: utf-8
"""
Python JSON-RPC Library Client Server - Setup
 
By Gerold - http://halvar.at/
"""

import os
from setuptools import setup, find_packages

THISDIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(THISDIR)

VERSION = open("version.txt").readline().strip()
HOMEPAGE = "https://github.com/gerold-penz/python-jsonrpc"
DOWNLOAD_BASEURL = "https://github.com/gerold-penz/python-jsonrpc/raw/master/dist/"
DOWNLOAD_URL = DOWNLOAD_BASEURL + "python-jsonrpc-%s.tar.gz" % VERSION


setup(
    name = "python-jsonrpc",
    version = VERSION,
    description = (
        "Python JSON-RPC Client Server Library - Simple To Use Python JSONRPC-Library"
    ),
    long_description = open("README.rst").read(),
    keywords = (
        "JSONRPC, JSON-RPC, JSON, RPC, Client, Server, HTTP-Server, "
        "HTTP-Client, CGI, Remote Procedure Call, JavaScript Object Notation, "
        "CherryPy, Data Interchange, BaseHTTPServer"
    ),
    author = "Gerold Penz",
    author_email = "gerold@halvar.at",
    url = HOMEPAGE,
    download_url = DOWNLOAD_URL,
    packages = find_packages(),
    classifiers = [
        #"Development Status :: 1 - Planning",
        # "Development Status :: 2 - Pre-Alpha",
        # "Development Status :: 3 - Alpha",
        # "Development Status :: 4 - Beta",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Networking",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    install_requires = [
        "munch",
        "cherrypy",
    ],
)

