class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        dicti={}
        count=0
        for stones in S:
            if stones not in dicti:
                dicti[stones]=1
            else:
                dicti[stones]+=1
        
        for jewels in J:
            if jewels in dicti:
                count+=dicti[jewels]
                
        return count