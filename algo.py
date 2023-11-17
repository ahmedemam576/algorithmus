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

## Binary tree level order  traversal
class solution:
	def levelOrder(self, root:[TreeNode])->List:
		q = collections.deque()
		res =[]
		q.append(root)
		while q:
			level =[]
			level_len = len(q)
			for lvl in level_len:
				node =q.popleft()
				if node :
					level.append(node.val)
					q.append(node.left)
					q.appned(node.right)
			res.append(level)
		return res
##### lowest ancestor for BTS
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if p.val > cur.val and q.val  > cur.val :
                cur = cur.right
            elif p.val < cur.val and q.val    < cur.val :
                cur = cur.left
            else:
                return cur
				
			
