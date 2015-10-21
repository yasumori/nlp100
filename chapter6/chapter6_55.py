#!/usr/bin/env python
import xml.etree.ElementTree as ET

tree = ET.parse('nlp.txt.xml')
root = tree.getroot()

def find_person(parent):
    word = ''
    if len(parent.getchildren()) == 0:
        return None
    else:
        for child in parent.getchildren():
            if child.tag == 'word':
                word = child.text
            elif child.tag == 'NER' and child.text == 'PERSON':
                print word
                word = ''
            find_person(child)
find_person(root)

###Old Solution###
'''
for line in open("nlp.txt.xml"):
    if "<word>" in line:
        w = line.lstrip(' ')
        w = w.replace('<word>','')
        w = w.replace('</word>\r\n', '')
    if "<NER>PERSON</NER>" in line:
        print w
'''
