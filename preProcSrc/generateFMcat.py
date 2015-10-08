#!/usr/bin/python
#FileName: generateFMcat.py
#Author:   Fuchen Duan
#Email:    slow295185031@gmail.com

try:
    import cPickle as pickle
except ImportError:
    import pickle
import re

with open('all_item_cat_map.pkl','rb') as mapPkl:
    dataMap = pickle.load(mapPkl);

with open('fm_submissions.txt','rb') as openFile:
    with open('fm_subCat','wb') as saveFile:
        conter  = 0;
        writeData = '';
        for eachLine in openFile:
            eachItems = re.split(' |,',eachLine.strip());
            for eachElements in eachItems:
                writeData += dataMap[eachElements] + ' ';
            writeData += '\n';
            conter += 1;
            print str(conter)+" processed!"
        saveFile.write(writeData);

print "Finished!"
