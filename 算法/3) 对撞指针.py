# 有序列表俩数和等于指定数
# 快慢指针
def FindTowSum(nums,target):
    front = 0
    rear = len(nums)-1
    while front<rear:
        if nums[front] + nums[rear] == target:
            print(front,rear)
            front += 1
            rear -= 1
        else:
            if nums[front] + nums[rear]<target:
                front += 1
            else:
                rear -= 1

# 利用字典
def FindTowSum2(nums,target):
    # 注意该字典里key为列表的值，val为列表的索引
    new_dict = {}
    for i in range(len(nums)):
        temp = target - nums[i]
        # 如果差值在字典里
        if temp in new_dict:
            return i,new_dict[temp]
        else:
            new_dict[nums[i]] = i

# 暴力破解
class Solution:
    def twoSum(self, nums, target: int) :
        for index1,value1 in enumerate(nums):
            for index2, value2 in enumerate(nums[index1+1:]):
                if value1 + value2 == target:
                    return index1,index2+index1+1

# 反转数组
def reverse(nums):
    left = 0
    right = len(nums)-1
    while left<right:
        nums[left],nums[right] = nums[right],nums[left]
        left += 1
        right -= 1
    print(nums)

reverse([1,2,3])