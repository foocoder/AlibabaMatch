#!/usr/bin/python
#FileName: generatSubmission.py
#Author:   Fuchen Duan
#Email:    slow295185031@gmail.com

try:
    import cPickle as pickle
except ImportError:
    import pickle
import linecache
import re

with open('fm_subCat','rb') as itemRecord:
    conter  = 1;
    writeData = '';
    for eachLine in itemRecord:
        eachCats = eachLine.strip().split(' ');
        eachItemLine = linecache.getline('fm_submissions.txt29',conter);
        eachItem = re.split(' |,',eachItemLine.strip());
        #print str(conter)+' '+str(len(eachCats)) +','+str(len(eachItem));
        writeLine = eachItem[0] + ' ';
        for i in range(1,len(eachCats)):
            if eachCats[i] != eachCats[0]:
                writeLine += eachItem[i] + ',';
        writeLine = re.sub('[ |,]$','\n',writeLine);
        writeData += writeLine;
        conter += 1;
        print str(conter) + " processed!"
with open('fm','wb') as saveFile:
    saveFile.write(writeData);

print "Finished!"
