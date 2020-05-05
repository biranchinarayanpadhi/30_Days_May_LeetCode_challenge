#Approach 1(Optimized)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counting_dicti={}
        length_of_s=len(s)
        for character in s:
            if character not in counting_dicti:
                counting_dicti[character]=1
            else:
                counting_dicti[character]+=1
                
        for index in range(length_of_s):
            character=s[index]
            if counting_dicti[character]==1:
                return index
        
        return -1

#Approach 2:

	class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums=[0]*26
        for character in s:
            position=ord(character)-97
            nums[position]+=1
            
        for index in range(len(s)):
            character=s[index]
            pos=ord(character)-97
            count=nums[pos]
            if count==1:
                return index
        
        return -1
        
#Approach 3:
	from collections import OrderedDict 
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return -1
        if len(s)==1:
            return 0
        new=set(s)
        min=len(s)
        for i in new:
            if s.count(i)==1 and s.index(i)<min:
                min=s.index(i)
        if min!=len(s):
            return min
        else:
            return -1
