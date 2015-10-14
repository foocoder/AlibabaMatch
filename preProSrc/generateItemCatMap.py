#!/usr/bin/python
#FileName: generateItemCatMap.py
#Author:   Fuchen Duan
#Email:    slow295185031@gmail.com

try:
    import cPickle as pickle
except ImportError:
    import pickle

with open('dim_items.txt','rb') as itemRecord:
    itemMap = {};
    conter  = 0;
    for eachLine in itemRecord:
        eachElements = eachLine.strip().split(' ');
        if not itemMap.has_key(eachElements[0]):
            itemMap[eachElements[0]] = eachElements[1];
        conter += 1;
        print str(conter) + " processed!"

with open('all_item_cat_map.pkl','wb') as saveRecord:
    pickle.dump(itemMap,saveRecord);
print "Finished!"
