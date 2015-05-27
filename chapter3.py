#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re

def show_answer(answer):
    for e in answer:
        print e

#20
for line in open("jawiki-country.json"):
    line = json.loads(line, 'utf-8')
    if line['title'] == u'イギリス':
        text=line['text'].encode('utf-8')
 
#21
data=[l for l in text.split('\n')]
answer21=list()
for line in data:
    if re.search(r'Category', line):
        answer21.append(line)

#22
answer22=re.findall(r'Category:[一-龥ぁ-んァ-ンa-zA-Z0-9]+', text)

#23
answer23=list()
for m in re.finditer(r'=+\s?[一-龥ぁ-んァ-ンa-zA-Z0-9]+\s?=+', text):
    level = re.search(r'=+', m.group(0))
    answer23.append((m.group(0), len(level.group(0))-1))

#24
pattern = re.compile(r'((File:|ファイル:)([\w\s]+\.)+\w+)')
answer24=re.findall(pattern, text)
#Could not figure out how to extract only first expressions stored in tuples
answer24=[name[0] for name in answer24]

#25
pattern = re.compile(r'\|[一-龥ぁ-んァ-ンa-zA-Z0-9]+\s=\s.*')
templates=re.findall(pattern, text)
answer25=dict()
for template in templates:
    field, value= template.split(" = ")
    answer25[field.strip('|')]=value

#26
text26=re.sub(r"'''''(.+)'''''", r"\1", text)
text26=re.sub(r"'''(.+)'''", r"\1", text26)
text26=re.sub(r"''(.+)''", r"\1", text26)


#27
text27=re.sub(r"\[\[(.+)#(.+)\|(.+)\]\]", r"\1\2\3", text26)
text27=re.sub(r"\[\[(.+)\|(.+)\]\]", r"\1\2", text27)
text27=re.sub(r"\[\[(.+)\]\]", r"\1", text27)

#28
#Remove more Wiki markup

pattern = re.compile(r'\|[一-龥ぁ-んァ-ンa-zA-Z0-9]+\s=\s.*')
templates=re.findall(pattern, text)
answer28=dict()
for template in templates:
    field, value= template.split(" = ")
    answer28[field.strip('|')]=value

#29    


