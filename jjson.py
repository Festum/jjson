#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""Simple JSON query Tool"""

import json
import re

def extract(obj, path, delimiter='.'):
    if type(path) is not unicode:
        raise ValueError('Target path is not a valid string')
    if type(obj) is str:
        obj = json.loads(obj)
    if type(obj) is not dict:
        raise ValueError('Invalid json')
    return parse(obj, path.split(delimiter))

def parse(content, nodes, deep=0):
    if len (content.keys()) > 0:
        for k, v in content.iteritems():
            if k==nodes[deep]:
                if len(nodes)-1 == deep:
                    return v
                if type(v) is dict:
                    return parse(v, nodes, deep+1)
            elif deep > len(nodes)-1:
                break
    return
