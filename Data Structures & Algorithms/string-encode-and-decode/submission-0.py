class Solution:

    def encode(self, strs: List[str]) -> str:
        newstr = ""
        for i in strs:
            newstr += i + "~"
        return newstr

    def decode(self, s: str) -> List[str]:
        newlist = s.split("~")
        return newlist[:-1]

