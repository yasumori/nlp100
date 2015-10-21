#!/usr/bin/env python

import xml.etree.ElementTree as ET
from collections import defaultdict

tree = ET.parse('nlp.txt.xml')
root = tree.getroot()
for dependency in root.findall(".//dependencies"):
    if dependency.attrib['type'] == 'collapsed-dependencies':
        nsubjs=list()
        dobjs=list()
        for dep in dependency.findall(".//dep"):
            if dep.attrib['type'] == 'nsubj':
                nsubjs.append(dep.getchildren())
            elif dep.attrib['type'] == 'dobj':
                dobjs.append(dep.getchildren())
        for sub_gov, sub_dep in nsubjs:
            for dob_gov, dob_dep in dobjs:
                #look for a predicate
                if sub_gov.text == dob_gov.text:
                    print sub_dep.text+'\t'+sub_gov.text+'\t'+dob_dep.text
                 
