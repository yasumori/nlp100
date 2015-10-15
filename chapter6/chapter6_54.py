#!usr/bin/env python

w = list()
for line in open('nlp.txt.xml'): 
    if len(w) < 3:
        if '<word>' in line:
            word = line.lstrip(' ')
            word = word.replace('<word>', '')
            word = word.replace('</word>\r\n', '')
            w.append(word)
        elif '<lemma>' in line:
            lemma = line.lstrip(' ')
            lemma = lemma.replace('<lemma>', '')
            lemma = lemma.replace('</lemma>\r\n', '')
            w.append(lemma)
        elif '<POS>' in line:
            pos = line.lstrip(' ')
            pos = pos.replace('<POS>', '')
            pos = pos.replace('</POS>\r\n', '')
            w.append(pos)
    else:
        print '\t'.join(w)
        w = list()

