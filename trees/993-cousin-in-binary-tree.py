# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        # edge case
        if root == x or root == y:
            return False

        # stack = [(root, level, parent)]
        stack = [(root, 0, None)]
        x_level_parent = -1
        y_level_parent = -1

        while stack:
            curr_node, level, parent = stack.pop()
            # check if the node is not Null and wont append leaf.left/leaf.right
            if curr_node:
                if curr_node.val == x:
                    x_level_parent = (level, parent)
                elif curr_node.val == y:
                    y_level_parent = (level, parent)

                stack.append((curr_node.left, level+1, curr_node))
                stack.append((curr_node.right, level+1, curr_node))

        #  check if the cousing condition is met
        if x_level_parent[0] == y_level_parent[0] and x_level_parent[1] != y_level_parent[1]:
            return True

        return False
