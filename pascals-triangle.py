class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if j in [0,i]:
                    row.append(1)
                else:
                    row.append(pascal[i-1][j-1]+pascal[i-1][j])
            pascal.append(row)
        return pascal