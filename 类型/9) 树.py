# 所有非叶子节点都有左右俩孩子  二叉树
# 所有非叶子节点都有左右孩子，且所有叶子节点都在同一层级上  满二叉树
# 所有非叶子节点都有左右孩子，且所有叶子节点都在同一层级上且齐全  完全二叉树
# 结点
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None
#     def __repr__(self):
#         return f"{self.data}"
# # 二叉树
# class BinaryTree:
#     def __init__(self):
#         self.root = None
#     # 添加
#     def _add(self,data):
#         new_node = Node(data)
#         if self.root is None:
#             self.root = new_node
#             return "ok"
#         else:
#             temp = [self.root]
#             while True:
#                 # 比如：temp第一次为[0],第二次为[1,2],第三次为[2,3,4]
#                 # pop_node为列表弹出的第一个
#                 pop_node = temp.pop(0)
#                 if pop_node.left is None:
#                     pop_node.left = new_node
#                     return  "ok"
#                 if pop_node.right is None:
#                     pop_node.right = new_node
#                     return  "ok"
#                 temp.append(pop_node.left)
#                 temp.append(pop_node.right)
#     # 不定长传参
#     def add(self,*data):
#         for i in data:
#             self._add(i)
#         return self
#     # 找父节点
#     def get_parent(self,data):
#         if self.root.data == data:
#             return None
#         temp = [self.root]
#         rec = []
#         while temp:
#             pop_node = temp.pop(0)
#             if pop_node.left and (pop_node.left.data == data):
#                 rec.append(pop_node.data)
#             if pop_node.right and (pop_node.right.data == data):
#                 rec.append(pop_node.data)
#             else:
#                 if pop_node.left:
#                     temp.append(pop_node.left)
#                 elif pop_node.right:
#                    temp.append(pop_node.right)
#         return rec
#
#
# a = BinaryTree()
# c = a.add(1,5,6,9,7)
# c = a.get_parent(10)
# print(c)

# a.get_parent(4)


# 导入模块
from pprint import pformat

class Node:
    def __init__(self,data,parent = None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.data)
        return pformat({"%s"%(self.data):(self.left,self.right)},indent= 1 )
        # return pformat({f"{self.data}:{self.left, self.right}"}, indent=1)

# 二叉搜索树
class BinarySearchTree:
    def __init__(self,root = None):
        self.root = root
    # 表示方法
    def __str__(self):
        return str(self.root)
    # 插入
    def _insert(self,data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            parent_node = self.root
            while True:
                if data < parent_node.data:
                    if parent_node.left is None:
                        parent_node.left = new_node
                        break
                    parent_node = parent_node.left
                else:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    parent_node = parent_node.right
            new_node.parent = parent_node
    # 不定长传参
    def insert(self,*data):
        for i in data:
            self._insert(i)
        return self
    # 查找
    def search(self,data):
        if self.root:
            node = self.root
            while node and node.data != data:
                node = node.left if data < node.data else node.right
            return node
        else:
            return "空"

    # 是否为右结点
    def is_right(self,node):
        return node == node.parent.right

    # 移除
    def remove(self,data):
        remove_node = self.search(data)
        if remove_node:
            if remove_node.left is None and remove_node.right is None:
                self._reassign_node(remove_node, None)
            elif remove_node.left is None:
                self._reassign_node(remove_node, remove_node.right)
            elif remove_node.right is None:
                self._reassign_node(remove_node, remove_node.left)
            else:
                reassign_node = self.get_max(remove_node.left)
                self.reomve(reassign_node.data)
                remove_node.data = reassign_node.data
        else:
            return "无"

    # 将输入的第一个更换为第二个
    def _reassign_node(self, be_reassign, reassign_node):
        if reassign_node :
            reassign_node.parent = be_reassign.parent
        if be_reassign.parent:
            if self.is_right(be_reassign):
                be_reassign.parent.right = reassign_node
            else:
                be_reassign.parent.left = reassign_node
        else:
            self.root = reassign_node

    # 获取最大
    def get_max(self,node = None):
        if node is None:
            node = self.root
        if self:
            while node.right :
                node = node.right
        return node

    # 通过递归前序遍历树
    def preOrder(self,node):
        if not node:
            return None
        print(node.data)
        self.preOrder(node.left)
        self.preOrder(node.right)


    # 通过栈前序遍历树
    def preOrder2(self,node):
        temp =[node]
        while temp:
            print(node.data)
            if node.right:
                temp.append(node.right)
            if node.left:
                temp.append(node.left)
            node = temp.pop()

    # 通过递归中序遍历树
    def inOrder(self,node):
        if not node:
            return None
        self.inOrder(node.left)
        print(node.data)
        self.inOrder(node.right)

    # 通过栈中序遍历树
    def inOrder2(self,node):
        temp = []
        while node or temp:
            while node:
                temp.append(node)
                node = node.left
            if temp:
                node = temp.pop()
                print(node.data)
                node = node.right
    # 用栈实现后序遍历树（汉诺塔思想）
    def poetOrder(self,node):
        if node is None:
            return None
        stack1 = []
        stack2 = []
        stack1.append(node)
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while stack2:
            print(stack2.pop().data,end=" ")

    # 层序遍历
    def levelOrder(self,node):
        from queue import Queue
        queue = Queue()
        queue.put(node)
        while queue:
            temp = queue.get()
            print(temp.data)
            if temp.left:
                queue.put(temp.left)
            if temp.right:
                queue.put(temp.right)



a = BinarySearchTree()
b = a.insert(4,6,5,1,3)
print(b)
a.levelOrder(a.root)


