class Point(object):
	def __init__(self, x, y):
		self.x, self.y = (x, y)

	def __str__(self):
		return '(%.3f, %.3f)' % (self.x, self.y)

	def add_point(self, other):
		return Point(self.x+other.x, self.y+other.y)

	def add_tuple(self, t):
		return Point(self.x+t[0], self.y+t[1])

	# Exercise 17.5.
	def __add__(self, p2):
		if isinstance(p2, Point):
			return self.add_point(p2)
		elif isinstance(p2, tuple):
			return self.add_tuple(p2)

		elif isinstance(p2, int): # made this up to add same constant to x and y to make sum() work
			return self.add_tuple((p2, p2))
		else:
			raise ValError , 'only addable to another Point obj or Tuple'

	def __radd__(self, other):
		return self.__add__(other)

def print_attributes(obj):
	for attr in obj.__dict__:
		print attr, getattr(obj, attr)

p1 = Point(3, 4)
print 'p1 : ', p1

p2= Point(1, 2)
print 'p1 + Point p2 (1, 2)', p1 + p2

print 'p1 + tuple (5, 5)', p1 + (5,5)

print 'sum([p1,p1,p2,p2]) : ', sum([p1,p1,p2,p2])

print 'p2 attributes: ', p2.__dict__

print_attributes(p2)