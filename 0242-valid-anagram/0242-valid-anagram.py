class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check lenght is that valid
        if len(s) != len(t):
            return False
        #create 2 hashmaps
        countS, countT = {},{}
        
        for i in range(len(s)):
            #get the count number and set the key and value for the hashmap
            #increase count numb if not exist set default value = 0
            
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        #compare character of 2 hashmaps
        # and if that CHARACTER doesn't exist set default value = 0
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
            
        return True