# 字典树结点
class TireNode:
    def __init__(self):
        self.data = {}
        self.is_work = False
    def __repr__(self):
        return f"{self.data}"

# 字典树  {s:{o:{m:{e}}}}
class Tire:
    def __init__(self):
        self.root = TireNode()

    # 插入
    def _insert(self,work):
        # 插入结点时从根结点开始判断
        node = self.root
        # 遍历插入单词的每一个字符
        for char in work:
            # 获取该字符键的值，如果不存在则新建
            child = node.data.get(char)
            if child is None:
                node.data[char] = TireNode()
            # 如果存在则结点下移找下一个
            node = node.data[char]
        node.is_work = True
    def insert(self,*work):
        for i in work:
            self._insert(i)
        return self

    # 查找单词是否存在
    def search(self,work):
        node = self.root
        for char in work:
            node = node.data.get(char)
            if node is None:
                return False
        return node.is_work

    # 判断前缀是否存在
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            node = node.data.get(char)
            if node is None:
                return False
        return True



a = Tire()
c = a.insert('apple')
print(c)
