# 三数和
def ShangShuHe(nums):
    rec = []
    for i in range(len(nums)-2):
        # 优化
        if nums[i] == nums[i+1]:
            continue
        left = i+1
        right = len(nums)-1
        if nums[i] + nums[left] + nums[right] < 0:
            right -= 1
        elif nums[i] + nums[left] + nums[right] > 0:
            left += 1
        else:
            # rec += [nums[i],nums[left],nums[right]]
            rec.append([nums[i],nums[left],nums[right]])
            # 优化
            while left < right and nums[left] == nums[left+1]:
                left += 1
            while left < right and nums[right] == nums[right-1]:
                right -= 1
            left += 1
            right -= 1
        return rec

# 最接近三数之和
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        zuiSums = nums[0] + nums[1] + nums[2]
        if len(nums) == 3:
            return zuiSums
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curSums = nums[i] + nums[left] + nums[right]
                if abs(zuiSums - target) > abs(curSums - target):
                    zuiSums = curSums
                if curSums > target:
                    right -= 1
                elif curSums < target:
                    left += 1
                else:
                    return target
        return zuiSums

# 找三角形的有效个数
def tirangleNum(nums):
    nums.sort()
    count = 0
    for i in range(len(nums)-2):
        left = i+1
        for right in range(left+1,len(nums)):
            while left<right:
                print(nums[i], nums[left], nums[right])
                if nums[i] + nums[left]>nums[right]:
                    count += 1
                    left += 1
                else:
                    left+=1
    return count

# def tirangleNum(nums):
#     nums.sort()
#     count = 0
#     for i in range(2,len(nums)):
#         left = 0
#         right = i-1
#         while left<right:
#             if nums[left] + nums[right] > nums[i]:
#                 count += right-left
#                 right -= 1
#             else:
#                 left += 1
#     return count

c = ShangShuHe([-2,-1,-1,0,1,1,2])
c = tirangleNum([1,2,3,4,5,6])
print(c)