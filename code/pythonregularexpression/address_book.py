# -*- coding: utf-8 -*-
"""
Created on Wed May 31 15:38:40 2017

@author: a93701011
"""

#([abc]) - creates a group that contains a set for the letters 'a', 'b', and 'c'. This could be later accessed from the Match object as .group(1)
#(?P<name>[abc]) - creates a named group that contains a set for the letters 'a', 'b', and 'c'. This could later be accessed from the Match object as .group('name').
#.groups() - method to show all of the groups on a Match object.
#re.MULTILINE or re.M - flag to make a pattern regard lines in your text as the beginning or end of a string.
#^ - specifies, in a pattern, the beginning of the string.
#$ - specifies, in a pattern, the end of the string.

import re

direction ="D:/Learning Note/Python/pythoncode/Treehouse/pythonregularexpression/"

name_file = open(direction+"names.txt", encoding = "utf-8")
data = name_file.read()
name_file.close()


line = re.search(r"""
    ^(?P<name>[-\w]*,\s[-\w]+)\t  # Last and first name
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t  # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-?\d{4})?\t  # Phone
    (?P<job>[\w\s]+,\s[\w\s]+)\t? # Job and Company
    (?P<twitter>@[\w\d]+)?$ # Twitter 
""", data, re.VERBOSE|re.MULTILINE)
print(line)
print(line.groupdict()) 

# print email
print(re.findall(r"""
    ^([-\w]*,\s[-\w]+)\t  # Last and first name
    ([-\w\d.+]+@[-\w\d.]+)\t  # Email
    (\(?\d{3}\)?-?\s?\d{3}-?\d{4})?\t  # Phone
    ([\w\s]+,\s[\w\s]+)\t? # Job and Company
    (@[\w\d]+)?$ # Twitter
""", data, re.VERBOSE|re.M))


