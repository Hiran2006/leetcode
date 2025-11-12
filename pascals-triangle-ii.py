class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        n = rowIndex
        r = 1
        pascal=[1]
        for i in range(1,rowIndex):
            pascal.append(n//r)
            n*=rowIndex-i
            r*=i+1
        pascal.append(1)
        return pascal

        