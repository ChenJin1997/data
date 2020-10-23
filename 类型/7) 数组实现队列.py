# 数组实现队列
class Array2Queue:
    def __init__(self):
        self.entries = []  #条目
        self.size = 0
    def __repr__(self):
        # [1:-1]是将列表的[]转成字符串后去掉，即拿[1,2,3]的第二个各
        return "<"+ str(self.entries)[1:-1] +">"
    def enQueue(self,data):
        self.entries.append(data)
        self.size += 1
    def deQueue(self):
        if self.entries:
            temp = self.entries[0]
            self.entries = self.entries[1:]
            self.size -= 1
        else:
            raise Exception("空")
    def get(self,index):
        if index< 0 or index>=self.size:
            raise IndexError("越界")
        return  self.entries[index]


a = Array2Queue()
a.enQueue(2)
a.enQueue(2)

print(a)

