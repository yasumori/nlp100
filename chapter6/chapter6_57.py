#!/usr/bin/env python

import xml.etree.ElementTree as ET
from collections import defaultdict
import pydot

def collect_dependencies():
    tree = ET.parse('nlp.txt.xml')
    root = tree.getroot()
    sent_id = 1
    dependencies = defaultdict(list)
    for sent in root.findall(".//sentence"):
        if sent.attrib:
            sent_id = int(sent.attrib['id'])
            for depen in sent.findall(".//dependencies"):
                if depen.attrib['type'] == 'collapsed-dependencies':
                    for dep in depen.findall(".//dep"):
                        governor, dependent = dep.getchildren()
                        dependencies[sent_id].append((governor.text, dependent.text))
    return dependencies 

def generate_dotfile(dependencies, sent_id):
    f_name = 'sent' + str(sent_id) + '.dot'
    f = open(f_name, 'w')
    line = 'digraph ' + 'sent' + str(sent_id) + ' {\n'
    f.write(line)

    for item in dependencies[sent_id]:
        govern = item[0]
        depen = item[1]
        if '-' in [govern, depen]:
            line = '"' + govern + '"' + ' -> ' + '"'+ depen + '"' + ';\n'
        else:
            line = govern + ' -> ' + depen + ';\n'
        f.write(line)
    f.write('}')
    f.close()

def main(sent_id = 1):
    dependencies = collect_dependencies()
    generate_dotfile(dependencies, sent_id)
    out_dot = 'sent' + str(sent_id) + '.dot'
    out_graph = 'sent'+str(sent_id)+'graph.png'
    graph = pydot.graph_from_dot_file(out_dot)
    graph.write(out_graph, prog='dot', format='png')
         
