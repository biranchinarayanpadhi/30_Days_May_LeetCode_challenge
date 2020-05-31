#Brute Force(O(N)-Level Order traversal)
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        if root is None:
            return None
        res=[]
        current=root
        q=[]
        
        while True:
            
            if current is not None:
                q.append(current)
                current=current.left
            
            elif len(q)>0:
                current=q.pop()
                res.append(current.val)
                current=current.right
                
            else:
                break
#print(res)       
        return res[k-1]

#Approach 2(O(K)-->Level Order Traversal):
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        #Brute Force Solution
        """"
        result=[]
        stack=[]
        stack.append(root)
        while len(stack)!=0:
            current=stack.pop()
            result.append(current.val)
            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)
        
         """
        q=[]
        result=[]
        current=root
        while True:
            if current is not None:
                q.append(current)
                current=current.left
            elif len(q)!=0:
                current=q.pop()
                result.append(current.val)
                current=current.right
            else:
                break
            if len(result) == k:
                return result[-1]

#Approach 3(Using Heap-O(NlogK)):
import heapq
class Solution(object):
        
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        q=[]
        q.append(root)
        result=[]
        while len(q)!=0:
            current=q.pop()
            result.append(current.val)
            if current.right is not None:
                q.append(current.right)
            if current.left is not None:
                q.append(current.left)
        heapq.heapify(result)
        smallest_ele=result[-1]
        while k!=0:
            smallest_ele=heapq.heappop(result)
            k-=1
        return smallest_ele
            