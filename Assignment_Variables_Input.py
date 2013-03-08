#!/usr/bin/env python2

# Non-Programmer's Tutorial for Python 2.6/Who Goes There?
# http://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_2.6/Who_Goes_There%3F#Input_and_Variables

__author__ = 'chris'
__version__ = '0.3'

number = int ( raw_input ( "Type in an integer: " ) )
text = str ( raw_input ( "Type in a string: " ) )
print "Your number is", number
print "Number is of", type ( number )
print "Number * 2 =", number * 2
print "The string you entered is", text
print "text is of", type ( text )
print "text * 2 =", text * 2