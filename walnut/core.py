#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

__title__ = 'walnut'
__version__ = '0.1'
__author__ = 'Martin Simon <me@martinsimon.me>'
__repo__ = 'https://github.com/c0ding/walnut'
__license__ = 'Apache v2.0 License'

class CpuInfo(object):

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
		# inspired and adapted from https://github.com/cfobel/python-cpu_info
		d = {}
		with open(self.get_path(), 'r') as f:
			f = f.read()
			processor_section_matches = [m for m in re.finditer(r'^processor.*:', f, re.MULTILINE)]
			p = processor_section_matches
			processor_section_ranges = [(p[i].start(), p[i + 1].start()) for i in range(len(p) - 1)] + [(p[-1].start(), -1)]
			processor_sections = [f[r[0]:r[1]] for r in processor_section_ranges]
			for s in processor_sections:
				cpu_info = dict([map(str.strip, line.split(':')) for line in s.splitlines() if line.strip()])
				d[cpu_info['processor']] = cpu_info
		return d

	def search(self, user_inp):
		with open(self.get_path(), 'r') as f:
			matcher = re.compile(user_inp, re.IGNORECASE)
			match = filter(matcher.match, f)
		return match
