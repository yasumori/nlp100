#!usr/bin/env python

for line in open('nlp.txt.xml'):
    if '<word>' in line:
        #remove white spaces
        line = line.lstrip(' ')
        #remove left <word> tag
        line = line.replace('<word>', '')
        #remove right <word> tag
        line = line.replace('</word>\r\n', '')
        print line
