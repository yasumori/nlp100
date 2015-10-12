#!/usr/bin/env python

import re

f = open('nlp.txt')
texts = list()
for line in f:
    texts.append(line)

pattern = re.compile(r'([.;:?!])(\s[A-Z])')

sents = list()
for text in texts:
    if text == '\n':
        continue
    text = text.strip('\n')
    new_text = re.sub(pattern, '\g<1>EOS\g<2>', text)
    new_sents = new_text.split('EOS ')
    for new_sent in new_sents:
        sents.append(new_sent)

#For output
f = open('50_out', 'w')
for sent in sents:
    f.write(sent)
    f.write('\n')
