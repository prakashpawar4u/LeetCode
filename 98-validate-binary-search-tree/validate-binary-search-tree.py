# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # def in_order_traversal(node):
        #     if not node:
        #         return []
        #     return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)
        
        # in_order = in_order_traversal(root)

        # for i in range(1, len(in_order)):
        #     if in_order[i] <= in_order[i -1]:
        #         return False
        # return True
        def validate(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            # Check if the current node's value is within the valid range
            if node.val <= lower or node.val >= upper:
                return False
            # Recursively validate the left and right subtrees
            return (validate(node.left, lower, node.val) and
                    validate(node.right, node.val, upper))

        return validate(root)