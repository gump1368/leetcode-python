# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        i = 0
        node = preorder[i]
        while node not in inorder:
            i += 1
            node = preorder[i]
        res = TreeNode(node)
        index = inorder.index(node)
        left = inorder[:index]
        right = inorder[index + 1:]

        res.left = TreeNode(left[0]) if len(left) == 1 else self.buildTree(preorder[i + 1:], inorder[:index])
        res.right = TreeNode(right[0]) if len(right) == 1 else self.buildTree(preorder[i + 1:], inorder[index + 1:])

        return res