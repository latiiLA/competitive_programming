"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyMap = {None: None}

        # Loop to make the copy of the dictionary
        curr = head
        while curr:
            copy = Node(curr.val)
            copyMap[curr] = copy
            curr = curr.next
        
        # Loop to make connect the Nodes
        curr = head
        while curr:
            copy = copyMap[curr]
            copy.next = copyMap[curr.next]
            copy.random = copyMap[curr.random]
            curr = curr.next

        return copyMap[head]

        