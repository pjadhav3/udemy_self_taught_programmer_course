'''
Assignment 8: practice regular expression
'''

Write a regular expression that matches the word Dutch in The Zen of Python.

* Dutch *

re.findall('*\sDutch\s*',zen_of_text,re.ignorecase)

Come up with a regular expression that matches all the digits in the string Arizona 479, 501, 870. California 209, 213, 650.

re.findall('\d',zen_of_text,re.ignorecase)