#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 20:16:26 2021

@author: callen
"""
from numTreeNodes import numTreeNodes

def isOdd(x):
    x%2 == 1
    
def getMedian(nodeTree):
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
    nodePosition = num_total - 1 - numRight - numTreeNodes(leadBranch.child_right) if numLeft > numRight else numLeft + numTreeNodes(leadBranch.child_left)
    whichNode = nodePosition
    treeRegister = leadBranch
    lagRegister = nodeTree
    hitMidpoint = False
    if abs(numLeft - numRight) == 1 and not num_total_isOdd:
        # attempting to get node+grandchild together for when the current node
        # is just one element ahead of the two nodes to be averaged
        if leadBranch.child_left:
            print(whichNode)
            return ((nodeTree.value + leadBranch.child_left.value)/2)    
        return ((leadBranch.value + nodeTree.value)/2)
    
    elif whichNode == medianPosition+1 and num_total_isOdd:
        return leadBranch.value
    
    print(f" we have {num_total} nodes. Starting at node number : {whichNode} with value: {leadBranch.value} and median goal: {medianPosition}")
    while treeRegister:
        # edge case: if the median is a node and its grandchild
        if whichNode == medianPosition-1 and treeRegister.child_left.child_right and not num_total_isOdd:
            return((treeRegister.value + treeRegister.child_left.child_right.value)/2)
        # navigate the tree based on if where I currently am is
        # an over-shoot or an under-shoot of the median position,
        # accounting for even-noded tree cases
        if treeRegister.child_left is not None and whichNode >= medianPosition:
            lagRegister = treeRegister
            treeRegister = treeRegister.child_left
            whichNode -= 1
            # node check. Are we there yet?
            if whichNode == medianPosition:
                hitMidpoint = True # will be good for even # node case
                if num_total_isOdd: # odd number case
                    return treeRegister.value
                else:
                    continue
            elif abs(whichNode - medianPosition) == 1 and hitMidpoint:
                # grandchild case again but after the traversal
                if leadBranch.child_left and whichNode-1==medianPosition:
                    return ((leadBranch.child_left.value + nodeTree.value)/2)
                return ((lagRegister.value + treeRegister.value)/2)
            else:
                continue

        elif treeRegister.child_right is not None and (whichNode <= medianPosition):
            # inch up the registers
            # order of inching up registers important so that we save where we were
            lagRegister = treeRegister
            treeRegister = treeRegister.child_right
            whichNode += 1
            # node check. Are we there yet?
            if whichNode == medianPosition:
                hitMidpoint = True # will be good for even # node case
                if num_total_isOdd: # odd number case
                    return treeRegister.value
                else:
                    continue
            elif abs(whichNode - medianPosition) == 1 and hitMidpoint:
                return ((lagRegister.value + treeRegister.value)/2)
            else:
                continue
        else:
            return ((lagRegister.value + treeRegister.value)/2)
        lagRegister = treeRegister
        treeRegister = treeRegister.child_right
    return
