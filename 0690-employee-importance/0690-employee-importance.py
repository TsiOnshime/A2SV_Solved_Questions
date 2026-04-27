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
        graph = defaultdict(list)
        id_imp = defaultdict(int)

        for i in range(len(employees)):
            graph[(employees[i].id, employees[i].importance)].extend(employees[i].subordinates)
            id_imp[employees[i].id] = employees[i].importance

        def dfs(start):
            stack = [start]
            importance = 0

            while stack:
                employee = stack.pop()
                importance += employee[1]

                for sub in graph[employee]:
                    stack.append((sub, id_imp[sub]))

            return importance




        for key in graph.keys():
            if key[0] == id:
                return dfs(key)