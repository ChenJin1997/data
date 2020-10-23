from random1 import random2

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"{self.data}"



class Sort:

    # 冒泡排序
    def bubbleSort(self,nums):
        size = len(nums)-1
        for i in range(size):  # 控制轮数
            # 只要后面有一大循环没调换，则后面已经排序好了，可直接跳出
            flag  = True
            for j in range(size-i): # 调换内循环相邻值
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                    flag = False
            if flag:
                break
        return nums

    # 选择排序
    def selectSort(self,nums):
        for i in range(len(nums)- 1):  # 控制轮数
            minIndex = i
            for j in range(i+1,len(nums)):# 找到内层循环极值索引
                if nums[j] < nums[minIndex]:
                    minIndex = j
            nums[minIndex], nums[i] = nums[i], nums[minIndex]
        return nums


    # 插入排序,扑克牌排序原理,左侧排好，右侧乱序，每次从右侧拿一张差进去
    def insertSort(self,nums):
        if len(nums)<=1:
            return nums
        for right in range(1,len(nums)): # 右边乱序的牌，左边第一张默认排好
            # 需赋变量，在下面right会变
            temp = nums[right]
            for left in range(right): # 左边排好的牌
                if temp<nums[left]:
                    nums[left+1:right+1] = nums[left:right]
                    nums[left] = temp
                    break
        return nums




    # 归并排序  将数组细分然后12排序，34排序，1234排序
    def mergeSort(self,nums):
        if len(nums)<= 1:
            return nums
        mid = len(nums)>>1
        left,right = nums[:mid],nums[mid:]
        return self.merge(self.mergeSort(left),self.mergeSort(right))
    def merge(self,leftNums, rightNums):
        rec = []
        while leftNums and rightNums:
            if leftNums[0]>rightNums[0]:
                rec.append(rightNums.pop(0))
            else:
                rec.append(leftNums.pop(0))
            # 追加余下数组
        rec.extend(leftNums)
        rec.extend(rightNums)
        return rec
    # 指针
    # def merge2(self,leftNums, rightNums):
    #     rec = []
    #     i = 0
    #     j = 0
    #     while i<len(leftNums) and j<len(rightNums):
    #         if leftNums[i]>rightNums[j]:
    #             rec.append(rightNums[j])
    #             j+=1
    #         else:
    #             rec.append(leftNums[i])
    #             i+=1
    #     rec.extend(leftNums[i:])
    #     rec.extend(rightNums[j:])
    #     return rec


    # 快排 12 和34分开，再1和2分开排序，3和4分开排序
    def quickSort(self,nums,start,end):
        if start>=end:
            return
        mid = self.partition2(nums,start,end)
        self.quickSort(nums, start, mid-1)
        self.quickSort(nums, mid+1,end)
        return nums

    def partition(self,nums,start,end):
        left = start + 1
        right = end
        while left<= right:
            while left<= right and nums[left]<nums[start]:
                left += 1
            while left<= right and nums[right]>=nums[start]:
                right -= 1
            if left<right:
                nums[left],nums[right] = nums[right],nums[left]
        nums[start],nums[right] = nums[right],nums[start]
        return right

    # 单指针
    def partition2 (self, nums, start, end):
        curr = start
        for i in range(start+1,end+1):
            if nums[i] < nums[start]:
                curr += 1
                nums[curr],nums[i] = nums[i],nums[curr]
        nums[curr],nums[start] = nums[start],nums[curr]
        return curr

    # 计数排序
    # def donKnow(self,nums):
    #     dict = {}
    #     for i in range(len(nums)):
    #         count = 0
    #         for j in range(len(nums)):
    #             if nums[j] == nums[i]:
    #                 count += 1
    #         dict[nums[i]] = count
    #     return dict

    # 计数排序
    def countSort(self,nums):
        new_nums = []
        # 新建一个全为零计数数组，长度为什么加一，考虑0
        arr_count = [0]*(max(nums)+1)
        # 计数
        for i in nums:
            arr_count[i] += 1
        # i为值，j为次数 ，为什么加一，不包尾
        for i in range(max(nums)+1):
            for j in range(arr_count[i]):
                new_nums.append(i)
        return new_nums

    # 桶排序  分层次再调用别的排序方法
    def bucketSort(self,nums):
        # 造桶
        buckets = [[] for i in range(len(nums))]
        # 定位元素属于哪个桶并放入
        for i in range(len(nums)):
            # 归一化后处理 不减1为值的区域，减一是下标的值
            bucketNum = int((nums[i]-min(nums))/(max(nums)-min(nums))*(len(nums)-1))
            bucket = buckets[bucketNum]
            bucket.append(nums[i])
        # 桶内排序
        for i in range(len(nums)):
            buckets[i].sort()
        # 输出
        rec = []
        for i in buckets:
            for j in i:
                rec.append(j)
        return rec





    # def quickSort(self,nums):
    #     if len(nums)<=1:
    #         return nums
    #     base = nums[0]
    #     left = [i for i in nums[1:] if i <base]
    #     right = [i for i in nums[1:] if i >=base]
    #     return self.quickSort(left)+[base]+self.quickSort(right)


    # 链表插入排序
    def insertLinkSort(self,head):
        dummp = None
        # 创建新链表
        left = dummp
        right = head
        while right:
            temp = right.next
            while left.next and left.next.data<right.data:
                left = left.next
            right.next = left.next
            left.next = right
            right = temp
            left = dummp
        return dummp.next




a = Sort()
for i in range(1):
    nums = random2.randomList(10,10)
    print(nums)
    c = a.bucketSort(nums)
    print(c)

