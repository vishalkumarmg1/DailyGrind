class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        inorder = []
        stack = []
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root =stack[-1]
            if root.val == val:
                return root
            inorder.append(root.val)
            stack.pop()
            root =root.right
        
        return root
