#!/usr/bin/env python
#-*- coding:utf-8 -*-

from chapter5_41 import sents
from collections import defaultdict

#Output of this programme doesnt match with the example.
#Collecting too many　case particles...
'''* 0 1D 1/1 0.857869
　	記号,空白,*,*,*,*,　,　,　
別段	副詞,助詞類接続,*,*,*,*,別段,ベツダン,ベツダン
* 1 2D 0/2 2.294919
くる	動詞,自立,*,*,カ変・クル,基本形,くる,クル,クル
に	助詞,格助詞,一般,*,*,*,に,ニ,ニ
も	助詞,係助詞,*,*,*,*,も,モ,モ
* 2 6D 0/3 -1.816825
及ば	動詞,自立,*,*,五段・バ行,未然形,及ぶ,オヨバ,オヨバ
ん	助動詞,*,*,*,不変化型,基本形,ん,ン,ン
さ	助詞,終助詞,*,*,*,*,さ,サ,サ
と	助詞,格助詞,引用,*,*,*,と,ト,ト
、	記号,読点,*,*,*,*,、,、,、
* 3 6D 0/1 -1.816825
主人	名詞,一般,*,*,*,*,主人,シュジン,シュジン
は	助詞,係助詞,*,*,*,*,は,ハ,ワ
* 4 6D 0/1 -1.816825
手紙	名詞,一般,*,*,*,*,手紙,テガミ,テガミ
に	助詞,格助詞,一般,*,*,*,に,ニ,ニ
* 5 6D 0/1 -1.816825
返事	名詞,サ変接続,*,*,*,*,返事,ヘンジ,ヘンジ
を	助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
* 6 -1D 0/0 0.000000
する	動詞,自立,*,*,サ変・スル,基本形,する,スル,スル
。	記号,句点,*,*,*,*,。,。,。
EOS'''

for sent in sents:
    noun_wo_candidates = defaultdict(list)
    other_cases_candidates = defaultdict(list)
    for chunk in sent:
        morphs = chunk.morphs
        for i in xrange(len(morphs)):
            if morphs[i].pos1 == 'サ変接続':
                if i+1 <= len(morphs)-1 and morphs[i+1].surface == 'を':
                    noun_wo_candidates[chunk].append((morphs[i].surface + morphs[i+1].surface))
                    
            if morphs[i].pos == '助詞' and morphs[i].surface != 'を':
                other_cases_candidates[chunk].append(morphs[i].surface)
                    
    noun_wo_verbs =list()
    other_cases = defaultdict(list)
    for key_chunk in noun_wo_candidates.keys():
    	dst = int(key_chunk.dst)
    	src_chunk = sent[dst]
    	for src_morph in src_chunk.morphs:
            if src_morph.pos == '動詞':
                noun_wo_verbs.append(noun_wo_candidates[key_chunk][0] + src_morph.base)
    for key_chunk in other_cases_candidates.keys():
        dst = int(key_chunk.dst)
        src_chunk = sent[dst]
        for src_morph in src_chunk.morphs:
            if src_morph.pos == '動詞':
                other_cases[key_chunk] = other_cases_candidates[key_chunk]
    
    cases = list()
    for value in other_cases.values():
        for v in value:
            cases.append(v)
    chunks = list()
    for key in other_cases.keys():
        chunks.append(key)

    #Decompose chunks into words
    words = list()
    for chunk in chunks:
        morphs = chunk.morphs
        word = ''
        for morph in morphs:
            word += morph.surface
        words.append(word)
    
    for i, noun_wo_verb in enumerate(noun_wo_verbs):
        if i == 0:
          print "{0}\t{1}\t{2}".format(noun_wo_verbs[0], ' '.join(cases), ' '.join(words))
        else:
          print noun_wo_verbs[i]

##Unix commands
#cut -f 1 chapter5_47.out | uniq -c | sort
#cut -f 1-2 chapter5_47.out | uniq -c | sort

