# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, node: Optional[TreeNode]) -> bool:

        def valid(node,low,high):
                
            if not node:
                return True
            
            if not (low < node.val <high):
                return False
            
            return valid(node.left, low, node.val) and valid(node.right, node.val, high)
        
        return valid(node,float('-inf'), float('inf'))
        
               
                
