class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)<=2 or numRows==1:
            return s

        r = [" "]*len(s)

        # __       | __       | __       | __
        # __    __ | __    __ | __    __ | __
        # __ __    | __ __    | __ __    | __
        # __       | __       | __       |

        group = (len(s)-1)//(2*numRows-2)+1
        # 首行单独计算
        for x in range((len(s)-1)//(2*numRows-2)+1):
            r[x] = s[x*(2*numRows-2)]

        # 靠左一共 (numRows-2)*((len(s)-*line*)//(2*numRows-2)+1)个字符
        accu = (len(s)-1)//(2*numRows-2)+1
        for line in range(2, numRows):
            for x in range((len(s)-line)//(2*numRows-2)+1):
                r[accu + 2*x] = s[line-1 + x*(2*numRows-2)]
            for x in range((len(s)-1-(2*numRows-2-line+1))//(2*numRows-2)+1):
                r[accu + 1 + 2*x] = s[2*numRows-2-line+1 + x*(2*numRows-2)]
            accu += (len(s)-line)//(2*numRows-2)+(len(s)-1-(2*numRows-2-line+1))//(2*numRows-2) + 2

        # 末行测试
        for x in range((len(s)-numRows)//(2*numRows-2)+1):
            r[len(s)-(len(s)-numRows)//(2*numRows-2)+x-1] = s[numRows-1+x*(2*numRows-2)]

        return "".join(r)

a = Solution()
print(a.convert("PAYPALISHIRING", 4))