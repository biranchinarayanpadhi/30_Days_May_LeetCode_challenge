#Brute Force Approach(Accepted):
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_s=len(s)
        if len_s == 1:
            return s
        frequency_map={}
        for element in s:
            if element not in frequency_map:
                frequency_map[element]=1
            else:
                frequency_map[element]+=1
        temp={}
        for key in frequency_map:
            if frequency_map[key] not in temp:
                temp[frequency_map[key]]=[key]
            else:
                temp[frequency_map[key]].append(key)   
        result_str=""
        value=len_s
        while value>=0:
            if value in temp:
                for element in temp[value]:
                    count=value
                    while count>0:
                        result_str+=element
                        count-=1
            value-=1
        return result_str
                
#Approach 2-optimized in terms of appending strings:
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_s=len(s)
        if len_s == 1:
            return s
        frequency_map={}
        for element in s:
            if element not in frequency_map:
                frequency_map[element]=1
            else:
                frequency_map[element]+=1
        temp={}
        for key in frequency_map:
            if frequency_map[key] not in temp:
                temp[frequency_map[key]]=[key]
            else:
                temp[frequency_map[key]].append(key)   
        result_str=[]
        value=len_s
        while value>=0:
            if value in temp:
                for element in temp[value]:
                    count=value
                    while count!=0:
                        result_str.append(element)
                        count-=1
            value-=1
        return ''.join(result_str)
                
#Best Appraoch(Optimized-N*k)
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_s=len(s)
        if len_s == 1:
            return s
        frequency_map={}
        for element in s:
            if element not in frequency_map:
                frequency_map[element]=1
            else:
                frequency_map[element]+=1
        temp={}
        for key in frequency_map:
            if frequency_map[key] not in temp:
                temp[frequency_map[key]]=[key]
            else:
                temp[frequency_map[key]].append(key)
        result_str=[]
        value=len_s
        while value>=0:
            if value in temp:
                for element in temp[value]:
                    result_str.append(element*value)        
            value-=1
        return ''.join(result_str)
                
        