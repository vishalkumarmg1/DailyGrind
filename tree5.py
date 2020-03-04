class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        inorder = []
        stack = []
        flag = False
        
        while root or stack:
            while root:
                stack.append(root)
                root =root.left
            root = stack[-1]
            inorder.append(root)
            stack.pop()
            root =root.right
        
        for x in inorder:
            if flag:
                return x
            if x.val==p.val:
                flag=True
                
        return None
            
