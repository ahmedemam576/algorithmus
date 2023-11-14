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
## same tree with recusrion
def same_tree(p,q):
	if  not p and not q:
		return True
	if  not p or not q or p.data != q.data:
		return False
	return same_tree(p.right, q.right) and (p.left, q.left)

