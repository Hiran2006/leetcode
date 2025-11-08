class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1
        low,high = 1,x
        while(low<high):
            mid = (low+high)//2
            x2 = mid*mid
            if(x2==x):
                return mid
            if(x2 > x):
                high = mid-1
            else:
                low = mid+1
        return low if low*low<=x else low-1
        

        
