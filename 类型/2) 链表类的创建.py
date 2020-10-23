##边界   self.head是否存在
##遍历   cursor
##self.head 标明链表头部在哪

# 新建结点类
class node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = None
    def __repr__(self):
        # 注意，不能只输出self.data，变量不等于字符
        return "node({})".format(self.data)


# 新建链表类
class linkedlist:
    # 初始化头为空
    def __init__(self):
        self.head = None

    # 显示
    def __repr__(self):
        result = ""
        cursor = self.head
        while cursor:
            result += "{} -> ".format(cursor)
            # 或result += f"{cursor} -> "
            cursor = cursor.next
        return result + "end"

    # 插入头
    def insert_head(self,data):
        new_data = node(data)
        if self.head:
            new_data.next = self.head
        self.head = new_data

    # 追加
    def appent(self, data):
        new_data = node(data)
        if self.head:
            cursor = self.head
            while cursor.next:
                cursor = cursor.next
            cursor.next = new_data
        else:
            self.insert_head(data)

    # 插入
    def insert(self,i,data):
        new_data = node(data)
        if self.head is None or i == 1:
            self.head = new_data
        else:
            try:
                after = self.head
                j = 1
                while j<i:
                    before = after
                    after = before.next
                    j += 1
                before.next = new_data
                new_data.next = after
                self.head = before
            except:
                print("报错")
                exit()

    # 删除头
    def del_head(self):
        if self.head:
            self.head = self.head.next

    # 删除尾
    def del_tail(self):
        cursor = self.head
        while cursor.next.next:
            cursor = cursor.next
        cursor.next = None

    # 列表转链表
    def list_to_link(self,list):
        self.head = node(list[0])
        cursor = self.head
        for i in list[1:]:
            Data = node(i)
            cursor.next = Data
            cursor = cursor.next

    # 链表反转
    def reverse(self):
        cursor = self.head
        before = None
        while cursor:
            after = cursor.next
            cursor.next = before
            before = cursor
            cursor  = after
        self.head = before

    # 索引
    def __getitem__(self, index):
        cursor = self.head
        if cursor is None:
            raise IndexError("the linked is empty")
        # 走的次数
        for i in range(0,index):
            if cursor.next is None:
                raise  IndexError(" the index is long ")
            cursor = cursor.next
        return cursor

    # 索引的输出/可省略
    def get(self,index):
        return  self.__getitem__(index)

    # 更改值
    def __setitem__(self, index,data):
        cursor = self.head
        if cursor is None:
            raise IndexError("the linked is empty")
        for i in range(index):
            if cursor.next is None:
                raise IndexError("the index is long")
            cursor = cursor.next
        cursor.data = data
        return cursor

    # 去指定值 (利用虚拟点)
    def removeValue(self,value):
        dummy = None
        dummy.next = node.head
        cursor = dummy
        while cursor.next:
            if cursor.next.data == value:
                temp = cursor.next
                cursor.next = cursor.next.next
                temp.next = None
            else:
                cursor = cursor.next
        # 返回头
        return dummy.next


    # 俩俩交换  1234 -》 2143
    def towTowChange(self,head):
        dummy = node(0)
        dummy.next = head
        cursor = dummy
        while cursor.next and cursor.next.next:
            slow = cursor.next
            fast = cursor.next.next
            slow.next = fast.next
            fast.next = slow
            cursor.next= fast
            cursor = slow
            # cursor.next = fast
            # slow.next = fast.next
            # fast.next = slow
            # cursor = cursor.next.next
        self.head = dummy.next



    # 拼接俩有序链表1
    def MergeTowList1(self,head1,head2):
        dummy = node(0)
        cursor = dummy
        while head1 or head2:
            if head1.data <head2.data:
                cursor.next = head1
                head1 = head1.next
            else:
                cursor.next = head2
                head2 = head2.next
            cursor = cursor.next
            #1取完
            if head1 is None:
                cursor.next = head2
                break
            if head2 is None:
                cursor.next = head1
                break
        return  dummy.next

    # 拼接俩有序链表2
    def MergeTowList2(self,head1,head2):
        dummy = node(0)
        cursor = dummy
        while head1 and head2:
            if head1.data <head2.data:
                cursor.next = head1
                head1 = head1.next
            else:
                cursor.next = head2
                head2 = head2.next
            cursor = cursor.next
        if head1 is None:
            cursor.next = head2
        if head2 is None:
            cursor.next = head1
        return  dummy.next

    # 链表插入排序  扑克牌插入原理
    def insertLinkSort(self,head):
        # 新建一个链表
        dummp = node(0)
        right = head
        while right:
            left = dummp
            temp = right.next
            while left.next and left.next.data<right.data:
                left = left.next
            right.next = left.next
            left.next = right
            right = temp
        self.head = dummp.next





l = linkedlist()
l.list_to_link(range(1,4))
# l.insert(1,8)
l.reverse()
# print(l)
# a= l.__getitem__(1)
# print(l)
b = l.head
l.towTowChange(b)
# l.insertLinkSort(b)
# print(l)
print(l)






# def list_to_link(self, list):
#     self.head = node(list[0])
#     cursor = self.head
#     for i in list[1:]:
#         Node = node(i)
#         cursor.next = Node
#         cursor = cursor.next
#     self.size += len(list)



