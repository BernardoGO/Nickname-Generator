__author__ = 'bernardo'


import linecache
import random

wordsfile = 'wordlist.txt'

getline = lambda x: linecache.getline(wordsfile, x).replace("\n", "")

infile=open(wordsfile, "r")
count=0
for line in infile:
    count=count+1

xs = random.randint(0, count)
print xs
word1 = getline(0)
word2 = getline(random.randint(0, count))


print word1+word2

