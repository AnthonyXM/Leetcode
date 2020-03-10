# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.m = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.h(root)
        return self.m

    def h(self, root: TreeNode) -> int:
        if root.left==None and root.right==None:
            return 0
        elif root.left==None:
            r = 1 + self.h(root.right)
            if r > self.m:
                self.m = r
            return r
        elif root.right==None:
            l = 1 + self.h(root.left)
            if l > self.m:
                self.m = l
            return l   
        else:
            l = 1 + self.h(root.left)
            r = 1 + self.h(root.right)
            if l+r > self.m:
                self.m = l+r
            return max(l,r)

a = Solution()
b = TreeNode(1)
b.left = TreeNode(2)
b.right = TreeNode(3)
b.left.left = TreeNode(4)
b.left.right = TreeNode(5)
print(a.diameterOfBinaryTree(b))