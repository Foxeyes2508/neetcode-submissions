# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # Returns the height of the subtree if it is balanced.
        # Returns -1 if the subtree is not balanced.
        def dfs(node):

            # Base case: empty tree has height 0
            if node is None:
                return 0

            # Find height of left subtree
            left = dfs(node.left)

            # If left subtree is unbalanced, stop immediately
            if left == -1:
                return -1

            # Find height of right subtree
            right = dfs(node.right)

            # If right subtree is unbalanced, stop immediately
            if right == -1:
                return -1

            # If height difference is greater than 1,
            # current subtree is not balanced
            if abs(left - right) > 1:
                return -1

            # Return height of current subtree
            return 1 + max(left, right)

        # If dfs returns -1, tree is not balanced
        return dfs(root) != -1