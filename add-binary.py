class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a)-1
        j = len(b)-1
        carry = 0
        result = []
        while(i>=0 or j >=0 or carry == 1):a
            da = int(a[i]) if i>=0 else 0
            db = int(b[j]) if j>=0 else 0
            r = da+db+carry
            result.append(str(r%2))
            carry = r//2
            i-=1
            j-=1
        
        return "".join(result[::-1])
            
        
