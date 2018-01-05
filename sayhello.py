#!/usr/bin/env python
#This simple program asks for user input and then returns it with "Hello" in front
import sys

#User is prompted to input here 
name = sys.stdin.read()

#Program spits out hello plus input
print "Hello " + name + "!"