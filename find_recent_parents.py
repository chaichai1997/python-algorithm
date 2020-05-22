# -*- coding: utf-8 -*-
# author = "chaichai"
from tree_array_transform import  array_to_tree
from stack_create import Stack
import math


"""
方法一：路径对比法
"""
"""
function： 找到二叉树从根节点root到node的路径
输入参数： root根节点，node目标节点，s存储路径的栈
返回值：node在root子树上，或node=root 返回True
"""


def get_path(root, node, s):
    if root is None:
        return False
    if root == node:
        s.push(root)
        return True
    """
    如果node节点在root的左子树或右子树上，那么root就是node的祖先节点
    """
    if get_path(root.left, node, s) or get_path(root.right, node, s):
        s.push(root)
        return True
    return False


"""
function: 查找二叉树中两个节点最近的共同父节点
输入： root, node1, node2
返回值： 最近父节点
"""


def find_recent_parent(root, node1, node2):
    stack1 = Stack()
    stack2 = Stack()
    get_path(root, node1, stack1)
    get_path(root, node2, stack2)
    while stack1.top() == stack2.top():
        common = stack1.top()
        stack1.pop()
        stack2.pop()
    return common


"""
方法二：节点标号法，假设树为完全二叉树，并对其进行编号，找node1，node2的父节n1/2 与 n2/2,直到相等
"""


class Ref:
    def __init__(self):
        self.num = None


"""
function: 找出节点在二叉树中的编号
"""


def get_num(root, node, number):
    if root is None:
        return False
    if root == node:
        return True
    tmp = number.num
    number.num = 2 * tmp
    if get_num(root.left, node, number):
        return True
    else:
        number.num = 2 * tmp + 1
        return get_num(root.right, node, number)


"""
function: 根据标号找出节点
"""


def get_node(root, number):
    if root is None or number < 0:
        return None
    if number == 1:
        return root
    lens = int((math.log(number)/math.log(2)))
    while lens > 0:
        if (1 << (lens-1)) & number == 1:
            root = root.right
        else:
            root = root.left
        lens -= 1
    return root


"""
function: 查找父节点
"""


def parent(root, node1, node2):
    ref1 = Ref()
    ref2 = Ref()
    ref1.num = 1
    ref2.num = 1
    get_num(root, node1, ref1)
    get_num(root, node2, ref2)
    n1 = ref1.num
    n2 = ref2.num
    while n1 != n2:
        if n1 > n2:
            n1 = n1 // 2
        else:
            n2 = n2 // 2
    return get_node(root, n1)


def find_parent_after(root, node1, node2):
    if root is None or root == node1 or root == node2:
        return root
    l = find_parent_after(root.left, node1, node2)
    r = find_parent_after(root.right, node1, node2)
    if l is None:
        return r
    elif r is None:
        return l
    else:
        return root


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    root = array_to_tree(arr, 0, len(arr)-1)
    node1 = root.left.left.left
    node2 = root.left.right
    # res = find_recent_parent(root, node1, node2)
    # res = parent(root, node1, node2)
    res = find_parent_after(root, node1, node2)
    if res is not None:
        print(str(node1.data) + '与' + str(node2.data) + '的最近公共父节点为' + str(res.data)  )



