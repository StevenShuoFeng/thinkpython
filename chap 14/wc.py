def linecount(filename):
	c = 0
	for l in open(filename):
		c += 1
	return c

