#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
	name = 'walnut',
	version = '0.1',
	url = 'https://github.com/c0ding/walnut',
	download_url = 'https://github.com/c0ding/walnut/archive/master.zip',
	author = 'Martin Simon',
	author_email = 'me@martinsimon.me',
	license = 'Apache v2.0 License',
	packages = ['walnut'],
	description = 'A pythonic library to parse /proc/cpuinfo',
	long_description = file('README.md','r').read(),
	keywords = ['CPU', 'system information', 'cpuinfo', '/proc'],
)
