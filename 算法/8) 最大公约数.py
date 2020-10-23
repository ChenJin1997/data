# 获取最大公约数
class getMaxCommenDivisor:

    # 穷举法
    def solution1(self,a,b):
        big = max(a,b)
        small = min(a,b)
        if big % small == 0:
            return small
        for i in range(small//2,1,-1):
            if big % i == 0 and small % i == 0:
                return i

    # 辗转相除法，正整数a和b的最大公约数等于a和b的余数c和b的最大公约数--欧几米的,俩数大的话余数大慢
    def solution2(self,a,b):
        big = max(a,b)
        small = min(a,b)
        if big%small == 0:
            return small
        self.solution2(big%small,small)

    # 更相减损法，正整数a和b的最大公约数等于a和b的差c和b的最大公约数，差值大的话次数多
    def solution3(self,a,b):
        big = max(a,b)
        small = min(a,b)
        if big%small == 0:
            return small
        self.solution2(big-small,small)

a = getMaxCommenDivisor()
c = a.solution3(8,4)
print(c)


