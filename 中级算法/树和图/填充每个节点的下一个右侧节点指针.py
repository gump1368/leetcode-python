"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        res = [root]
        while res:
            res_back = []
            right_next = None
            while res:
                node = res.pop()
                if right_next:
                    node.next = right_next
                right_next = node
                if node.left:
                    res_back.extend([node.right, node.left])
            res = res_back[::-1]
        return root
