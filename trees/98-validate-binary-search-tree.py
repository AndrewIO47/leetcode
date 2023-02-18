# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        output = []

        def inOrder(root):
            if not root:
                return

            inOrder(root.left)
            output.append(root.val)
            inOrder(root.right)

        inOrder(root)
        # checks if the previous value is >= to the current value
        # this works becasue we are using inOrder traversal which returns
        # a list in increasing order since it is a BST
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False

        return True
