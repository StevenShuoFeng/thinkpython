import copy
from vpython import *

# Exercise 17.7. 
class Kangaroo(object):
	def __init__(self, content = []):
		self.pouch_contents = copy.deepcopy(content)

	def put_in_pouch(self, newObj):
		self.pouch_contents.append(newObj)

	def __str__(self):
		out = ''
		for i in self.pouch_contents:
			out +=  object.__str__(i) + '\n'
		return out

def main():
	kanga = Kangaroo()
	kanga.put_in_pouch('wallet')
	kanga.put_in_pouch('car keys')
	print 'kanga content:'
	print kanga

	roo = Kangaroo(['a'])
	roo.put_in_pouch(123)
	roo.put_in_pouch(roo)

	print 'roo content:'
	print roo

# Exercise 17.8.
def main2():
	scene.range = (256,256,256)
	scene.center = (128,128,128)
	color = (0.1, 0.1, 0.9)
	sphere(pos = scene.center, radius=128, color=color)

# main()
main2()