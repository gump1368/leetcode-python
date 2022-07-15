# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        left = [root]
        right = []
        res = []
        while left or right:
            cache = []
            while left:
                node = left.pop()
                cache.append(node.val)
                if node.left:
                    right.append(node.left)
                if node.right:
                    right.append(node.right)

            if cache:
                res.append(cache)
                cache = []

            while right:
                node = right.pop()
                cache.append(node.val)
                if node.right:
                    left.append(node.right)
                if node.left:
                    left.append(node.left)

            if cache:
                res.append(cache)
        return res
