# -*- coding: utf-8 -*-
"""
Created on Wed May 31 23:04:00 2017

@author: a93701011
"""

import re

direction ="D:/Learning Note/Python/pythoncode/Treehouse/pythonregularexpression/"

name_file = open(direction+"address.txt", encoding = "utf-8")
data = name_file.read()
name_file.close()

print(re.match(r"""
               ^([-\w]*,\s[-\w]+),\s
                ([\w\d+]*@[\w\d.]+),\s
                (\d{3}-\d{3}-\d{4}),\s
                (@[\w\d]+)$ # Twitter
                """,data, re.X|re.M))

print(re.findall(r"""
                (@[\w\d]+)$ # Twitter
 """, data, re.X|re.M))