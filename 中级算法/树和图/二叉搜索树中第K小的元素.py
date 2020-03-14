# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return None

        stack = []
        small = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            small.append(root.val)
            if len(small) == k:
                break
            root = root.right
        return small[-1]

