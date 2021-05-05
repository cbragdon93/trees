#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 19:02:21 2021

@author: callen
"""

def numTreeNodes(nodeTree):
    if nodeTree is not None:
        return 1 + numTreeNodes(nodeTree.child_left) + numTreeNodes(nodeTree.child_right)
    return 0
