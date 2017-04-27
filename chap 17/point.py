class Point(object):
	def __init__(self, x, y):
		self.x, self.y = (x, y)

	def __str__(self):
		return '(%.3f, %.3f)' % (self.x, self.y)

p1 = Point(3, 4)
print p1