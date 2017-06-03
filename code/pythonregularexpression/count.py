# -*- coding: utf-8 -*-
"""
Created on Wed May 31 14:51:16 2017

@author: a93701011
"""
#\w{3} - matches any three word characters in a row.
#\w{,3} - matches 0, 1, 2, or 3 word characters in a row.
#\w{3,} - matches 3 or more word characters in a row. There's no upper limit.
#\w{3, 5} - matches 3, 4, or 5 word characters in a row.
#\w? - matches 0 or 1 word characters.
#\w* - matches 0 or more word characters. Since there is no upper limit, this is, effectively, infinite word characters.
#\w+ - matches 1 or more word characters. Like *, it has no upper limit, but it has to occur at least once.
#.findall(pattern, text, flags) - Finds all non-overlapping occurrences of the pattern in the text.
import re

direction ="D:/Learning Note/Python/pythoncode/Treehouse/pythonregularexpression/"

name_file = open(direction+"names.txt", encoding = "utf-8")
data = name_file.read()
name_file.close()

# print phone number
print(re.findall(r"\(?\d{3}\)? \d{3}-\d{3,5}",data))
# print name
print(re.findall(r"\w*, \w+", data))

def first_number(data):
    return re.search(r"\d",data)

print(first_number(data))

# EXAMPLE:
# >>> find_words(4, "dog, cat, baby, balloon, me")
# ['baby', 'balloon']

def find_words(count, data):
    return re.findall(r"\w"*count+"+", data)

print(find_words(10,data))


