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
###### the Kth smallest element in a BST
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n=0 
        stack = []
        pointer = root
        while pointer or stack:
            while pointer:
                stack.append(pointer)
                pointer = pointer.left
            pointer = stack.pop()
            n+=1
            if n== k:
                return pointer.val
            pointer = pointer.right

#####serialize and deserialize binary tree with recursion

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        def dfs(root):
            if not root:
                ans.append("N")
                return
            ans.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.i=0
        values = data.split(",")
        def dfs():
            if values[self.i]=="N":
                self.i +=1
                return None
            root = TreeNode(int(values[self.i]))
            self.i +=1
            root.left =dfs()
            root.right =dfs()
            return root
        return dfs()
	    ### construct BST from preorder and inorder
class Solution:
   def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        # Recursive solution
        if inorder:   
            # Find index of root node within in-order traversal
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            
            # Recursively generate left subtree starting from 
            # 0th index to root index within in-order traversal
            root.left = self.buildTree(preorder, inorder[:index])
            
            # Recursively generate right subtree starting from 
            # next of root index till last index
            root.right = self.buildTree(preorder, inorder[index+1:])
            return root

## implement a Trie
class Node:
    def __init__(self):
        self.children = {}
        self.EndofWord= False
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur =self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=Node()
            cur = cur.children[c]
        cur.EndofWord =True
        

    def search(self, word: str) -> bool:
        cur= self.root
        for c in word:
            if c not in cur.children :
                return False
            cur = cur.children[c]
        return cur.EndofWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

## course schedule , detect cycle in a graph
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prelist = {}
        for crs in range(numCourses):
            prelist[crs]= []
        for crs, pre in prerequisites:
            prelist[crs].append(pre)
        visitset = set()
        def dfs(crs):
            if crs in visitset:
                return False
            if prelist[crs]==[]:
                return True
            visitset.add(crs)
            for pre in prelist[crs]:
                if not dfs(pre):
                    return False
            visitset.remove(crs) # if we remove this it will always produce false
            prelist[crs]=[] #if we removed this it will take too much time
            return True
        for crs in range(numCourses):
            if not dfs(crs):return False
        return True
# clone graph
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtonew={}
        def dfs(node):
            if not node:
                return None
            if node in oldtonew:
                return oldtonew[node]
            copy = Node(node.val)
            oldtonew[node]=copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)
	    ## number of island depth for search with queue
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r,c):
            q =collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row,col =q.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    r,c = row+dr , col+dc
                    if (r in range(rows) and
                        c in range(cols) and 
                        grid[r][c] =='1'and
                        (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))

        if not grid :

            return 0
        
        rows , cols = len(grid), len(grid[0])
        visit = set()
        islands =0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and (r,c) not in visit:
                    bfs(r,c)
                    islands +=1
        return islands
        
#pacific atlantic ocean (graph)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        rows, cols = len(heights), len(heights[0])
        pvisit = set()
        avisit = set()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(visited, x,y):
            visited.add((x,y))
            for dx, dy in directions:
                newx, newy = x+dx, y+dy
                if 0 <= newx< rows and 0<=newy<cols and (newx, newy) not in visited and heights[newx][newy]>=heights[x][y]:
                    dfs(visited, newx,newy)
        for r in range(rows):
            #left and right border
            dfs(pvisit, r,0)
            dfs(avisit,r, cols-1 )
        for c in range(cols):
            # top and bottom borders
            dfs(pvisit, 0, c)
            dfs(avisit, rows-1, c)
        # the intersection of 2 lists are the position where water can flow from pacific to the atlantic
        return list(pvisit.intersection(avisit))
#climbing stairs # dynamic programing
class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two  = 1
        for i in range(n-1):
            tmp = one
            one = one+two
            two = tmp
        return one

