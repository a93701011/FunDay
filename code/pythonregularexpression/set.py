# -*- coding: utf-8 -*-
"""
Created on Wed May 31 15:02:27 2017

@author: a93701011
"""

#[abc] - this is a set of the characters 'a', 'b', and 'c'. It'll match any of those characters, in any order, but only once each.
#[a-z], [A-Z], or [a-zA-Z] - ranges that'll match any/all letters in the English alphabet in lowercase, uppercase, or both upper and lowercases.
#[0-9] - range that'll match any number from 0 to 9. You can change the ends to restrict the set.

import re

direction ="D:/Learning Note/Python/pythoncode/Treehouse/pythonregularexpression/"

name_file = open(direction+"names.txt", encoding = "utf-8")
data = name_file.read()
name_file.close()

# print email
print(re.findall(r"[-\w\d+.]+@[-\w\d+.]+", data))
print(re.findall(r"\b[trehous]{9}\b", data, re.I))