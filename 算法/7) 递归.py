# 斐波那数列
def fid(n):
    if n <= 0:
        return None
    if n <= 2:
        return 1
    return fid(n-1) + fid(n-2)

# 阶层
def jieCeng(n):
    if n < 0 :
        return None
    if n <= 2:
        return n
    return n*jieCeng(n-1)

# 一青蛙跳台阶，每次跳一层或俩层，共几种方法
def qinWa(n):
    if n <= 2:
        return n
    # 在倒数第二层有几种跳法，在倒数第三层有几种跳法
    return qinWa(n-1)+qinWa(n-2)

print(qinWa(5))