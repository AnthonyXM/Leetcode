class Solution1:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1)==0 or len(str2)==0:
            return ""
        if len(str1) < len(str2):
            temp = str1
            str1 = str2
            str2 = temp
        len1, len2 = len(str1), len(str2)
        common_Divisor = [x for x in range(len1,1,-1) if len1%x==0 and len2%x==0] + [1]

        for x in range(len(common_Divisor)):
            s1, s2 = str1[0:common_Divisor[x]] * (len1//common_Divisor[x]), str2[0:common_Divisor[x]] * (len2//common_Divisor[x])
            if str1[0:common_Divisor[x]] == str2[0:common_Divisor[x]] and s1 == str1 and s2 == str2:
                return str1[0:common_Divisor[x]]
        
        return ""

class Solution2:
    def gcd(self, a: int, b: int) -> int:
        return a if b==0 else self.gcd(b, a%b)
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        return str1[0:self.gcd(len(str1), len(str2))]

a = Solution2()
print(a.gcdOfStrings("ABCABC", "ABC"))