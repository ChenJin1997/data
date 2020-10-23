class node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"{self.data}"

class linkedlist:
    # 初始化
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        result = ""
        cursor = self.head
        while cursor:
            result += f"{cursor}-->"
            cursor = cursor.next
        return result + "end"

    # 索引
    def get(self,index):
        cursor = self.head
        for i in range(index):
            cursor = cursor.next
        return cursor

    # 插入
    def insert(self,index,data):
        new_node = node(data)
        # 边界
        if index<0 or index>self.size:
            raise IndexError("越界")
        # 空
        if self.size == 0 :
            self.head = new_node
            self.tail = new_node
        # 头
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        # 尾
        elif index == self.size-1:
            self.tail.next = new_node
            self.tail = new_node

        else:
            before = self.get(index-1)
            new_node.next = before.next
            before.next = new_node
        self.size += 1

    # 删除
    def remove(self,index):
        if index<0 or index>=self.size:
            raise Exception("越界")

        else:
            if index == 0:
                remove_node = self.head
                self.head = remove_node.next
                remove_node.next = None

            elif index == self.size-1:
                before = self.get(index - 1)
                remove_node = before.next
                before.next = None
                self.tail = before

            else:
                before = self.get(index-1)
                remove_node = before.next
                before.next = remove_node.next
            self.size -= 1
            return f"{remove_node}"

    # 链表反转
    def reverse(self):
        cursor = self.head
        before = None
        self.tail = self.head
        while cursor:
            after = cursor.next
            cursor.next = before
            before = cursor
            cursor = after
        self.head = before

a = linkedlist()
a.insert(0,2)
a.insert(1,4)
a.insert(2,6)
a.remove(0)
print(a)
