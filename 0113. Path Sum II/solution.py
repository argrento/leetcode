class Solution:
    def dfs(self, node: TreeNode, current_path: List[int], paths: List[List[int]], target: int) -> List[List[int]]:
        p = list(current_path)
        p.append(node.val)
        if node.left:
            paths = self.dfs(node.left, p, paths, target)
        if node.right:
            paths = self.dfs(node.right, p, paths, target)
        if not node.left and not node.right:
            if sum(p) == target:
                paths.append(p)
        return paths
        
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        return self.dfs(root, [], [], targetSum)