class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False

        count = {}
        win = {}

        for i in range(len(s1)):
            count[s1[i]] = count.get(s1[i],0) + 1
            win[s2[i]] = win.get(s2[i],0) + 1

        if count == win:
            return True

        l = 0
        for r in range(len(s1),len(s2)):
            win[s2[r]] = win.get(s2[r],0) + 1
            win[s2[l]] -= 1

            if win[s2[l]] == 0:
                del win[s2[l]]
                
            l += 1

            if count == win:
                return True

        return False



