class Solution:
    def __init__(self):
        self.result = 0
        self.covered = set([None])
    def dfs(self, node: TreeNode, parent: TreeNode=None):
        if node:
            self.dfs(node.left, node)
            self.dfs(node.right, node)
            
            if (parent is None and node not in self.covered or
                node.left not in self.covered or node.right not in self.covered):
                self.result += 1
                self.covered.update([parent, node, node.left, node.right])
            
        
    def minCameraCover(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.result
