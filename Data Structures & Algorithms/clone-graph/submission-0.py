"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Given a graph, deep clone the graph
        # The key parts of this problem is:
        # Doing it while conserving all connections
        # Not getting stuck in an infinite loop
        # To preserve all connections, we should make connections 
        # once a node is reached
        # To avoid an infinite loop, keep track of which nodes are visited
        # To prevent repeat connections (since it's a non-directed graph)
        # Don't add connections which have been visited
        nodes = {1 : Node(node.val) if node else None}
        visited = set()
        queue = []
        if node is not None:
            queue.append(node)
        while queue:
            item = queue.pop()
            if item.val in visited:
                continue
            visited.add(item.val)
            queue.extend(item.neighbors)
            for neighbor in item.neighbors:
                copy = nodes.setdefault(neighbor.val, Node(neighbor.val))
                nodes[item.val].neighbors.append(copy)

    
        return nodes[1]
