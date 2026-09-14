class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')','{':'}','[':']'}
        stack = []

        for i in s:
          
            if i in "{([":
                stack.append(i)

            else:
                if stack and d[stack[-1]] == i:
                    stack.pop()
                else:
                    return False

        

        if not stack:
            return True

        return False
