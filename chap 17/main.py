

def int_to_time(sec):
    t = Time()
    t.minute, t.second = divmod(sec, 60)
    t.hour, t.minute = divmod(t.minute, 60)
    return t

class Time(object):
	def __init__(self, hour = 0, minute = 0, second = 0):
		self.hour, self.minute, self.second = (hour, minute, second)

	def __str__(self):
		return '%2d:%2d:%2d' % (self.hour, self.minute, self.second)

	def __add__(self, other):
		s = self.time_to_int() + other.time_to_int()
		return int_to_time(s)

	# Exercise 18.1.
	def __cmp__(self, other):
		tself = (self.hour, self.minute, self.second)
		tother = (other.hour, other.minute, other.second)
		return cmp(tself, tother)

	def print_time(self):
		print '%2d:%2d:%2d' % (self.hour, self.minute, self.second)

	def time_to_int(self):
		return self.hour*60*60 + self.minute*60 + self.second

	def increment(self, secs):
		secs += self.time_to_int()
		return int_to_time(secs)

	def is_after(self, t2):
		return self.time_to_int() > t2.time_to_int()


t1 = Time(9, 54, 39)
t2 = t1.increment(60*3)

print "t1 : ", t1
print "t2 : ", t2

print t1.is_after(t2)
print t2.is_after(t1)

print 't1+t2 = ', t1+t2
