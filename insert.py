#%% imports
from myNode import myNode
from numTreeNodes import numTreeNodes
#%% insert function

# Was having a weird time trying to integrate
# these methods into the myNode class, but 
# my plan was to make a private insert method
# that would modify the private numNodes{Left,Right}
# attributes in the myNodes class
def insert_private(nodeTree, value):
    if nodeTree is None or nodeTree.value is None:
        return myNode(value)
    if value < nodeTree.value:
        nodeTree.child_left = insert_private(nodeTree.child_left, value)
    elif value > nodeTree.value:
        nodeTree.child_right = insert_private(nodeTree.child_right, value)
    return nodeTree

# since this function messes with non-private
# attributes, I may just have to traverse the tree to
# track the number of nodes on each side for each insert
# if I don't trust the user to not modify those attributes
def insert(nodeTree, value):
    nodeTree = insert_private(nodeTree, value)
    nodeTree.numNodesLeft = numTreeNodes(nodeTree.child_left) if nodeTree.child_left is not None else 0
    nodeTree.numNodesRight = numTreeNodes(nodeTree.child_right) if nodeTree.child_right is not None else 0
    # This section fails if I try to enter duplicate values
    # I'd rather have this dynamic up-ticking below work, but sticking with
    # traversal after insertion for now.
    # so just traverse the tree after insertion...
    # if value < nodeTree.value:
    #     nodeTree.numNodesLeft += 1
    # elif value > nodeTree.value:
    #     nodeTree.numNodesRight += 1
    return nodeTree
