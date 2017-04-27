import math

class Point(object):
	""" Newbioh """

def print_point(p):
	print "(%f, %f)" % (p.x, p.y)

"""
Exercise 15.1. Write a function called that takes two Points as ar- guments and returns the distance between them.
"""
def distance_between_points(p1, p2):
	return math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)

def main():
	print Point
	blank = Point()
	print blank
	blank.x = 3.0
	blank.y = 4.0
	blank.z = 5.0
	print_point(blank)

	p1 = Point()
	p2 = Point()
	p1.x = 3
	p1.y = 4
	p2.x = 0
	p2.y = 0
	print "\nDistance between :"
	print_point(p1)
	print_point(p2)
	print " is ", distance_between_points(p1, p2)
 

main()