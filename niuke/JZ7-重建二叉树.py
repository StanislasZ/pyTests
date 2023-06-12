from typing import  List


'''
给定节点数为 n 的二叉树的前序遍历和中序遍历结果，请重建出该二叉树并返回它的头结点。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建出如下图所示。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pre int整型一维数组
# @param vin int整型一维数组
# @return TreeNode类
#
class Solution:
    def reConstructBinaryTree(self , pre: List[int], vin: List[int]) -> TreeNode:
        # write code here
        # 先序的第一个是 根节点， 根据这个数 到 中序遍历里 找， 切分出  左子树， 当前节点，  右子树

        # 中止条件
        if len(pre) == 0:
            return None

        currVal = pre[0]
        currIndexInVin = vin.index(currVal)

        leftPreList = pre[1:currIndexInVin + 1]  # 左子树的 先序遍历
        rightPreList = pre[currIndexInVin + 1::]  # 右子树的 先序遍历

        leftVinList = vin[0:currIndexInVin]  # 左子树的 中序遍历
        rightVinList = vin[currIndexInVin + 1::]  # 右子树的 中序遍历

        currNode = TreeNode(currVal)
        currNode.left = self.reConstructBinaryTree(leftPreList, leftVinList)
        currNode.right = self.reConstructBinaryTree(rightPreList, rightVinList)

        return currNode


if __name__ == "__main__":
    preList = [1,2,4,7,3,5,6,8]   # 先序遍历
    vinList = [4,7,2,1,5,3,8,6]   # 中序遍历


    currVal = preList[0]
    currIndexInVin = vinList.index(currVal)   # 当前节点在中序遍历列表中的索引
    print("currIndexInVin = ", currIndexInVin)
    leftPreList = preList[1:currIndexInVin + 1]  # 左子树的 先序遍历

    rightPreList = preList[currIndexInVin + 1::]
    print("leftPreList = ", leftPreList)
    print("rightPreList = ", rightPreList)

    leftVinList = vinList[0:currIndexInVin]
    rightVinList = vinList[currIndexInVin + 1::]
    print("leftVinList = ", leftVinList)
    print("rightVinList = ", rightVinList)





    # root = Solution().reConstructBinaryTree(preList, vinList)