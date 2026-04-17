class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res= list(zip(*strs))
        x=""
        for i in res:
            if len(set(i))==1:
                x+=i[0]
            else:
                break
        return x
        

