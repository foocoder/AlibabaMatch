#!/usr/bin/python
#Filename: PMdatarepair.py
#Author:   Fuchen Duan

try:
    import cPickle as pickle
except ImportError:
    import pickle
import sys


with open(sys.argv[1],'rb') as pickleFile:
    dataMap = pickle.load(pickleFile);
with open(sys.argv[2],'rb') as data:
    lineCounter = 1;
    writeData = '';
    data.readline();
    for eachLine in data:
        lineElements = eachLine.strip().split(' ');
        counter = 1;
        writeLine =[];
        print lineElements;
        for eachElement in lineElements:
            writeLine.append(dataMap[int(eachElement)+1]);
            counter = counter + 1;
        writeData += ' '.join(writeLine) + '\n';
        print 'process ',lineCounter,' line'
        lineCounter = lineCounter + 1;
with open(sys.argv[2]+'_new','wb') as processedData:
    processedData.write(writeData);
print 'Finish!'

