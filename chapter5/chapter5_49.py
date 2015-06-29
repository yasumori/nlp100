#!/usr/bin/env python
#-*- coding:utf-8 -*-

from chapter5_41 import sents

'''もっと綺麗なコードになるはず……'''

#For testing
sents = [sents[5]]

def root_path(chunk, sent, path):
    #Recursive function finding a path to the root
    chunk_postags = [morph.pos for morph in chunk.morphs]
    chunk_surface = [morph.surface for morph in chunk.morphs]
    
    path.append((chunk, chunk_postags, chunk_surface))

    dst = int(chunk.dst)
    src_chunk = sent[dst]
    if dst > 0:
        return root_path(src_chunk, sent, path)
    else:
        return path


for sent in sents:
    for i, chunk in enumerate(sent):
        for morph in chunk.morphs:
            if morph.pos == '名詞':
                path = list()
                path = root_path(chunk, sent, path)
                i_chunks = [item[0] for item in path]
                i_postags = [item[1] for item in path]
                #If there is another noun in i_chunks, that should be processed later.
                n_nouns = 0
                for postag in i_postags:
                    if '名詞' in postag:
                        n_nouns +=1
                if n_nouns < 2:                
                    #pattern1: i and j share k
                    for j in xrange(i+1, len(sent)):
                        for morph_j in sent[j].morphs:
                            if morph_j.pos == '名詞':
                                path_j = list()
                                path_j = root_path(sent[j], sent, path_j)
                                j_chunks = [item[0] for item in path_j]
                                pattern1=list()
                                for k in xrange(j+1, len(sent)):
                                    if sent[k] in i_chunks and sent[k] in j_chunks:
                                        for n, item in enumerate(path):
                                            if item[0] == sent[k]:
                                                pattern1.append(' | ')
                                            elif n == 0:
                                                noun_index = item[1].index('名詞')
                                                item[2][noun_index]='X'
                                                pattern1.append(''.join(item[2]))
                                            else:
                                                pattern1.append(' -> '.join(item[2]))
                                                pattern1.append(''.join(item[2]))

                                        for n, item in enumerate(path_j):
                                            if item[0] == sent[k]:
                                                pattern1.append(' | ')
                                            elif n == 0:
                                                noun_index = item[1].index('名詞')
                                                item[2][noun_index]='X'
                                                pattern1.append(''.join(item[2]))
                                            else:
                                                pattern1.append(' -> '.join(item[2]))
                                                pattern1.append(''.join(item[2]))
                                        pattern1.append(''.join([morph.surface for morph in sent[k].morphs]))
                                        print ''.join(pattern1)

                #pattern2: path from i to j
                pattern2 = list()
                for n, item in enumerate(path):
                    if n == 0:
                        noun_index = item[1].index('名詞')
                        item[2][noun_index] = 'X'
                        pattern2.append(''.join(item[2]))
                    elif n!=0 and '名詞' in item[1]:
                        tmp = 'Y'
                        tmp_pattern = list(pattern2)
                        tmp_pattern.append(''.join(tmp))
                        print ' -> '.join(tmp_pattern)
                        pattern2.append(''.join(item[2]))
                    else:
                        pattern2.append(''.join(item[2]))
                    
                
                
