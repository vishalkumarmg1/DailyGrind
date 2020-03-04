class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        inorder =[]
        
        stack = []
        
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            
            root = stack[-1]
            inorder.append(root.val)
            stack.pop()
            
            root = root.right
            
        return inorder==sorted(inorder) and len(inorder)==len(set(inorder))
