class solution:
# 有序的列表
    # 去重的方法1
    def removeDuplicats1(self,nums):
        # set 去重
        n = len(set(nums))
        i = 0
        while i< n-1:
            if nums[i] == nums[i+1]:
                temp = nums[i+1]
                nums[i+1:len(nums)-1] = nums[i+2:]
                nums[i+n] = temp

    # 用指针去重
    def removeDuplicats2(self, nums):
        slow = 0
        fast = 1
        while fast< len(nums):
            if nums[slow] != nums[fast] :
                slow += 1
                ## [1,2,2,3,3]
                nums[slow] = nums[fast]
                fast += 1
            else:
                fast += 1
        return slow+1

    # 移除重复次数大于2的元素
    def delDouble(self,nums):
        count = 1
        slow = 0
        fast = 1
        while fast<len(nums):
            if nums[slow] == nums[fast]:
                count += 1
                if count == 2:
                    slow += 1
                    nums[slow] = nums[fast]
            else:
                slow += 1
                nums[slow] = nums[fast]
                count = 1
            fast += 1
        for i in range(slow+1):
            print( nums[i] , end="->")

    # 移动零
    def removeZero(self,nums):
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] == 0:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        for i in range(slow,len(nums)):
            nums[i] = 0
        for i in range(len(nums)):
            print( nums[i] , end="->")

    # 删除指定数
    def delValue(self,nums,value):
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] == value:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        for i in range(slow):
            print( nums[i] , end="->")


a =[0,0,1,1,1,1,2,3,3]
b= solution()
c = b.delDouble(a)
print( c)