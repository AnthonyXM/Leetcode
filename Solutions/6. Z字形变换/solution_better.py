# 这次是真的better solution了

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s) :return s
        r,j,k=['']*numRows,0,1
        for i in s:
            r[j]+=i
            j+=k
            if j==0 or j==numRows-1 : k=-k
        return "".join(r)

a = Solution()
print(a.convert("PAYPALISHIRING", 4))

# 日 看完这个解答 我觉得自己的智商受到了侮辱quq