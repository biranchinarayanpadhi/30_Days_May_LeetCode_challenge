class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dicti={}
        for element in magazine:
            if element not in magazine_dicti:
                magazine_dicti[element]=1
            else:
                magazine_dicti[element]+=1
                
        for element in ransomNote:
            if element not in magazine_dicti:
                return False
            else:
                magazine_dicti[element]-=1
                if magazine_dicti[element]<0:
                    return False
        
        return True
        