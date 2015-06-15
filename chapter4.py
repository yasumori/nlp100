#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib.font_manager
import math


#30
f = open('neko.txt.mecab')
sents=list()
sent=list()
for line in f:
	line = line.strip('\n') 
	if line != 'EOS':
		morphs= dict()
		surface, rest = line.split('\t')
		morphs['surface']=surface
		rest= rest.split(',')
		morphs['pos'] = rest[0]
		morphs['pos1'] = rest[1]
		morphs['base'] = rest[6]
		sent.append(morphs)
	else:
		if sent != []:
                    sents.append(sent)
		    sent=list()
                else:
                    continue

#31
answer31 = list()
for i in xrange(len(sents)):
    for j in xrange(len(sents[i])):
        if sents[i][j]['pos'] == '動詞':
            answer31.append(sents[i][j]['surface'])

#32
answer32 = list()
for i in xrange(len(sents)):
    for j in xrange(len(sents[i])):
        if sents[i][j]['pos'] == '動詞':
            answer32.append(sents[i][j]['base'])

#33
answer33 = list()
for i in xrange(len(sents)):
    for j in xrange(len(sents[i])): 
        if sents[i][j]['pos1'] == 'サ変接続' and sents[i][j]['pos'] == '名詞':
            answer33.append(sents[i][j]['surface'])

#34
answer34=list()
for i in xrange(len(sents)):
    for j in xrange(len(sents[i])):
        #j+1 < len(sents[i]) To avoid an IndexError caused by wrongly assigned EOSs
        if sents[i][j]['surface'] == 'の' and j+1 < len(sents[i]):
            if sents[i][j-1]['pos'] == '名詞' and sents[i][j+1]['pos'] == '名詞':
                answer34.append(sents[i][j-1]['surface']+sents[i][j]['surface']+sents[i][j+1]['surface'])

#35
answer35=list()
longest=0
for i in xrange(len(sents)):
    for j in xrange(len(sents[i])-1):
        #Find an initial sequential noun
        if sents[i][j]['pos']=='名詞' and sents[i][j-1]['pos'] != '名詞':
            seq_noun = list()
            k = 0
            while sents[i][j+k]['pos'] == '名詞':
                seq_noun.append(sents[i][j+k]['surface'])
                k=k+1
                #To avoid IndexError
                if k+j == len(sents[i]):
                    break
            if not len(seq_noun) < longest:
                if len(seq_noun) == longest:
                    answer35.append(seq_noun)
                else:
                    longest=len(seq_noun)
                    answer35=list()
                    answer35.append(seq_noun)          
            

#36
freqs = defaultdict(int)
for i in xrange(len(sents)):
    for j in xrange(len(sents[i])):
        freqs[sents[i][j]['surface']] += 1
answer36 = sorted(freqs.items(), key= lambda x: x[1], reverse=True)

#37
#Get a font for Japanese
font = matplotlib.font_manager.FontProperties(fname="/usr/share/fonts/truetype/fonts-japanese-gothic.ttf")

top10 = answer36[0:10]
words = [w[0] for w in top10]
frequency = [f[1] for f in top10]
nums = [x for x in xrange(len(words))]
#use utf-8 for the words
words=[w.decode('utf-8') for w in words]
plt.bar(nums, frequency, align='center')
plt.xticks(nums, words, fontproperties=font)
plt.show()

#38
word_freqs= defaultdict(int)
for item in answer36:
    #key: frequency, value: the number of words which have a specific frequency
    word_freqs[item[1]] +=1
sorting = sorted(word_freqs.items(), key=lambda x: x[1], reverse=True)
f = [i[0] for i in sorting]
t = [i[1] for i in sorting]
nums = [x for x in xrange(len(sorting))]
plt.bar(nums, t, align='center')
plt.xticks(nums, f)
plt.show()
#Many words in a text appear only once (Zipf's)

#39
rank = list()
freqs39=list()
for i, freq in enumerate(answer36):
    rank.append(math.log(i+1))
    freqs39.append(math.log(freq[1]))
plt.plot(rank, freqs39)
plt.show()

