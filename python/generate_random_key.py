#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
import string


def generate_random_key(bit):
    """ generate random secret key with arbitrary bit length """
    print ''.join([random.choice(string.digits+string.letters) for _ in range(bit)])


if __name__ == '__main__':
    """
        usage: python generate_random_key 32
    """
    import sys
    bit = sys.argv[1]
    generate_random_key(int(bit))
