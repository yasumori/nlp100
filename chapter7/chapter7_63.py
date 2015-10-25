#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import plyvel

def create_db_63():
    db = plyvel.DB('./db_63', create_if_missing=True)
    for line in open('artist.json'):
        line = json.loads(line.strip())
        name = line['name'].encode('utf-8')
        if 'tags' in line:
            #plyvel does not accept a list as a value
            #tags are converted to str
            tag_str=''
            for tag in line['tags']:
                tag_str += str(tag['count']) + ',' + tag['value'] + ':'
            db.put(name, tag_str.encode('utf-8'))
        else:
            db.put(name, 'NA')
    db.close()

def get_count(artist):
    db = plyvel.DB('./db_63', create_if_missing=True)
    print 'artist: ', artist
    if db.get(artist):
        #It's not a clean solution at all! 
        tag_list = db.get(artist).split(':')
        del tag_list[-1]
        count = sum([int(item.split(',')[0]) for item in tag_list])
        print count
    else:
        print '{0} not in the Database\n'.format(artist)
    db.close()

#create_db_63()
get_count('Oasis')
get_count('Lady Gaga')
get_count('チャットモンチー')
