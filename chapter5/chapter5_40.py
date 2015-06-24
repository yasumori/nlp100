#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Morph(object):
    def __init__(self, surface, base, pos, pos1):
	self.surface = surface
	self.base = base
	self.pos = pos
	self.pos1 = pos1


f = open('../neko.txt.cabocha')
sents=list()
sent=list()
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
		sent.append(morph)
	elif line.startswith('*'):
		continue
	else:
		if sent != []:
                    sents.append(sent)
		    sent=list()
                else:
                    continue

#Morphs in the third sentence 
print sents[2]
