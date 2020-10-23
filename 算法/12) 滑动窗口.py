# 给定一个正整数数组和一个正整数，找出大于或等于该数的长度最小的连续数组的长度
def minSubArrayLen(s,nums):
    # float('inf')正无穷
    left,sums,res = 0,0,float('inf')
    for right in range(len(nums)):
        sums += nums[right]
        while sums>=s:
            if right-left+1<res:
                res = right-left+1
            sums -= nums[left]
            left += 1
    return 0 if res == float('inf') else res

print(minSubArrayLen(5,[2,1,3,4,1]))


