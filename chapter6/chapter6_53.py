#!/usr/bin/env python

import xml.etree.ElementTree as ET

#using xml.etree
tree = ET.parse('nlp.txt.xml')
root = tree.getroot()
#recursive function to find 'word' tags
def find_word(parent):
    #base case, the deepest level of the tree
    if len(parent.getchildren()) == 0:
        return None
    else:
        for child in parent.getchildren():
            #find word tag, print its text
            if child.tag == 'word':
                print child.text
            find_word(child)
find_word(root)
        

###Old solution###
#no use of a library to process the xml file
'''for line in open('nlp.txt.xml'):
    if '<word>' in line:
        #remove white spaces
        line = line.lstrip(' ')
        #remove left <word> tag
        line = line.replace('<word>', '')
        #remove right <word> tag
        line = line.replace('</word>\r\n', '')
        print line'''
