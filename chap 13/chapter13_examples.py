import random
import string

def histogram(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0)+1
	return d


def print_hist(h):
	ks = h.keys()
	ks.sort() # sort the keys in alphabetic

	for c in ks:
		print c, ":", h[c]

def reverse_lookup(d, v):
	l = []
	for c in d:
		if d[c] == v:
			l.append(c)
	return l

def invert_dict(d):
	out = dict()
	for k, val in d.iteritems():
		out.setdefault(val, []).append(k)
	return out

def min_max(t):
	return min(t), max(t)

def printall(*args):
	print args
	print len(args)

def sumall(*args):
	out = 0
	for v in args:
		out += v
	return out

def sort_by_length(words):
	l = []
	for w in words:
		l.append((len(w), w))

	l.sort()

	res = []
	for _, w in l:
		res.append(w)
	return res

def sort_by_random_length(words):
	l = []
	for w in words:
		l.append((len(w), random.random(), w))

	l.sort()

	res = []
	for _, _, w in l:
		res.append(w)
	return res

def parse_line(line, hist): # read in a line, parse with all delimiter count word freq 

	line = line.replace('-', ' ')
	for word in line.split():
		word = word.strip(string.punctuation + string.whitespace)
		word = word.lower()
		hist[word] = hist.get(word, 0) + 1

"""
Generate a histgram of the frequency of all words in a book
"""
def book_stat(bookname):

	hist = {}
	fin = open(bookname)
	for line in fin:
		parse_line(line, hist)

	print "Total words in book: ", len(hist)

	return hist
"""
count the total number of words in the book
Get the 'count' most frequently used words.
"""
def top_freq_words(hist, count=10):
	# DSU to sort hist by frequency
	wordFreq = [];
	for w, c in hist.items():
		wordFreq.append((c, w))
	wordFreq.sort(reverse=True)

	print "Most frequent %d words" % count
	rank = 1
	for w, c in wordFreq[0:count]:
		print "rank %d " % rank,
		print w, c 
		rank += 1

"""
Exercise 13.4. Modify the previous program to read a word list (see Section 9.1) and 
then print all the words in the book that are not in the word list. 
How many of them are typos? How many of them are common words that should be in the word list, 
and how many of them are really obscure?
"""
def check_missing_word(hist, wordlist):
	out = []
	for w in wordlist:
		if w not in hist:
			out.append(w)

	print "\nAmong these words: ",
	for i in wordlist:
		print i,

	print "\nMissing from book: ",
	for i in out:
		print i,
	print '\n\n'
	return out


"""
Exercise 13.5. Write a function named that takes a histogram 
as defined in Section 11.1 and returns a random value from the histogram, 
chosen with probability in proportion to frequency

Add count to return more than 1 randomly picked values
"""

def choose_from_hist(hist, count = 1):
	# recover the dictionary into a list
	t = []
	for w, c in hist.items():
		t += [w]*c
	
	out = []
	for i in range(count):
		out += [random.choice(t)]

	return out


"""
Exercise 13.7. This algorithm works, but it is not very efficient; each time you choose a random word,
 it rebuilds the list, which is as big as the original book. 
 An obvious improvement is to build the list once and then make multiple selections, 
 but the list is still big.
1. Use keys to get a list of the words in the book.
2. Build a list that contains the cumulative sum of the word frequencies (see Exercise 10.3). The last item in this list is the total number of words in the book, n.
3. Choose a random number from 1 to n. Use a bisection search (See Exercise 10.11) to find the index where the random number would be inserted in the cumulative sum.
4. Use the index to find the corresponding word in the word list.
"""

def bisect(list, val): # seach for the first element in list >= val assuming list is sorted in acsending order
	l = 0
	r = len(list)-1

	while l < r:
		m = int((l+r)/2)

		if list[m] == val:
			return m

		if list[m] < val:
			l = m+1
		if list[m] > val:
			r = m

	return r


def choose_from_hist_efficient(hist):
	kys = hist.keys()
	kys.sort()

	cumsum = []
	for k in kys:
		if len(cumsum)==0:
			cumsum = [hist[k]]
		else:
			cumsum.append(hist[k]+cumsum[-1])# append with sum of new val and prev last element

	n = cumsum[-1] # total count
	ranInd = random.randint(0, n)

	indInKey = bisect(cumsum, ranInd)
	return kys[indInKey]

# --------------
# Example function 
def example_read_book_chapter13():
	# chapter 13 exercises etc
	bookname = "book0.txt"
	print "Create histogram of the book."
	hist = book_stat(bookname)

	print "\nFind top frequency words."
	top_freq_words(hist)

	# check whether the list of words all showed up in the book
	words_to_check = ['new', 'the', 'in', 'out', 'shuo', 'exist', 'people']
	check_missing_word(hist, words_to_check)

	# randomly pick N words with the original probability of the dictionary
	# verify it by running histogram and rank again
	print "Create a list of words with the orginal probability from book"
	l = choose_from_hist(hist, 3000)

	print "Check frequency ranking of the pseudo random picked words"
	hist_l = histogram(l)
	top_freq_words(hist_l, 5)

	# print "\nUse the efficient (cum sum, bi-search) version of picking a random word with the original probability:"
	# for i in range(10):
	# 	print choose_from_hist_efficient(hist),

	l = ['a', 'a', 'b']
	hist_l = histogram(l)
	for i in range(100):
		print choose_from_hist_efficient(hist_l),


# --------------
# Main function 
example_read_book_chapter13()