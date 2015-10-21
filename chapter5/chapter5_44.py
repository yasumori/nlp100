#!/usr/bin/env python
#-*- coding:utf-8 -*-

from chapter5_41 import sents

import pydot

def convert(sent, out_name):
    f_name = out_name + '.dot'
    f = open(f_name, 'w')
    line = 'digraph ' + out_name + ' {\n'
    f.write(line)
    
    for chunk in sent:
        dst = int(chunk.dst)
        if dst > 0:
            dst_text = ''
            for morph in chunk.morphs:
                dst_text+=morph.surface
            src_chunk = sent[dst]
            src_text = ''
            for morph in src_chunk.morphs:
                src_text += morph.surface
            line = dst_text + ' -> ' + src_text + ';\n'
            f.write(line)
    f.write('}')
    f.close()

sent8 = sents[7]
convert(sent8, 'sent8')
graph = pydot.graph_from_dot_file('sent8.dot')
graph.write('graph.png', prog='dot', format='png')
