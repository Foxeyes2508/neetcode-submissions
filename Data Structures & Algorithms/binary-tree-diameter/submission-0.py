# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # Stores the maximum diameter found so far
        diameter = 0

        # Returns the height of the subtree rooted at 'node'
        def dfs(node):
            nonlocal diameter

            # Base case: empty subtree has height 0
            if node is None:
                return 0

        
            left = dfs(node.left)

            # Height of right subtree
            right = dfs(node.right)

            # Diameter passing through the current node
            diameter = max(diameter, left + right)

            # Return height of the current subtree
            return 1 + max(left, right)

        # Start DFS from the root
        dfs(root)

        # Return the maximum diameter found
        return diameter