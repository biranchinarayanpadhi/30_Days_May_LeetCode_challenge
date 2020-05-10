class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) == 0:
            return 1
        
        #Counting the no of uniq_people and coutning the majority_trusted_people
        trust_person_dicti={}
        trusting_person_frequency=[0]*(N+1)
        for pairs in trust:
            person=pairs[0]
            trusted_entity_of_person=pairs[1]
            trusting_person_frequency[trusted_entity_of_person]+=1
            if person not in trust_person_dicti:
                trust_person_dicti[person]=[trusted_entity_of_person]
            else:
                trust_person_dicti[person].append(trusted_entity_of_person)
        
        #Here i am finding who is the maximum_trusted_judge and what is the  majority votes
        maxi_trust=0
        majority_trust_person=1
        for index in range(1,N+1):
            if maxi_trust<=trusting_person_frequency[index]:
                majority_trust_person=index
                maxi_trust=trusting_person_frequency[index]
        
        #here i am finding out the validity of 3rd condition i.e how many people are present with majority votes
        #if it is more than 2 then 3rd cindition is invalid
        majority_counting_person=0
        for index in range(N+1):
            if maxi_trust == trusting_person_frequency[index]:
                majority_counting_person+=1
        if majority_counting_person >1:
            return -1
        
    
        #here i am finding out the validity of 1st two consitions
        trusted_judge=majority_trust_person #in this line i am considering the trusted_judge who have majority votes
        if trusted_judge not in trust_person_dicti:
            for person in trust_person_dicti:
                if trusted_judge not in trust_person_dicti[person]:
                    return -1
            return trusted_judge
        else:
            return -1