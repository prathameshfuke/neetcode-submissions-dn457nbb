from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result = result + str(len(s)) + "#" + s
        return result


    def decode(self, strs: str) -> List[str]:
        result,i = [], 0
        while i < len(strs):
            j = i 
            while strs[j]!="#":
                j=j+1
            length = int(strs[i:j])
            result.append(strs[j+1:j+1+length])
            i = j+1+length
        return result

