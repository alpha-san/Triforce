#!/usr/bin/python

import sys

def main():
	n = int(sys.argv[1])
	if n < 0:
		n *= -1
		print_negative_triforce(n)
	else:
		print_triforce(n)

def print_triforce(n):
	height = 2 * n
	base = height - 1

	# print the top triangle
	for i in xrange (0, n):
		line = ""
		for j in xrange(0, base - i):
			line += " "
		for k in xrange(0, 1 + (2 * i)):
			line += "*"	
		print(line)
	
	# print the bottom two triangles
	for i in xrange(0, n):
		line = ""
		for j in xrange(0, (base / 2) - i):
			line += " "
		for k in xrange(0, 1 + (2 * i)):
			line += "*"
		for l in xrange(0, base - (2 * i)):
			line += " "
		for m in xrange(0, 1 + (2 * i)):
			line += "*"
		print(line)

def print_negative_triforce(n):
	height = 2 * n
	base = height - 1

	# print the top two trianagles
	for i in xrange(0, n):
		line = ""
		for j in xrange(0, i):
			line += " "
		for k in xrange(0, base - (2 * i)):
			line += "*"
		for l in xrange(0, 1 + (2 * i)):
			line += " "
		for m in xrange(0, base - (2 * i)):
			line += "*"
		print(line)

	# print the bottom triangle
	for i in xrange (0, n):
		line = ""
		for j in xrange(0, n + i):
			line += " "
		for k in xrange(0, base - (2 * i)):
			line += "*"
		print(line)

if __name__== '__main__':
	main()
