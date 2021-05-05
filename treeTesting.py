#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 18:54:53 2021

@author: callen
"""

#%% imports
from myNode import myNode
from numTreeNodes import numTreeNodes
from insert import *
from getMedian import getMedian
from statistics import median
#%% practice
def runTests():
    # inserting
    myTree = myNode(None)
    myNumbers = [8,60,4,2,1,14,15]
    for i in myNumbers:
        myTree = insert(myTree, i)
    # add more
    numbersToAdd = [70, 13, 62, 65, 5, 100, 105, 110, 120]
    for n in numbersToAdd:
        myNumbers.append(n)
        myTree = insert(myTree, n)
        print(f"Tree median: {getMedian(myTree)}")
        print(f"Expected median: {median(myNumbers)}")
#%% run it
from getMedian import getMedian
runTests()
#%% single-cases
from getMedian import getMedian
testTree = myNode(None)
myNumbers = [8,60,4,2,1,14,15, 70]
for i in myNumbers:
    testTree = insert(testTree, i)
x=(getMedian(testTree))
print(f"tree Median, isolated case: {x}")
print(f"expected Median, isolated case: {median(myNumbers)}")
#%% test inserting
p=myNode(None)
p=insert(p,5)
p=insert(p,4)
p=insert(p,3)
p=insert(p,9)
p=insert(p,9)
print(p.__dict__)
