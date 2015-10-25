#!/usr/bin/env python
# -*- coding: utf-8 -*-

import plyvel 

db = plyvel.DB('./db_60', create_if_missing=True)

def get_area(artist):
    print 'artist: ', artist
    if db.get(artist):
        print 'area: ', db.get(artist), '\n'
    else:
        print "{0} not in the Database\n".format(artist)

get_area('Oasis')
get_area('Lady Gaga')
get_area('Chatmonchy')
get_area('チャットモンチー')
get_area('Die Ärzte')

db.close()
