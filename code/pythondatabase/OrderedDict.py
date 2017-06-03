# -*- coding: utf-8 -*-
"""
Created on Mon May 29 16:14:15 2017

@author: a93701011
"""

#! usr/bin/env python3

from collections import OrderedDict 

menu = OrderedDict([
        ("a","aa"),
        ("b","bb")
    ])

for key, value in menu.items():
    print("{}) {}".format(key, value))