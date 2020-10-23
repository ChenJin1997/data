## next记录的是内存地址

#新建结点类
class node:
    #结点的数据,指向与长度，next初始化为空
    def __init__(self,data):
        self.data = data
        self.next = None
        self.size = 0
    #repr，将结点用字符串显示
    def __repr__(self):
        # 注意  不能只输出self.data，变量不等于字符
        return  "node({})".format(node.data)


