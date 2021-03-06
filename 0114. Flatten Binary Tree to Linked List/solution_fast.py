class Solution:
    def __init__(self):
        self.previous = None
    
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        self.flatten(root.right)
        self.flatten(root.left)
        
        root.right = self.previous
        root.left = None
        self.previous = root
