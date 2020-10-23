# 导入类型
from typing import Optional

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"{self.data}"

# 自定义函数
# 判断是否有环
def is_circle(head):
    slow = head
    fast = head
    # 判断快指针
    while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return "有环"
    return "没环"

# 找闭环点
def findPoint(head :Optional[node] = None):
    try:
        slow = head
        fast = head
        # 判断快指针
        while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                # 有环的时候停止
                if fast == slow:
                    break
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next
        return  f'{slow}'
    except:
        return  "没环"

# 快捷输入__main__
# 程序入口
if __name__ == "__main__":
    node1 = node(1)
    node2 = node(2)
    node3 = node(3)
    node4 = node(4)
    node5 = node(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    # node5.next = node

print(findPoint(node1))


