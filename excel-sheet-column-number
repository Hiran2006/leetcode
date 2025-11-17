class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num=0
        for i,l in enumerate(columnTitle[::-1]):
            num+=(ord(l)-ord("A")+1) * 26**i
        return num
        

