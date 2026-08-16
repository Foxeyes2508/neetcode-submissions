class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT={}
        for c in t:
            countT[c]=countT.get(c,0)+1
        left=0
        res=""
        countS={}
        have=0
        need=len(countT)
        res_len=float("inf")
        for r in range(len(s)):
            c=s[r]
            countS[c]=countS.get(c,0)+1
            if c in countT and countS[c]==countT[c]:
                have+=1
            while have==need:
                if r-left+1<res_len:
                    res_len=r-left+1
                    res=s[left:r+1]
                countS[s[left]]-=1
                if s[left] in countT and countS[s[left]]<countT[s[left]]:
                    have-=1
                left+=1
        return res