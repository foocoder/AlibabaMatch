#!/usr/bin/python
#FileName: mapItemCatId.py
#Author:   Fuchen Duan
#Email:    slow295185031@gmail.com

try:
    import cPickle as pickle
except ImportError:
    import pickle

dataName='dim_items.txt';
with open(dataName, 'rb') as itemRecord:
    dataMap = {};
    counter = 0;
    for eachLine in itemRecord:
        splitedItem = eachLine.strip().split(' ');
        dataMap[splitedItem[0]] = splitedItem[1];
        counter += 1;
        print "Process"+str(counter)+"Records";

with open('item_cat.pkl','wb') as pklFile:
    pickle.dump(dataMap,pklFile);
print "Finished!"
