# 列表构件栈
class listStack:
    def __init__(self):
        self.stack = []
        self.size = 0

    # 压栈
    def push(self,data):
        self.stack.append(data)
        self.size += 1

    # 弹栈
    def pop(self):
        if self.stack:
            temp = self.stack.pop()
            self.size -= 1
        else:
            raise Exception("空")
        return temp

    # 返回栈顶
    def peek(self):
        if self.stack:
            return self.stack[-1]

    # 判断是否为空
    def is_empty(self):
        return not bool(self.stack)

    def size(self):
        return self.size

    def __repr__(self):
        return f"{self.stack}"

a=listStack()
# a.push(2)
print(a.is_empty())
