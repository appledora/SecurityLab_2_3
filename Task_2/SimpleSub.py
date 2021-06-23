import time
from collections import Counter
import re
from itertools import tee, islice
import matplotlib.pyplot as plt
alphaMapping1 = {"a": "x", "b": "y", "c": "w", "d": "l", "e": "c", "f": "n", "g": "o", "h": "p", "i": "h", "j": "s", "k": "r", "l": "z",
                 "m": "t", "n": "a", "o": "i", "p": "j", "q": "k", "r": "b", "s": "m", "t": "e", "u": "g", "v": "q", "w": "u", "x": "v", "y": "f", "z": "d", " ": " ", "\n": "\n"}

alphaMapping2 = {"a": "v", "b": "u", "c": "s", "d": "h", "e": "a", "f": "l", "g": "m", "h": "n", "i": "f", "j": "q", "k": "p", "l": "o",
                 "m": "r", "n": "w", "o": "g", "p": "y", "q": "z", "r": "x", "s": "i", "t": "c", "u": "e", "v": "t", "w": "j", "x": "k", "y": "d", "z": "b", " ": " ", "\n": "\n"}


def calculateCharFrequency(str):
    str = str.strip()
    str = " ".join(re.split('\W+', str))
    print(" -------------------------------------------------------------------------------- ")
    print("Character Frequency =>")
    category = Counter(str)
    for key, value in sorted(category.items()):
        print(key, value)

def take_second(elem):
    return elem[1]


def calculateWordDensity(str):
    wordlist = str.split()
    total = len(wordlist)
    print(" -------------------------------------------------------------------------------- ")
    print ("Total Words: ", total)
    print(" -------------------------------------------------------------------------------- ")
    wordfreq = []
    for w in wordlist:
        wordfreq.append(float(wordlist.count(w) * 100) / float(total))
    density = sorted(set(zip(wordlist, wordfreq)),
                     key=take_second, reverse=True)
    print("Top 40 words by frequency density => ")
    count = 0
    for item in density:
        if(count == 40):
            break
        print(item, "% ")
        count += 1


def ngrams(str, n):
    lst = re.findall("\w+", str)
    tlst = lst
    while True:
        a, b = tee(tlst)
        l = tuple(islice(a, n))
        if len(l) == n:
            yield l
            next(b)
            tlst = b
        else:
            break


def getStatistics (textWOspace):
    print("---------------------- S.T.A.T.I.S.T.I.C.S --------------------")
    calculateCharFrequency(textWOspace)
    calculateWordDensity(textWOspace)
    bigrams = Counter(ngrams(textWOspace, 2)).most_common(20)
    print(" -------------------------------------------------------------------------------- ")
    print("Top 20 bigrams sorted by frequency => ")
    for key in bigrams:
        print(key)
    trigrams = Counter(ngrams(textWOspace, 3)).most_common(20)
    print(" -------------------------------------------------------------------------------- ")
    print("Top 20 trigrams sorted by frequency => ")
    for key in trigrams:
        print(key)
    print(" -------------------------------------------------------------------------------- ")

def main():
    objType = input(
        "type 1 for problem 1 and 2 for problem 2. \n")
    print("Type your string below")
    text = ""
    while True:
        dummy = input()+'\n'
        if dummy == '\n':
            break
        text += dummy
    textWOspace = text.replace("\n","")
    getStatistics(textWOspace)
    if (int(objType) == 1):
        alphaMapping = alphaMapping1

    elif (int(objType) == 2):
        alphaMapping = alphaMapping2

    else:
        print("Only select 1 or 2")
        main()

    start_time = time.time()
    print("".join([alphaMapping.get(x, '') for x in text.lower()]))
    print("--- %s seconds ---" % (time.time() - start_time))

    print("Congratulations!")
    print(" -------------------------------------------------------------------------------- ")


if __name__ == "__main__":
    main()
