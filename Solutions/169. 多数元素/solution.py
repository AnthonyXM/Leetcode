from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n1, n2 = [], []
        for x in nums:
            if n1==[] and n2==[]:
                n1 += [x]
            elif n1==[]:
                if n2[0]==x:
                    n2 += [x]
                else:
                    n2 = n2[:-1]
            elif n2==[]:
                if n1[0]==x:
                    n1 += [x]
                else:
                    n1 = n1[:-1]
            else:
                if n1[0]==x:
                    n1 += [x]
                elif n2[0]==x:
                    n2 += [x]
                else:
                    n1 = n1[:-1]
        return n1[0] if len(n1) > len(n2) else n2[0]

a = Solution()
print(a.majorityElement([1]))