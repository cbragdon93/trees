class myNode:
    def __init__(self, value, child_left=None, child_right=None):
        self.value = value
        self.child_left = child_left
        self.child_right = child_right
        self.numNodesLeft = 0
        self.numNodesRight = 0