#!/usr/bin/env python
#-*- coding:utf-8 -*-

from chapter5_41 import sents

#Perhaps, very memory inefficient...

for sent in sents:
    for chunk in sent:
        dst = chunk.dst
        if dst > 0:
            dst_text = ''
            chunk_postags = [morph.pos for morph in chunk.morphs]
            if '名詞' in chunk_postags:
                for morph in chunk.morphs:
                    if morph.pos != '記号':
                        dst_text += morph.surface
	    src_chunk = sent[int(dst)]
            src_chunk_postags = [morph.pos for morph in src_chunk.morphs]
            src_text =''
            if '動詞' in src_chunk_postags:
                for morph in src_chunk.morphs:
                    if morph.pos != '記号':
	                src_text += morph.surface
        if dst_text != '' and src_text != '':
            print '{0}\t{1}'.format(dst_text, src_text)
