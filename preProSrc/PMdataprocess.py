#!/usr/bin/python
#Filename: PMdataprocee.py
#Author:   Fuchen Duan

try:
    import cPickle as pickle
except ImportError:
    import pickle

with open('nopeatItemCatId','rb') as data:
    dataMap = {};
    dataMap1 = {};
    counter = 1;
    for eachLine in data:
        lineElements = eachLine.strip().split(' ');
        for eachElement in lineElements:
            if not dataMap.has_key(eachElement):
                dataMap[eachElement] = counter;
                dataMap1[counter] = eachElement;
                counter = counter +1;
                print str(counter-1);
with open('Cat_No.pkl','wb') as pickleFile:
    pickle.dump(dataMap, pickleFile)
with open('No_Cat.pkl','wb') as pickleFile:
    pickle.dump(dataMap1, pickleFile)

with open('nopeatItemCatId','rb') as data:
    lineCounter = 1;
    writeData = '';
    for eachLine in data:
        lineElements = eachLine.strip().split(' ');
        writeLine = ['0' for i in range(counter-1)];
        for eachElement in lineElements:
            writeLine[dataMap[eachElement]-1] = '1';
        writeData += ' '.join(writeLine) + '\n';
        print 'process ',lineCounter,' line'
        lineCounter = lineCounter + 1;
with open('labledcat.dat','wb') as processedData:
    processedData.write(writeData);
print 'Finish!'

