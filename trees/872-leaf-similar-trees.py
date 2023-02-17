# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        result1 = []
        result2 = []

        def inorder(root, result):

            if not root:
                return
            inorder(root.left, result)
            if (root.left is None and root.right is None):
                result.append(root.val)
            inorder(root.right, result)

        inorder(root1, result1)
        inorder(root2, result2)

        if result1 == result2:
            return True
        return False
