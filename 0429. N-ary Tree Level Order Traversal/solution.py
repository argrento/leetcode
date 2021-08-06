"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        queue = [root] if root else None
        
        while queue:
            result.append([x.val for x in queue])
            queue = [child for node in queue for child in node.children]
        return result