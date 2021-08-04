"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hm = {}
        for emp in employees:
            hm[emp.id] = emp
        queue = hm[id].subordinates
        result = hm[id].importance
        
        while queue:
            id = queue.pop(0)
            result += hm[id].importance
            queue.extend(hm[id].subordinates)
            
        return result
            