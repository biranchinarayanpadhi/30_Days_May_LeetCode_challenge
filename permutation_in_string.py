#Brute Force (Time Limit Exceeded):
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1=len(s1)
        len_s2=len(s2)
        list_s1=list(s1)
        
        left=0
        right=len_s1-1
        
        self.dicti={}
        self.permutation(list_s1,left,right,self.dicti)
        for index in range(len_s2):
            if s2[index:index+len_s1] in self.dicti:
                return True
        return False
        
    def permutation(self,s1,l,r,dicti):
        if l==r: 
            dicti["".join(s1)]=0
        else: 
            for i in range(l,r+1): 
                s1[l], s1[i] = s1[i], s1[l] 
                self.permutation(s1, l+1, r,dicti) 
                s1[l], s1[i] = s1[i], s1[l]

#Bit optimized Approach(using sort):
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=sorted(s1)
        len_s1=len(s1)
        len_s2=len(s2)
        list_s1=list(s1)
        if len_s2<len_s1:
            return False
        
        for index in range(len_s2-len_s1+1):
            if sorted(s2[index:index+len_s1]) == s1:
                return True
        return False

#Approach 3(Fully Optimized-Sliding Window Concept):
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dicti_s1={}
        dicti_s2={}
        
        len_s1=len(s1)
        len_s2=len(s2)
        if len_s1>len_s2:
            return False
        
        for character in s1:
            if character in dicti_s1:
                dicti_s1[character]+=1
            else:
                dicti_s1[character]=1
        
        for index in range(len_s1):
            character=s2[index]
            if character in dicti_s2:
                dicti_s2[character]+=1
            else:
                dicti_s2[character]=1
                
        if dicti_s1 == dicti_s2:
            return True
        
        for index in range(len_s2-len_s1):
            character_to_be_removed=s2[index]
            dicti_s2[character_to_be_removed]-=1
            if dicti_s2[character_to_be_removed] == 0:
                dicti_s2.pop(character_to_be_removed)
            
            print(index)
            character_to_be_added=s2[index+len_s1]
            if character_to_be_added in dicti_s2:
                dicti_s2[character_to_be_added]+=1
            else:
                dicti_s2[character_to_be_added]=1
                
            if dicti_s1 == dicti_s2:
                return True
            
        return False
                
            
        
            
            
        
        
       
        
            
        
        
       
        