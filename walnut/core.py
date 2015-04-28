#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class CpuInfo(object):

    def __init__(self, path='/proc/cpuinfo'):
        self.path = path

    def fileobj(self):
        return open(self.path, 'r')

    def __str__(self):
        with self.fileobj() as f:
            lines = [line.strip() for line in f]
        return '\n'.join(lines)

    def __repr__(self):
        return self.__str__()
    
    def dict(self):
        # inspired and adapted from https://github.com/cfobel/python-cpu_info
        d = {}
        with self.fileobj() as f:
            f = f.read()
            processor_section_matches = [m for m in re.finditer(r'^processor.*:', f, re.MULTILINE)]
            p = processor_section_matches
            processor_section_ranges = [(p[i].start(), p[i + 1].start()) for i in range(len(p) - 1)] + [(p[-1].start(), -1)]
            processor_sections = [f[r[0]:r[1]] for r in processor_section_ranges]
            for s in processor_sections:
                cpu_info = dict([map(str.strip, line.split(':')) for line in s.splitlines() if line.strip()])
                d[cpu_info['processor']] = cpu_info
        return d

    def search(self, regex):
        with self.fileobj() as f:
            matcher = re.compile(regex, re.IGNORECASE)
            match = filter(matcher.match, f)
        return match
