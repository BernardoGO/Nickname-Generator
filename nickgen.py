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
    infile=open(wordsfile, "r")
    for line in infile:

        if line.lower().strip() == word.lower().strip():
            print ("Already Exists")
            return
    else:
        with open(wordsfile, "a") as myfile:
            myfile.write(word.lower())
            print ("ADDED")

def getNick(words, nums, firstCharUpper = False, divideNumber = False, startsWith  = '', endsWith = ''):
    mx = "".rjust(nums, '9')
    randnum = str(random.randint(0, int(mx)))
    underscore = '_' if divideNumber else ''; nick = startsWith

    for x in range(0, words):
        go = False
        _ = ""
        while not go:
            _=getline()
            if len(_) > 1: go = True

        nick += _.title() if firstCharUpper else _

    nick += underscore + randnum + endsWith
    return nick


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-w', action="store", default=2, type=int)
    parser.add_argument('-n', action="store", default=2, type=int)
    parser.add_argument('-d', action="store_true", default=False)
    parser.add_argument('-f', action="store_true", default=False)
    parser.add_argument('-a', action="store", default=False)
    parser.add_argument('-s', action="store", default='')
    parser.add_argument('-e', action="store", default='')

    parsed = parser.parse_args()

    wordcount = parsed.w
    numcount = parsed.n
    firstCharUpper = bool(parsed.f)
    divideNumber = bool(parsed.d)
    newword = (parsed.a)
    startsWith = parsed.s
    endsWith = parsed.e

    if newword:
        addToList("\n"+newword)
    else:

        print (getNick(wordcount, numcount, firstCharUpper, divideNumber, startsWith, endsWith))

