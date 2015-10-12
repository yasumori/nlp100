#!usr/bin/env python

from stemming.porter2 import stem

f = open("51_out")
out = open("52_out", "w")
for line in f:
    line = line.strip("\n")
    stem_line = stem(line)
    out_str = line + "\t" + stem_line
    out.write(out_str)
    out.write("\n")
