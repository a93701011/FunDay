# -*- coding: utf-8 -*-
"""
Created on Wed May 31 14:50:01 2017

@author: a93701011
"""

#\w - matches an Unicode word character. That's any letter, uppercase or lowercase, numbers, and the underscore character. In "new-releases-204", \w would match each of the letters in "new" and "releases" and the numbers 2, 0, and 4. It wouldn't match the hyphens.
#\W - is the opposite to \w and matches anything that isn't an Unicode word character. In "new-releases-204", \W would only match the hyphens.
#\s - matches whitespace, so spaces, tabs, newlines, etc.
#\S - matches everything that isn't whitespace.
#\d - is how we match any number from 0 to 9
#\D - matches anything that isn't a number.
#\b - matches word boundaries. What's a word boundary? It's the edges of word, defined by white space or the edges of the string.
#\B - matches anything that isn't the edges of a word.
#Two other escape characters that we didn't cover in the video are \A and \Z. These match the beginning and the end of the string, respectively. As we'll learn later, though, ^ and $ are more commonly used and usually what you actually want.

import re

direction ="D:/Learning Note/Python/pythoncode/Treehouse/pythonregularexpression/"

name_file = open(direction+"names.txt", encoding = "utf-8")
data = name_file.read()
name_file.close()

#print(re.match(r"Love", data))
#print(re.search(r"Kenneth", data))
print(re.search(r"\w\w\w", data))

def first_number(data):
    return re.search(r"\d",data)

print(first_number(data))
