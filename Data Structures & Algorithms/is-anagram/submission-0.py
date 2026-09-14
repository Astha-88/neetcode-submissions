class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        res = {}
        for i in range(len(s)):
            res[s[i]] = 1 + res.get(s[i],0)
            res[t[i]] = res.get(t[i],0) - 1

        for i in range(len(res)):
            if res[s[i]] != 0:
                return False
        return True