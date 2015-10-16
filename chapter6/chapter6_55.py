#!usr/bin/env python

for line in open("nlp.txt.xml"):
    if "<word>" in line:
        w = line.lstrip(' ')
        w = w.replace('<word>','')
        w = w.replace('</word>\r\n', '')
    if "<NER>PERSON</NER>" in line:
        print w
