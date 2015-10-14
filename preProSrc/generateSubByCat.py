#!usr/bin/python
#FileName: generateSubByCat.py
#Author:   Fuchen Duan
#Email:    slow295185031@gmail.com

try:
    import cPickle as pickle
except ImportError:
    import pickle
import re
import sys
with open(sys.argv[1],'rb') as boolFile:
    boolTab = [i.strip().split(' ') for i in boolFile];
with open(sys.argv[2],'rb') as openFile:
    openTab = [re.split(' |,|;',i.strip()) for i in openFile];
writeLine = '';
for x in range(len(boolTab)):
    for y in range(len(boolTab[x])):
        if boolTab[x][y] == '1' and y == 0:
            writeLine += openTab[x][y]+' ';
        elif boolTab[x][y] == '1' and y!=len(boolTab[x])-1:
            writeLine += openTab[x][y]+',';
        elif boolTab[x][y] == '1' and y==len(boolTab[x])-1:
            writeLine += openTab[x][y]+'\n';
    print x;
with open('fm_submission','wb') as writeFile:
    writeFile.write(writeLine);
