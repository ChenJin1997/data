class PriorityQueue:
    def __init__(self):
        self.array = []
        self.size = 0
    # def __repr__(self):
    #     return f"{self.array}"
    def _enQueue(self,data):
        self.array.append(data)
        self.size += 1
        self.heapity_up()
    def enQueue(self,*data):
        for i in data:
            self._enQueue(i)
        return self
    def deQueue(self):
        if self.array:
            remove_node = self.array[0]
            self.array[0] = self.array[-1]
            del self.array[-1]
            self.size -= 1
            self.heapity_down()
            return remove_node
        else:
            return "空"
    def swap(self,index_a,index_b):
        self.array[index_a],self.array[index_b] = self.array[index_b],self.array[index_a]
    # 向上堆化，结点上移
    def heapity_up(self):
        newIndex = self.size-1
        parentIndex = (newIndex-1)>>1
        while newIndex > 0 and self.array[newIndex]>self.array[parentIndex]:
            self.swap(newIndex,parentIndex)
            newIndex = parentIndex
            parentIndex = (newIndex-1)>>1
    # 向下
    def heapity_down(self):
        index = 0
        maxIndex = index
        while True:
            if 2*index+1<self.size and self.array[2*index+1]>self.array[maxIndex]:
                maxIndex = 2*index+1
            if 2*index+2<self.size and self.array[2*index+2]>self.array[maxIndex]:
                maxIndex = 2*index+2
            if maxIndex == index:
                break
            self.swap(index, maxIndex)
            index = maxIndex
    def outPut(self):
        for i in self.array:
            print(i)

a = PriorityQueue()
c = a.enQueue(1,2,3,4,8,5)
c = a.deQueue()
a.outPut()

