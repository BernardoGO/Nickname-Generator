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

def addToList(word):

    for line in infile:
        if line == word.lower():
            print "Already Exists"
            return
    else:
        with open(wordsfile, "a") as myfile:
            myfile.write(word)
            print "ADDED"

def getNick(words, nums, firstCharUpper = False, divideNumber = False):
    mx = "".rjust(nums, '9')
    randnum = str(random.randint(0, int(mx)))
    underscore = '_' if divideNumber else ''; nick = ""

    if firstCharUpper: print getline().title()

    for x in xrange(0, words):
        go = False
        _ = ""
        while not go:
            _=getline()
            if len(_) > 1: go = True

        nick += _.title() if firstCharUpper else _

    nick += underscore + randnum
    return nick


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-w', action="store", default=2, type=int)
    parser.add_argument('-n', action="store", default=2, type=int)
    parser.add_argument('-d', action="store_true", default=False)
    parser.add_argument('-f', action="store_true", default=False)
    parser.add_argument('-a', action="store", default=False)

    parsed = parser.parse_args()

    wordcount = parsed.w
    numcount = parsed.n
    firstCharUpper = bool(parsed.f)
    divideNumber = bool(parsed.d)
    newword = (parsed.a)

    if newword:
        addToList("\n"+newword)
    else:

        print getNick(wordcount, numcount, firstCharUpper, divideNumber)

