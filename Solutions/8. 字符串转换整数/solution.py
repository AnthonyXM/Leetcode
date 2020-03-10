class Solution:
    def myAtoi(self, str: str) -> int:
        if len(str) == 0:
            return 0
        
        flag_exist = False
        exist_index = 0
        flag_negative = False
        i = 0
        for x in range(len(str)):
            if str[x] == " ":
                continue
            elif str[x] == "-" and x != len(str)-1:
                flag_negative = True
                flag_exist = True
                exist_index = x+1
                break
            elif str[x] == "+" and x != len(str)-1: # 怎么还有这种事情...
                flag_negative = True
                flag_exist = True
                exist_index = x+1
                break
            elif str[x] in "0123456789":
                flag_exist = True
                exist_index = x
                break
            else:
                break
        if flag_exist:
            for x in range(exist_index,len(str)):
                if str[x] in "0123456789":
                    i = i*10 + int(str[x])
                else:
                    break
        if flag_negative:
            i = -i
        if i > 2147483647:
            return 2147483647
        if i < -2147483648:
            return -2147483648
        return i

a = Solution()
print(a.myAtoi("   -1234 sda"))