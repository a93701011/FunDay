# -*- coding: utf-8 -*-
"""
Created on Mon May 29 23:38:19 2017

@author: a93701011
"""
import re

direction ="D:/Learning Note/Python/pythoncode/Treehouse/pythonregularexpression/"

name_file = open(direction+"names.txt", encoding = "utf-8")
data = name_file.read()
name_file.close()

#print(re.match(r"Love", data))
#print(re.search(r"Kenneth", data))
