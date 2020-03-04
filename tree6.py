class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        
        # if there's a right node, that means we need to find the left most node of the right node.
        
        if node.right:
            curr = node.right
            while curr.left:
                curr = node.left
            return curr
        
        # If thats not the case, then return the parent node accordingly
        
        while node.parent and node.parent.right is node:
            node = node.parent
        return node.parent
                
                
            
