import string
import random

"""
Exercise 13.8. Markov analysis:
"""

prefix = () # buffer of the current prefix
prefix_to_suffixprefix_map = {}
wordCount = 0

def skip_gutenberg_header(fp):
    # Reads from fp until it finds the line that ends the header.

    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


def process_line(line, prefixLen = 2):
	line.replace('-', ' ')

	global prefix
	global wordCount

	for word in line.split():
		wordCount += 1
		word = word.strip(string.whitespace)

		# for initialization of prefix
		if len(prefix) < prefixLen:
			prefix += (word,)
			return

		# update dictionary
		try:
			prefix_to_suffixprefix_map[prefix].append(word)
		except KeyError:
			prefix_to_suffixprefix_map[prefix] = [word]

		# update prefix buffer
		prefix = prefix[1:] + (word,)


def read_file(bookname):
	fin = open(bookname)

	# skip_gutenberg_header(fin)
	for line in fin:
		process_line(line, 2)

	print "Total prefix : ", len(prefix_to_suffixprefix_map),  " from total %d words " % wordCount


def random_text(nlen = 100):
	start = random.choice(prefix_to_suffixprefix_map.keys())

	for i in range(nlen):
		t = prefix_to_suffixprefix_map.get(start, None)

		if t == None:
			random_text(n-i)
			return

		word = random.choice(t)
		print word,
		start = start[1:] + (word,)



def example_markov_analysis():
	read_file("markov_analysis.txt")
	read_file("structshape.txt")
	random_text(1500)

example_markov_analysis()