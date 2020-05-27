#Python got drunk and the built-in functions str() and int() are acting odd:
#str(4) ➞ 4
#str("4") ➞ 4
#int("4") ➞ "4"
#int(4) ➞ "4"

#You need to create two functions to substitute str() and int().
# A function called int_to_str() that converts integers into strings
# and a function called str_to_int() that converts strings into integers.

#Notes
#This is meant to illustrate the dangers of using already-existing function names.
#Extra points if you can de-drunk Python.
str, int = int, str

def int_to_str(n):
	return str(n)

def str_to_int(s):
	return int(s)

int_to_str(5)

print("\"%s\"" % int_to_str(5))