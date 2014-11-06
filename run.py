__author__ = 'bernardo'


import linecache
import random
import argparse

wordsfile = 'wordlist.txt'

getline = lambda: linecache.getline(wordsfile, random.randint(1, count)).replace("\n", "")

infile=open(wordsfile, "r")
count=0
for line in infile:
    count=count+1

parser = argparse.ArgumentParser()
parser.add_argument('-w', action="store", default=2, type=int)
parser.add_argument('-n', action="store", default=2, type=int)
parsed = parser.parse_args()

wordcount = parsed.w
numcount = parsed.n
mx = "".rjust(numcount, '9')

randnum = str(random.randint(0, int(mx)))

nick = ""

for x in xrange(0, wordcount):
    nick += getline()

nick += randnum


print nick

