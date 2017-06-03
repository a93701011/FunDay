# -*- coding: utf-8 -*-
"""
Created on Wed May 31 15:21:38 2017

@author: a93701011
"""
#
#[^abc] - a set that will not match, and, in fact, exclude, the letters 'a', 'b', and 'c'.
#re.IGNORECASE or re.I - flag to make a search case-insensitive. re.match('A', 'apple', re.I) would find the 'a' in 'apple'.
#re.VERBOSE or re.X - flag that allows regular expressions to span multiple lines and contain (ignored) whitespace and comments.

                                                                                              
import re

direction ="D:/Learning Note/Python/pythoncode/Treehouse/pythonregularexpression/"

name_file = open(direction+"names.txt", encoding = "utf-8")
data = name_file.read()
name_file.close()

# print email
print(re.findall(r"""
    \b@[-\w\d.]* # fisrt was a word boundary, an @, and anynumber of character
    [^gov\t]+ # Ignore 1+ instances of the letters'g','o','v' and a tab
    \b # another word boundary
""", data, re.VERBOSE))
print(re.findall(r"\b[trehous]{9}\b", data, re.I))