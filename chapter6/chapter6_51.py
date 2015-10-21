#!/usr/bin/env python 

f = open("50_out")
out = open("51_out", "w")
for line in f:
    line = line.strip("\n")
    words = line.split(" ")
    for i in xrange(len(words)):
        out.write(words[i])
        out.write("\n")
    out.write("\n") 
