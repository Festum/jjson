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
    if delimiter: # delimiter = None for parse basename only
        path = path.split(delimiter)
    return parse(obj, path)

def parse(content, nodes, deep=0):
    out = ''
    if len (content.keys()) > 0:
        for k, v in content.iteritems():
            if type(nodes) is list:
                if k==nodes[deep]:
                    if len(nodes)-1 == deep:
                        return v
                    if type(v) is dict:
                        return parse(v, nodes, deep+1)
                elif deep > len(nodes)-1:
                    break
            else:
                if k==nodes:
                    out = v
                if type(v) is dict:
                    return parse(v, nodes, deep+1)
    return out

def flatten(content, key='', out={}):
    for k, v in content.iteritems():
        if type(v) is dict:
            out.update(flatten(v, '{}{}'.format(key+'/' if key else '',k)))
        else:
            if type(v) is list:
                v = ', '.join(str(e) for e in v)
            out['{}{}'.format(key+'/' if key else '',k)] = v
    return out
