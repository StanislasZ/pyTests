
from typing import  List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printListFromTailToHead(self , listNode: ListNode) -> List[int]:
        # write code here
        list1 = []
        while listNode != None:
            list1.append(listNode.val)

            listNode = listNode.next
        list1.reverse()
        return list1


    rlt = []

    # 递归
    def printListFromTailToHead2(self, listNode: ListNode) -> List[int]:
        # 中止条件
        if listNode != None:
            self.printListFromTailToHead2(listNode.next)
            self.rlt.append(listNode.val)
        return self.rlt

    # 栈
    def printListFromTailToHead3(self, listNode: ListNode) -> List[int]:
        stack = []
        res = []
        while listNode != None:
            stack.append(listNode.val)
            listNode = listNode.next

        while len(stack) > 0:
            res.append(stack.pop())
        return res






if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3



    list = Solution().printListFromTailToHead2(node1)
    print(list)