class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        inorder = []
        stack = []
        
        while root or stack:
            while root:
                stack.append(root)
                root =root.left
            
            root = stack[-1]
            inorder.append(root.val)
            stack.pop()
            root =root.right
        
        return inorder[k-1]
