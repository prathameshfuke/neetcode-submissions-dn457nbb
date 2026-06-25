class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        countT, countS = {}, {}

        for i in range(len(t)):
            countS[s[i]] = 1 + countS.get(s[i],0) #we are using get to prevent Keyerror so while going thru chareceters first time we dont get keyerrors in a string
            countT[t[i]] = 1 + countT.get(t[i],0)
        for c in countS:
            if countS[c]!=countT.get(c,0):
                return False
        return True