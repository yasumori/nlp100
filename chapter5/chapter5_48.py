#!/usr/bin/env python
#-*- coding:utf-8 -*-

from chapter5_41 import sents
#test
sents = [sents[5]]

def get_root(chunk, sent, path):
    #Recursive function looking for a root

    #Append surface forms of current chunk
    morphs = chunk.morphs
    chunk_str = ''
    for morph in morphs:
        if morph.pos != '記号':
            chunk_str += morph.surface
    path.append(chunk_str)        
    
    #Find the next chunk
    dst = int(chunk.dst)
    src_chunk = sent[dst]
    
    #Base case: root. Append a surface form of root and return a path
    if int(src_chunk.dst) == -1:
        src_morphs = src_chunk.morphs
        src_str = ''
        for src_morph in src_morphs:
            if src_morph.pos != '記号':
                src_str += src_morph.surface
        path.append(src_str)          
        return path
    #Recursion with src_chunk
    else:
        return get_root(src_chunk, sent, path)

for sent in sents:
    for chunk in sent:
        morphs = chunk.morphs
        path = list()
        for morph in morphs:
            if morph.pos == '名詞':
                full_path = get_root(chunk, sent, path)
                break
        if len(path) != 0:
            print ' -> '.join(path)
