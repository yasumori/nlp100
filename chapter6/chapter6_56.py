#!/usr/bin/env python

from collections import defaultdict
import xml.etree.ElementTree as ET

class Mention(object):
    def __init__(self, repr_text, sent_id, start, end):
        self.repr_text = repr_text
        self.sent_id = sent_id
        self.start = start
        self.end = end

def extract_info(root):
    '''extracts text and mentions from nlp.txt.xml'''
    text = defaultdict(list)
    sent_id = 1
    mentions = list()
    #text extraction 
    for sent in root.findall(".//sentence"):
        if sent.attrib:
            sent_id = int(sent.attrib['id'])
            for word in sent.findall(".//word"):
                text[sent_id].append(word.text)
    #mention extraction
    for mention in root.findall(".//mention"):
        if mention.attrib:
            repr_text = mention.getchildren()[4].text
        else:
            sent_num = int(mention.getchildren()[0].text)
            start = int(mention.getchildren()[1].text)
            end = int(mention.getchildren()[2].text)
            mentions.append(Mention(repr_text, sent_num, start, end))
    return text, mentions

def text_replacement(text, mentions):
    '''replaces mentions with their representation'''
    for mention in mentions:
        sent_id = mention.sent_id
        start = mention.start
        end = mention.end
         
        sent = text[sent_id]
        #insert the mention representation at the start position
        sent[start-1] = mention.repr_text + ' [mention: ' + sent[start-1]
        #insert the bracket at the end position        
        sent[end-2] = sent[end-2] + ']'
    return text

def main():
    tree = ET.parse('nlp.txt.xml')
    root = tree.getroot()
    text, mentions = extract_info(root)
    return text, mentions
    text = text_replacement(text, mentions)
    for i in xrange(1, len(text)+1):
        print ' '.join(text[i])
