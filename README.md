# Trees
##About
This github page is an exploration of implementing and optimizing a Binary Search Tree(BST) approach for insertions and median acquisition.
## Contents
- ‘myNode.py’ contains the `myNode` class, the object I use to create my trees.
- ‘insert.py’ contains the function that inserts new values/`myNode` objects into a `myNode` object.
   - Inputs: `myNode` object and a number
   - Output:  a modified myNode object with the new entry if it wasn’t already present; otherwise, the original myNode object. Updates the `numNodesLeft` and `numNodesRight` attributes of the (root) `myNode` object.
- getMedian.py contains the function that will return the median from a myNode object:
  - Input: `myNode` object
  - Output: number denoting the median(corner cases accounted for)
- numTreeNodes.py contains the function required to count the number of nodes in a `myNode` object.
  - Input: `myNode` object
  - Output:  integer denoting the number of present nodes
- treeTesting.py contains a script that executes a creation and appending of test trees (values were thought of arbitrarily). It then invokes `getMedian` after certain insertions, and compares the value acquired through `getMedian` and the value arising from calling `statistics.median` on a list version of the BST.
- getMedianFaster.py is an experimental script where I am making improvements to the speed of getMedian.py
