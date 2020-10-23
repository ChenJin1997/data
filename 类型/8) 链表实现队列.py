class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"{self.data}"

class Link2Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def __repr__(self):
        cursor = self.front
        result = ""
        while cursor:
            result += f"{cursor}" + "-->"
            cursor = cursor.next
        return result

    def enQueue(self,data):
        new_node = Node(data)
        if self.front:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = new_node
            self.rear = new_node
        self.size += 1

    def deQueue(self):
        if self.front:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            self.size -= 1
        else:
            raise Exception("空")

a = Link2Queue()
a.enQueue(2)
a.deQueue()
print(a)


