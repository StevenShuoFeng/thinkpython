import string
import os
from os.path import join, getsize
import subprocess
import wc
import urllib

# for root, dirs, files in os.walk('/Users/Steven/Desktop'):
#     print root, "consumes",
#     print sum(getsize(join(root, name)) for name in files),
#     print "bytes in", len(files), "non-directory files"
#     if 'CVS' in dirs:
#         dirs.remove('CVS')  # don't visit CVS directories


# for root, dirs, files in os.walk('/Users/Steven/Desktop/ebooks papars'):
# 	print files

"""	
Exercise 14.2. Write a function called sed that takes as arguments a pattern string,
 a replacement string, and two filenames; it should read the first file and write the 
 contents into the second file (creating it if necessary). If the pattern string appears anywhere in the file,
  it should be replaced with the replacement string.
"""

def sed(pattern, replacestr, filein, fileout):
	try:
		fin = open(filein, 'r')
		fout = open(fileout, 'w')

		for line in fin:
			line = line.replace(pattern, replacestr)
			fout.write(line)

		fin.close()
		fout.close()

	except:
		print "Something went wrong"


# sed('gif', 'pdf', 'chap14in.txt', 'chap14out.txt')

cmdCopy = 'cp book0.txt /Users/Steven/Desktop'
fp = subprocess.call(cmdCopy, shell=True)
cmdRemove = 'rm /Users/Steven/Desktop/book0.txt'
fp = subprocess.call(cmdRemove, shell=True)

print wc
print wc.linecount('chapter14.py'), 'lines'

# conn = urllib.urlopen('http://thinkpython.com/secret.html')
conn = urllib.urlopen('https://docs.python.org/2/library/urllib.html')
fout = open('parsedoutput.txt', 'w')
for line in conn:
	line = line.strip(string.punctuation+string.whitespace)
	# if 'Example:' in line:
	fout.write(line)
	fout.write("\n")
fout.close()
