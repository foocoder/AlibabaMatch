#!/usr/bin/python
#FileName: extractDatabase.py
#Author: Fuchen Duan

try:
    import cPickle as pickle
except ImportError:
    import pickle

dataName = 'user_bought_history';
savePath = './';

#Load Data
record = open(savePath+dataName+'.txt','rb');
dateMap ={};
dateCounter = 0;
recordCounter   = 0;
for eachLine in record:
    splitedElements = eachLine.strip().split(' ');
    if not dateMap.has_key(splitedElements[2]):
        dateMap[splitedElements[2]] = [ (splitedElements[0],splitedElements[1]) ];
        dateCounter += 1;
    else:
        dateMap[splitedElements[2]].append((splitedElements[0],splitedElements[1]));
    recordCounter += 1;
    print "Processed "+ str(recordCounter)+" records";
record.close();
print "total is "+str(dateCounter)+" pickls!"

pickleFile = open(savePath+dataName+'.pkl','wb');
pickle.dump(dateMap,pickleFile);
pickleFile.close();

#Save Data
#count1 = 1;
#dataSaveName = 'user_bought_1_day';
#for eachList in dateMap.values():
#    count1 += 1;
#    if len(eachList) == 1:
#	continue;
#    writeLine = ' '.join(eachList);
#    writeLine = writeLine + '\n';
#    saveFile = open(savePath+dataSaveName,'ab');
#    saveFile.write(writeLine);
#    print "Saved " + str(count1) + "Records, total is " + str(dateCounter) +"Records"
#saveFile.close();
print "Finished!"
