#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import random as rand
from sets import Set

#00
stressed = "stressed"
reverse = stressed[::-1]
print reverse

#01
pata = u"パタトクカシーー"
new_pata = ""
for i in range(len(pata)):
	if i % 2 == 0:
		new_pata += pata[i]
print new_pata

#02
pata2 = u"パトカー"
taku = u"タクシー"
new_pata2 = "".join([p + t for (p, t) in zip(pata2, taku)])
print new_pata2

#03
sent3 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words3 = sent3.split(" ")
counts3 = list()
for word in words3:
	word = word.replace(",", "")
	word = word.replace(".", "")
	counts3.append(len(word))
print counts3

#04
sents4 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words4 = sents4.split(" ")
nums4 = [1, 5, 6, 7, 8, 9, 15, 16, 19]
elements = dict()
for n, word in enumerate(words4):
	if n+1 in nums4:
		elements[word[0]] = n+1
	else:
		elements[word[:2]] = n+1
#print sorted(elements.items(), key= lambda x: x[1])
print elements

#05
def make_ngram(seq, n):
	ngrams = list()
	for i in xrange(len(seq)-(n-1)):
		ngram = seq[i:i+n]
		ngrams.append(ngram)
	return ngrams

out5_1= make_ngram("I am an NLPer", 2)
print out5_1
out5_2=make_ngram("I am an NLPer".split(" "), 2)
print out5_2

#06
bigrams6_1 = make_ngram("paraparaparadise", 2)
bigrams6_2 = make_ngram("paragraph", 2)

X6 = Set(bigrams6_1)
Y6 = Set(bigrams6_2)
union6 = X6 | Y6
intersection6 = X6 & Y6
difference6 = X6 - Y6

print "union :", union6
print "intersection :", intersection6
print "difference :", difference6

if "se" in X6:
	print "se is in X"
else:
	print "se is not in X"

if "se" in Y6:
	print "se is in Y"
else:
	print "se is not in Y"

#07
def weather(x, y, z):
	print u"{0}時の{1}は{2}".format(x, y, z)
weather(12, u"気温", 22.4)


#08
def cipher(charas):
	encoded = ""
	for c in charas:
		if c in string.lowercase:
			encoded += chr(219 - ord(c))
		else:
			encoded += c
	return encoded
message8= cipher("I love seals.")
print message8

def typoglycemia(words):
	words = words.split(" ")
	typogly = ""
	for word in words:
		if len(word) >= 5:
			middle = word[1:len(word)-1]
			middle = [c for c in middle]
			for i in xrange(10):
				i1 = rand.randint(0, len(middle)-1)
				i2 = rand.randint(0, len(middle)-1)
				middle[i1], middle[i2] = middle[i2], middle[i1]
			middle = "".join(middle)
			print middle
			shuff = word[0] + middle + word[len(word)-1] + " "
			typogly += shuff
		else:
			word = word + " "
			typogly += word
	return typogly
example8 ="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
output8 = typoglycemia(example8)
print output8



