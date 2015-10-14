#!/usr/bin/python
#FileName: processItem2CatId.py
#Author:   Fuchen Duan
#Email:    slow295185031@gmail.com

try:
    import cPickle as pickle
except ImportError:
    import pickle
import sys
import re

with open('item_cat.pkl','rb') as openPkl:
    dataMap = pickle.load(openPkl);
with open(sys.argv[1],'rb') as openFile:
    writeData = '';
    for eachLine in openFile:
        eachItem = re.split(sys.argv[2],eachLine.strip());
        writeLine = '';
        for element in eachItem:
            writeLine += dataMap[element]+' ';
        writeData += writeLine + '\n';
with open(sys.argv[1]+"CatId",'wb') as saveFile:
    saveFile.write(writeData);
print "Finished!"

