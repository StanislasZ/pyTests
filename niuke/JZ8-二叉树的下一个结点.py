# -*- coding:utf-8 -*-

'''
给定一个二叉树其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的next指针。

下图为一棵有9个节点的二叉树。树中从父节点指向子节点的指针用实线表示，从子节点指向父节点的用虚线表示

'''

class TreeLinkNode:


    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None    # 父节点



class Solution:

    nodes = []

    def GetNext(self, pNode):
        # write code here

        # 先找root
        rootNode = pNode
        while rootNode.next != None:
            rootNode = rootNode.next


        # 对 rootNode 进行中序遍历
        self.inOrder(rootNode)

        hitIndex = -1
        for i in range(len(self.nodes)):
            if self.nodes[i].val == pNode.val:
                hitIndex = i

        if hitIndex == -1 or hitIndex == len(self.nodes) - 1:
            return None
        return self.nodes[hitIndex + 1]



    # 中序遍历
    def inOrder(self, root: TreeLinkNode):
        if root == None:
            return
        self.inOrder(root.left)
        self.nodes.append(root)
        self.inOrder(root.right)




if __name__ == "__main__":
    node8 = TreeLinkNode(8)
    node6 = TreeLinkNode(6)
    node5 = TreeLinkNode(5)
    node7 = TreeLinkNode(7)
    node10 = TreeLinkNode(10)
    node9 = TreeLinkNode(9)
    node11 = TreeLinkNode(11)

    node8.left = node6
    node8.right = node10

    node6.next = node8
    node6.left = node5
    node6.right = node7

    node10.next = node8
    node10.left = node9
    node10.right = node11

    node5.next = node6
    node7.next = node6

    node9.next = node10
    node11.next = node10



    nextNode = Solution().GetNext(node8)
    print(nextNode)