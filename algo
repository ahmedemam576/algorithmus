## maiximum depth of a binary tree with recusrsion

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

from ds_v1.BinaryTree.BinaryTree import TreeNode


def find_max_depth(root):
        if not root:
            return 0
        
        return 1 + max(find_max_depth(root.right), find_max_depth(root.left)
