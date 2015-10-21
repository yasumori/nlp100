#!/usr/bin/env python

import xml.etree.ElementTree as ET

#test sentence: sent_id2 in nlp.txt.xml
sent2 = '(ROOT (S (PP (IN As) (NP (JJ such))) (, ,) (NP (NN NLP)) (VP (VBZ is) (ADJP (VBN related) (PP (TO to) (NP (NP (DT the) (NN area)) (PP (IN of) (NP (JJ humani-computer) (NN interaction))))))) (. .)))'

###This answer is not correct###
#when sent2 is processed, one of the NPs should be "humani-computer interaction"
#However, its actual output is "of humani-computer interaction"
#Removing "of" from this NP, while keeping "of" to produce a longer NP, "the area of humani-computer interaction" is needed.

def get_NPs(exp):
    stack = list()
    temp = list()
    nest = list()
    NP_counter = 0
    for c in exp:
        if c == '(':
            symbol = ''
        elif c not in ['(', ')', ' ']:
            symbol += c
        elif c == ' ':
            if symbol:
                stack.append(symbol)
                #collect non-terminals if NP_counter > 0
                if symbol == 'NP':
                    NP_counter += 1
            symbol = ''
        elif c == ')':
            #avoid appending an empty symbol to temp
            if NP_counter > 0 and symbol:
                temp.append(symbol)
            symbol = ''
            top = stack.pop() 
            if top == 'NP':
                #print non-nested np
                if len(temp) != 0: 
                    print ' '.join(temp)
                NP_counter -= 1
                #nest is not over 
                if NP_counter != 0:
                    nest.append(' '.join(temp))
                    temp = list()
                #nest is over, print nest
                else:
                    if nest:
                        print ' '.join(nest)
                    nest = list()
                    temp = list()


def main():
    tree = ET.parse('nlp.txt.xml')
    root = tree.getroot()
    for parse in root.findall(".//parse"):
        s = parse.text
        get_NPs(s)
        print '\n'

if __name__=='__main__':
    main()
