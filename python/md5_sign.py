#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib


def sign(params_dict, key):
    """ md5 sign to a param dict with key [key]"""
    content = '&'.join(['%s=%s' % (key, params_dict[key]) for key in sorted(params_dict.keys())])+key
    return hashlib.new('md5', content).hexdigest()
