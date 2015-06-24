#!/usr/bin/env python
#-*- coding:utf-8 -*-

#Three possible operations
#See *, then make a new chunk, and add it to a sent
#See EOS, then add a sent to sents and make a new sent
#See neither * nor EOS, make a morph and add it to a chunk

#dst: dependency direction (which morpheme the current morpheme depends on)
#srcs: from which morpheme dependency coming (can be more than 1)

#sents[sent[chunk[morph...morph],..., chunk[morph...morph]] ,...]

from collections import defaultdict
from chapter5_40 import Morph


class Chunk(object):
    def __init__(self, dst, morphs =None, srcs= None):
        self.dst = dst
        self.morphs = list()
        self.srcs = list()


f = open('../neko.txt.cabocha')

sents=list()
sent=list()
srcs_indexes=defaultdict(list)

current_chunk = -1
for line in f:
    line = line.strip('\n') 
    if line != 'EOS' and not line.startswith('*'):
	surface, rest = line.split('\t')
	sur = surface
	rest= rest.split(',')
	pos = rest[0]
	pos1 = rest[1]
	base=rest[6]
	morph = Morph(sur, base, pos, pos1)
	sent[current_chunk].morphs.append(morph)
    elif line.startswith('*'):
        current_chunk += 1
        dependency = line.split(' ')
	dst = dependency[2].strip('D')
        chunk = Chunk(dst)
        
        srcs_indexes[dst].append(dependency[1])
        
        if dependency[1] in srcs_indexes:
            chunk.srcs = srcs_indexes[dependency[1]]    
        
        sent.append(chunk)
    else:
	if sent != []:
            sents.append(sent)
	    sent=list()
            srcs_indexes=defaultdict(list)
            current_chunk = -1
        else:
            continue

#8th sentence
for chunk in sents[7]:
    dst = chunk.dst
    text = ''
    for morph in chunk.morphs:
        text += morph.surface
    print '文字列: ',text, '| 係り先: ', dst
