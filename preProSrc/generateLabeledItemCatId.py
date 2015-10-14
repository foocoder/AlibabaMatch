#!usr/bin/python
#FileName: generateLabledItemCatId.py
#Author:   Fuchen Duan
#Email:    slow295185031@gmail.com

try:
    import cPickle as pickle
except ImportError:
    import pickle
import re
dataName = 'item_cat.pkl'
with open(dataName,'rb') as itemCatFile:
    dataMap = pickle.load(itemCatFile);
    with open('dim_fashion_matchsets.txt','rb') as labeledFile:
        counter = 0;
        writeLine = '';
        for eachLine in labeledFile:
            lineElements = re.split(',|;',eachLine.strip().split(' ')[1]);
            for elements in lineElements:
                writeLine += dataMap[elements]+' ';
            writeLine += '\n';
            counter += 1;
            print "process "+str(counter)+" labled matches";
with open('labledItemCatId','wb') as writeFile:
    writeFile.write(writeLine);
