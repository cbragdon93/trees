#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 17:27:16 2021

@author: callen
"""

"""
Experimental, attempting to 
optimize speed of BST median acquisitionn
by dynamically checking the skewedness of the current node we traversed to
"""
#%% imports
from numTreeNodes import numTreeNodes
from myNode import myNode
from treeTesting import runTests
from insert import *
from statistics import median
#%% functions
def isOdd(x):
    x%2 == 1
    
def getMedianFaster(nodeTree):
    if not nodeTree:
        return None
    numLeft = nodeTree.numNodesLeft
    numRight = nodeTree.numNodesRight
    num_total = numLeft + numRight + 1
    num_total_isOdd = num_total % 2 != 0
    if numLeft == numRight and num_total_isOdd:
        return nodeTree.value
    medianPosition = num_total // 2
    leadBranch = nodeTree.child_left if numLeft>numRight else nodeTree.child_right
    # I start traversing on the root node of the *leading branch*.
    # so, I need to find first child node's relative position based on what branch
    # the tree is skewed toward
    print(leadBranch.__dict__)
    nodePosition = \
        num_total - 1 - numRight \
        if numLeft > numRight \
            else \
                numLeft + 1 + leadBranch.numNodesLeft
    if numLeft>numRight and leadBranch.child_right:
        print(leadBranch.__dict__)
        nodePosition -= (leadBranch.numNodesRight)
    elif numRight>numLeft and leadBranch.child_left:
        print(nodePosition)
    whichNode = nodePosition
    treeRegister = leadBranch
    lagRegister = nodeTree
    hitMidpoint = False
    print(f" we have {num_total} nodes. Starting at node number : {whichNode} with value: {leadBranch.value} and median goal: {medianPosition}")
    while treeRegister:
        # can check relative position for median here
        # before updating registers.
        # will be cleaner for accounting for
        # grandparent-grandchild pairs for the median
        numLead = treeRegister.numNodesRight
        numLag = treeRegister.numNodesLeft
        leadOverLag = numLead > numLag
        leadIsLag = numLead == numLag
        oneStepAround  = abs(whichNode-medianPosition) <= 1
        if whichNode == medianPosition+1 and num_total_isOdd:
            return treeRegister.value
        elif whichNode == medianPosition and not num_total_isOdd:
            if not leadOverLag and treeRegister.child_left:
                return ((treeRegister.child_left.value + lagRegister.value)/2)
            elif not leadOverLag and treeRegister.child_right:
                return((treeRegister.child_right.value + treeRegister.value)/2)
            return((treeRegister.value + lagRegister.value)/2)
        if leadOverLag:
            lagRegister = treeRegister
            treeRegister = treeRegister.child_right
            whichNode += treeRegister.numNodesLeft + 1
        elif numLead == numLag:
            if numLeft > numRight:
                lagRegister = treeRegister
                treeRegister = treeRegister.child_right
            elif numLeft < numRight:
                lagRegister = treeRegister
                treeRegister = treeRegister.child_left
        else:
            lagRegister = treeRegister
            treeRegister = treeRegister.child_left

def runTestsFaster(myNumbers = [8,60,4,2,1,14,15],
             numbersToAdd = [70, 13, 62, 65, 5, 100, 105, 110, 120]):
    # inserting
    myTree = myNode(None)
    if myNumbers:
        for i in myNumbers:
            myTree = insert(myTree, i)
    # add more
    if numbersToAdd:
        for n in numbersToAdd:
            myNumbers.append(n)
            myTree = insert(myTree, n)
            print(f"Tree median: {getMedianFaster(myTree)}")
            print(f"Expected median: {median(myNumbers)}")
#%% test
testTree = [20,2,1,4,3,8,7,6,40,35,25,22,24,37,36,70,60,80]
runTestsFaster(myNumbers = [], numbersToAdd=testTree)





