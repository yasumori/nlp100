#!/usr/bin/env python
#-*- coding:utf-8 -*-

from chapter5_41 import sents
from collections import defaultdict


for sent in sents:
    case_chunks=list()
    for chunk in sent:
        for morph in chunk.morphs:
            if morph.pos == '助詞':
                case_chunks.append((chunk, morph.surface))

    case_patterns = defaultdict(list)
    for case_chunk in case_chunks:
        dst = int(case_chunk[0].dst)
        if dst > 0:
            src_chunk = sent[dst]
            for morph in src_chunk.morphs:
                if morph.pos == '動詞':
                    case_patterns[morph.base].append(case_chunk[1])
                    #find the leftmost verb, then break
                    break
    for item in case_patterns.items():
        if len(item[1]) > 1:
            cases = ''
            for case in item[1]:
                text = case + ' '
                cases += text
            print '{0}\t{1}'.format(item[0], cases)
        else:
            print '{0}\t{1}'.format(item[0], item[1][0])

#Unix commands
#uniq -c output_file | sort
#grep 見る output_file | uniq -c | sort
        
            
