class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        seen={}
        for i in strs:
            a=str(sorted(i))
            if a in seen:
                ans[seen[a]].append(i)
            else:
                seen[a]=len(ans)
                ans.append([i])

        return ans