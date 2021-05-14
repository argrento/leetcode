class Solution:
    def dfs(self, node: TreeNode, flattened: List[TreeNode]):
        flattened.append(node)
        if node.left:
            self.dfs(node.left, flattened)
        if node.right:
            self.dfs(node.right, flattened)
    
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return []
        head = root
        flattened = []
        self.dfs(head, flattened)    

        for idx in range(len(flattened)-1):
            flattened[idx].left = None
            flattened[idx].right = flattened[idx+1]
        
        return root
