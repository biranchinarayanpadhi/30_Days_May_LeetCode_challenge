#Sliding_Window(O(N)):
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        dicti_p={}
        dicti_s={}
        len_s=len(s)
        len_p=len(p)
        if len_s<len_p:
            return []
        result=[]
        for character in p:
            if character not in dicti_p:
                dicti_p[character]=1
            else:
                dicti_p[character]+=1
                
        for index in range(len_p):
            character=s[index]
            if character not in dicti_s:
                dicti_s[character]=1
            else:
                dicti_s[character]+=1
                
        if dicti_s == dicti_p:
            result.append(0)
    
        for index in range(0,len_s-len_p):
            character_to_be_removed=s[index]
            dicti_s[character_to_be_removed]-=1
            
            if dicti_s[character_to_be_removed]==0:
                dicti_s.pop(character_to_be_removed)
                
            character_to_be_added=s[index+len_p]
            
            if character_to_be_added in dicti_s:
                dicti_s[character_to_be_added]+=1
            else:
                dicti_s[character_to_be_added]=1
                
            if dicti_s == dicti_p:
                result.append(index+1)
                
        return result
        
#Approach 2(Using Sort(N(KlogK)):
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p=sorted(p)
        len_p=len(p)
        len_s=len(s)
        result=[]
        start=0
        end=len_s-len_p+1
        while start<end:
            if sorted(s[start:start+len_p]) == p:
                result.append(start)
            if sorted(s[end:end+len_p]) == p:
                result.append(end)
            start+=1
            end-=1
        
        if start == end:
            if sorted(s[start:start+len_p]) == p:
                result.append(start)
            
        return result