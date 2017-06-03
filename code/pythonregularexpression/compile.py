# -*- coding: utf-8 -*-
"""
Created on Wed May 31 19:00:02 2017

@author: a93701011
"""
#re.compile(pattern, flags) - method to pre-compile and save a regular expression pattern, and any associated flags, for later use.
#.groupdict() - method to generate a dictionary from a Match object's groups. The keys will be the group names. The values will be the results of the patterns in the group.
#re.finditer() - method to generate an iterable from the non-overlapping matches of a regular expression. Very handy for for loops.
#.group() - method to access the content of a group. 0 or none is the entire match. 1 through how ever many groups you have will get that group. Or use a group's name to get it if you're using named groups.
import re

direction ="D:/Learning Note/Python/pythoncode/Treehouse/pythonregularexpression/"

name_file = open(direction+"names.txt", encoding = "utf-8")
data = name_file.read()
name_file.close()


line = re.compile(r"""
    ^(?P<name>(?P<first>[-\w]*),\s(?P<last>[-\w]+))\t  # Last and first name
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t  # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-?\d{4})?\t  # Phone
    (?P<job>[\w\s]+,\s[\w\s]+)\t? # Job and Company
    (?P<twitter>@[\w\d]+)?$ # Twitter 
""", re.VERBOSE|re.MULTILINE)

print(re.search(line, data).groupdict()) 
print(line.search(data).groupdict())

for match in line.finditer(data):
    print(match.group("name"))
    print("{first} {last} <{email}>".format(**match.groupdict()))

