class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        excel=[]
        while(columnNumber!=0):
            columnNumber-=1
            num = columnNumber%26
            columnNumber=columnNumber//26
            excel.append(chr(ord('A')+num))
        
        return "".join(reversed(excel))