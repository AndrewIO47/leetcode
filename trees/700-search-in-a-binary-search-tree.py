# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # since it is a BST, all nodes to the left of the root are < root.val
        # and on the right the values are > root.val
        # knowing this, we can determine where is the target located in the subtrees
        current = root

        while current:

            if current.val > val:
                current = current.left

            elif current.val < val:
                current = current.right

            else:
                root = current
                return root
