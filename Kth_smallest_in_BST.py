#Optimized Approach(O(Nodes)-->Worst_Case)-->Inorder 
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
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

