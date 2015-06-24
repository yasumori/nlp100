#!/usr/bin/env python
#-*- coding:utf-8 -*-

from chapter5_41 import sents

for sent in sents:
    for chunk in sent:
        dst = chunk.dst
        if dst > 0:
            dst_text = ''
            for morph in chunk.morphs:
                if morph.pos != '記号':
                    dst_text += morph.surface
	    src_chunk = sent[int(dst)]
	    src_text =''
	    for morph in src_chunk.morphs:
                if morph.pos != '記号':
	            src_text += morph.surface
        print '{0}\t{1}'.format(dst_text, src_text)
