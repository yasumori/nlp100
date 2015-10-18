#!usr/bin/env python

import xml.etree.ElementTree as ET

tree = ET.parse('nlp.txt.xml')
root = tree.getroot()

def find_tags(parent):
    tags = list()
    if len(parent.getchildren()) == 0:
        return None
    else:
        for child in parent.getchildren():
            if child.tag == 'word':
                tags.append(child.text)
            elif child.tag == 'lemma':
                tags.append(child.text)
            elif child.tag == 'POS':
                tags.append(child.text)
                print '\t'.join(tags)
            find_tags(child)
find_tags(root)
###Old Solution###
'''
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
'''
