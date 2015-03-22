#!/usr/bin/env python
# -*- coding: utf-8 -*-

__title__ = 'walnut'
__version__ = '0.1a'
__author__ = 'Martin Simon <me@martinsimon.me>'
__repo__ = 'https://github.com/c0ding/walnut'
__license__ = 'Apache v2.0 License'

class CPUInfo(object):

	def __init__(self, path='/proc/cpuinfo'):
		self.path = path

	def __str__(self):
		with open(self.get_path(), 'r') as f:
			lines = [line.strip() for line in f]
			return '\n'.join(lines)

	def __repr__(self):
		return self.__str__()

	def get_path(self):
		return self.path
	
	def dict(self):
		d = {}
		with open(self.get_path(), 'r') as f:
			d = {k: v for line in f for (k, v) in (line.strip().split(None, 1),)}
		return d

	def search(self, input):
		with open(self.get_path(), 'r') as f:
			match = [s for s in f if input in s]
			# will have to figure out a way to make this case insensitive.
			# mem.search('Swap') and mem.search('swap') should both match.
			return match
