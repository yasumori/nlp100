#!/usr/bin/env python
# -*- coding: utf-8 -*-

import plyvel 
import json

db = plyvel.DB('./db_60', create_if_missing=True)
for line in open('artist.json'):
    line = json.loads(line.strip())
    name = line['name'].encode('utf-8')
    if 'area' in line:
        area = line['area'].encode('utf-8')
    else:
        area = 'NA'.encode('utf-8')
    db.put(name, area)
db.close()
