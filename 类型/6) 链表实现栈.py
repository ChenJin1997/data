class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"{self.data}"

class linkStack:
    def __init__(self):
        self.top = None
        self.size = 0

    #  压栈
    def push(self,data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top  = node
        self.size += 1

    # 弹栈
    def pop(self):
        if self.top:
            node = self.top
            self.top = self.top.next
            node.next = None
            self.size -= 1
            return  node
        else:
            raise Exception("空")




