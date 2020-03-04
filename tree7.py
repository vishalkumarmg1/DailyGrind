class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return []
        
        preorder = []
        stack =[root]
        
        
        while stack:
            curr = stack.pop()
            if curr:
                stack.append(curr.right)
                stack.append(curr.left)
                preorder.append(curr.val)
                
        return preorder
        
