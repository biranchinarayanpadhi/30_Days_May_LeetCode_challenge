#Approach 1- Using Depth First Search(DFS) Technique
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        ##Using DFS
        if root is None:
            return False
        current=root
        stack=[]
        stack.append(root)
        parents={}
        depth={}
        par=None
        count=0
        stack_of_parents=[None] #temporary_stack to keep track of parents of each child in Binary Tree
        while len(stack)>0:
            node=stack.pop()
            parentNode_of_child=stack_of_parents.pop()
            if parentNode_of_child:
                depth[node.val]=1+depth[parentNode_of_child.val]
            else:
                depth[node.val]=0
            parents[node.val]=parentNode_of_child
            if node.right is not None:
                stack.append(node.right)
                stack_of_parents.append(node)
            if node.left is not None:
                stack.append(node.left)
                stack_of_parents.append(node)
                
        return  depth[x]==depth[y] and parents[x]!=parents[y]
            
      
        
        
#Approach 2-Using Breadth First Search Technique
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        ## Using BFS
        if root is None:
            return False
        dicti={}
        dicti[x]=[-1,-1]
        dicti[y]=[-1,-1]
        q=[]
        q.append(root) 
        count=0
        while q:
            nodes_count=len(q)
            while nodes_count>0:
                    current=q.pop(0)
                    if current.left is not None:
                        if current.left.val == x or current.left.val == y:
                            dicti[current.left.val][0]=count
                            dicti[current.left.val][1]=current.val
                        q.append(current.left)
                    if current.right is not None:
                        if current.right.val == x or current.right.val == y:
                            dicti[current.right.val][0]=count
                            dicti[current.right.val][1]=current.val
                        q.append(current.right)
                    nodes_count-=1
            if dicti[x][0]!=1 and dicti[y][0]!=-1:
                break
            count+=1
        if dicti[x][1]!=dicti[y][1]:
            if dicti[x][0] == dicti[y][0]:
                return True
            else:
                return False
        else:
            return False
