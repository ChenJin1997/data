# 数组的低层是列表
class array:
    #给了10就可以不传参
    def __init__(self,capacity=10):
        self.array = [None]*capacity
        self.size = 0

    def output(self):
        for i in range(self.size):
            # end 不换行
            print(self.array[i],end = "->")
    # 增加链表位置
    def addcapacity(self):
        new_array = [None]*len((self.array)+1)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def insert(self,index,element):
        # 插入到有效后面的后面时候
        if index<0 or index > self.size:
            raise IndexError("越界")
        # 插入到最后或者中间但是满时
        if index >= len(self.array) or self.size>= len(self.array):
            self.addcapacity()
        # 也可以用切片 self.array[index+1:self.size+1] = self.array[index:self.size]
        for i in range(self.size-1,index-1,-1):
            self.array[i+1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def remove(self,index):
        #越界：index小于零或者 满的时候
        if index <0 or index >= self.size:
            raise IndexError("越界")
        # 移除数组最后值时
        if self.size == len(self.array):
            self.addcapacity()
        for i in range(index,self.size):
            self.array[i] = self[i+1]
        self.size -= 1

    # 反转数组
def reverse(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    print(nums)


a= array(10)
a.insert(0,0)
a.insert(1,1)
a.insert(2,2)
a.insert(3,3)
a.insert(4,4)
a.output()

a.insert(2,100)

a.output()


