class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root == None:
            return result
        max_depth = 0
        
        def dfs(root: TreeNode, child: TreeNode, depth: int):
            if child != None:
                print(child.val, depth, len(result))
                if len(result) <= depth:
                    result.append([])
                result[depth].append(child.val)
                
                dfs(child, child.left, depth + 1)
                dfs(child, child.right, depth + 1)
        
        dfs(None, root, 0)
        
        return result
        
