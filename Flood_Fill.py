#Brute Force(RecursiveApproach):
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        prevColor=image[sr][sc]
        
        self.recursiveApproach(image,sr,sc,newColor,prevColor)
        return image
    
    def recursiveApproach(self,image,i,j,newColor,prevColor):
        
        print(i,j)
        
        if not (0<=i<len(image) and 0<=j<len(image[0])):
            return 
        
        if prevColor != image[i][j]:
            return 
        
        if newColor == image[i][j]:
            return
        
        image[i][j]=newColor

        self.recursiveApproach(image,i-1,j,newColor,prevColor)
        self.recursiveApproach(image,i+1,j,newColor,prevColor)
        self.recursiveApproach(image,i,j+1,newColor,prevColor)
        self.recursiveApproach(image,i,j-1,newColor,prevColor)
 
#Approach 2:(Optimizing Recusrive Approach with Memoization):
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.count=0
        prevColor=image[sr][sc]
        memo=[[-1 for j in range(len(image[0]))] for i in range(len(image))]
        self.recursiveApproach(image,sr,sc,newColor,prevColor,memo)
        return image
    
    def recursiveApproach(self,image,i,j,newColor,prevColor,memo):
        
        self.count+=1
        if not (0<=i<len(memo) and 0<=j<len(memo[0])):
            return
        
        if prevColor != image[i][j]:
            return 
        
        if memo[i][j]!=-1:
            return
        
        if prevColor == image[i][j] and prevColor == newColor:
            return
       
        if prevColor == image[i][j]:
            image[i][j]=newColor
            memo[i][j]=newColor
            
        
        self.recursiveApproach(image,i-1,j,newColor,prevColor,memo)
        self.recursiveApproach(image,i+1,j,newColor,prevColor,memo)
        self.recursiveApproach(image,i,j+1,newColor,prevColor,memo)
        self.recursiveApproach(image,i,j-1,newColor,prevColor,memo)
        
#Approach 3(BFS):
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        prevColor=image[sr][sc]
        q=[(sr,sc)]
        
        if image[sr][sc] == newColor:
            return image

        while q:
            i,j=q.pop()
            if 0<=i<len(image) and 0<=j<len(image[0]) and image[i][j]==prevColor:
                image[i][j]=newColor
                q.append((i-1,j))
                q.append((i+1,j))
                q.append((i,j-1))
                q.append((i,j+1))
                
        return image
        