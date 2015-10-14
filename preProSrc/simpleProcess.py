#!/usr/bin/python
#FileName: simpleProcess.py
#Author:   Fuchen Duan
#Email:    slow295185031@gmail.com

try:
    import cPickle as pickle
except ImportError:
    import pickle

itemFileName = 'test_items.txt';
savedPath = './';

with open(savedPath+itemFileName+'rb') as itemRecord:
    itemMap = {};
    conter  = 0;
    for eachItem in itemRecord:

