class Heap:
    def __init__(self):
        self.data_list = []
    def __repr__(self):
        return f"{self.data_list}"
    def get_parent_index(self,index):
        if index<= 0 or index>len(self.data_list)-1:
            return None
        else:
            # 储存右移，相当于除2
            return (index-1)>>1
    # 通过索引调换俩值
    def swap(self,index_a,index_b):
        self.data_list[index_a],self.data_list[index_b] = self.data_list[index_b],self.data_list[index_a]
    def _insert(self,data):
        self.data_list.append(data)
        index = len(self.data_list)-1
        parent = self.get_parent_index(index)
        while parent  and self.data_list[parent]<self.data_list[index]:
            self.swap(parent,index)
            index = parent
            parent = self.get_parent_index(index)
    def insert(self, *data):
        for i in data:
            self._insert(i)
        return  self
    # 弹出堆顶，即弹出最大值
    def pop(self):
        if self.data_list:
            pop_data = self.data_list[0]
            self.data_list[0] = self.data_list[-1]
            del self.data_list[-1]
            self.heapify(0)
            return pop_data
    # 堆化，即把最大的放到堆顶
    def heapify(self,index):
        maxValueIndex = index
        listLen = len(self.data_list)-1
        while True:
            # 判断左孩子是否为空
            if 2*index+1 <= listLen and self.data_list[2*index+1]>self.data_list[maxValueIndex]:
                maxValueIndex = 2*index+1
            if 2 * index + 2 <= listLen and self.data_list[2 * index + 2] > self.data_list[maxValueIndex]:
                maxValueIndex = 2 * index + 2
            if index == maxValueIndex:
                break
            self.swap(index,maxValueIndex)
            index = maxValueIndex



a = Heap()
c = a.insert(12)
d = a.pop()
print(d)
