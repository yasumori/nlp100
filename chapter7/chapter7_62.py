#!/usr/bin/env python

import plyvel

db = plyvel.DB('./db_60')

i = 0
for k, v in db:
    if v == 'Japan':
        i += 1
print i
db.close()
