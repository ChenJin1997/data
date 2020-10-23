class Solution:
    # 延伸扩展法
    def longestPalindrome(self, s: str) -> str:
        leng = len(s)
        if leng<2:
            return s
        maxlen = 1
        res = s[0]
        for i in range(leng-1):
            # 奇数时
            odd = self.centerSpread(s,i,i)
            # 偶数时
            even = self.centerSpread(s,i,i+1)
            maxstr = odd if len(odd)>len(even) else even
            if len(maxstr)> maxlen:
                maxlen = len(maxstr)
                res = maxstr
        return res


    def centerSpread(self,strs,left,right):
        while left>= 0 and right<= len(strs)-1:
            if strs[left] == strs[right]:
                left -= 1
                right += 1
            else:
                break
        return strs[left+1:right]
a = Solution()
c = a.longestPalindrome("asddVvv")
print(c)

#回文子串，不知道678怎么来的
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
        # 长度
#         for length in range(len(s), -1, -1):
#             for index in range(0, len(s) - length + 1):
#                 sub_string = s[index:length + index]
#                 print(s[index:length + index])
#                 if sub_string == sub_string[::-1]:
#                     return sub_string
# a = Solution()
# c = a.longestPalindrome("abacdef")
# print(c)
