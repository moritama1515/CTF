# -*- coding: utf-8 -*-
import sys
import re
import string

print "Please enter the string."
print "=================================="
line = raw_input()
print "=================================="
s_line = line.lower()

tlines = s_line.translate(string.maketrans("abcdefghij","0123456789"))
tlines = list(tlines)

for i,tline in enumerate(tlines):
    if tlines[i] == "k":
        tlines[i] = "10"
    elif tlines[i] == "l":
        tlines[i] = "11"
    elif tlines[i] == "m":
        tlines[i] = "12"
    elif tlines[i] == "n":
        tlines[i] = "13"
    elif tlines[i] == "o":
        tlines[i] = "14"
    elif tlines[i] == "p":
        tlines[i] = "15"
    elif tlines[i] == "q":
        tlines[i] = "16"
    elif tlines[i] == "r":
        tlines[i] = "17"
    elif tlines[i] == "s":
        tlines[i] = "18"
    elif tlines[i] == "t":
        tlines[i] = "19"
    elif tlines[i] == "u":
        tlines[i] = "20"
    elif tlines[i] == "v":
        tlines[i] = "21"
    elif tlines[i] == "w":
        tlines[i] = "22"
    elif tlines[i] == "x":
        tlines[i] = "23"
    elif tlines[i] == "y":
        tlines[i] = "24"
    elif tlines[i] == "z":
        tlines[i] = "25"
    elif tlines[i] == "_":
        tlines[i] = "26"
    elif tlines[i] == "{":
        tlines[i] = "27"
    elif tlines[i] == "}":
        tlines[i] = "28"
    elif tlines[i] == ".":
        tlines[i] = "29"
    elif tlines[i] == "?":
        tlines[i] = "30"
    elif tlines[i] == "!":
        tlines[i] = "31"

#print tlines

print "How much move?"
move = raw_input()

def input_dir():
    print "left? or right?(l/r)"
    global dir
    inp_dir = raw_input()
    dir = direction(inp_dir)

def direction(dir):
    if dir == "r":
        dir = move
        dir = int(dir)
    elif dir =="l":
        dir = move
        dir = -int(dir)
    else:
        print dir
        input_dir()
    return dir

input_dir()        

if dir > 0:
    strage = 25-dir
else:
    strage = 25+dir

schar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','_','{','}','.','?','!']

for i,tline in enumerate(tlines):
    num = int(tlines[i])
    s_num = 25-num

    if num > 25:
        tlines[i] = schar[num]
    elif dir > 0 and s_num < move:
        num -= (strage+1)
        tlines[i] = schar[num]
    else:
        num += dir
        tlines[i] = schar[num]

char = "".join(tlines)
print "=================================="
print char
print "=================================="
