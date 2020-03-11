class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        t = s//3
        if t*3 != s:
            return False
        t1 = 0
        for x in range(len(A)-2):
            t3 = 0
            t1 += A[x]
            if t1 == t:
                for y in range(len(A)-1,x+1,-1):
                    t3 += A[y]
                    if t3 == t:
                        return True
        return False
