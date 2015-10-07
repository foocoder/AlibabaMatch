#!/usr/bin/python
#FileName: extractDatabase.py
#Author:   Fuchen Duan
#Email:    slow295185031@gmail.com

try:
    import cPickle as pickle
except ImportError:
    import pickle

dataName = 'user_bought_history.txt';
savePath = './';

#Load Data
with open(savePath+dataName,'rb') as record:
    dateMap ={};
    counter = 1;
    for eachLine in record:
        splitedElements = eachLine.strip().split(' ');
        if not dateMap.has_key((splitedElements[0],splitedElements[2])):
            dateMap[(splitedElements[0],splitedElements[2])] = [ splitedElements[1] ];
            counter += 1;
        else:
            dateMap[(splitedElements[0],splitedElements[2])].append(splitedElements[1]);

#Save Data
dataSaveName = 'user_bought_database';
for eachList in dateMap.values():
    if len(eachList) == 1:
        continue;
    writeLine = ' '.join(eachList);
    writeLine += '\n';
    with open(savePath+dataSaveName,'ab') as saveFile:
        saveFile.write(writeLine);

print "Finished!"
