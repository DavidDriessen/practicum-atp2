# Python bytecode 3.6 (3379)
# Embedded file name: .\class_demo.py
# Compiled at: 2017-08-30 14:14:36
# Size of source mod 2**32: 10024 bytes
# Decompiled by https://python-decompiler.com
from typing import TypeVar, List, Union
A = TypeVar('A')

class BSTNode:
    pass


class BSTNode:

    def __init__(self, element, left, right):
        self.element = element
        self.left = left
        self.right = right

    def __repr__(self, nspaces=0) -> str:
        """show tree with self as root
        parameters:
            nspaces: number of preceding spaces
        return:
            None"""
        s1 = ''
        s2 = ''
        s3 = ''
        if self.right is not None:
            s1 = self.right.__repr__(nspaces + 3)
        s2 = s2 + ' ' * nspaces + str(self.element) + '\n'
        if self.left is not None:
            s3 = self.left.__repr__(nspaces + 3)
        return s1 + s2 + s3

    def insert(self, e) -> bool:
        """insert e.
        parameters:
            e: object to be inserted
        return:
            True if e is not already present
            False if a is already present"""
        parent = self
        current = None
        found = False
        if parent.element < e:
            current = parent.right
        else:
            if parent.element > e:
                current = parent.left
            else:
                found = True
        while not found and current:
            parent = current
            if parent.element < e:
                current = parent.right
            elif parent.element > e:
                current = parent.left
            else:
                found = True

        if not found:
            if parent.element < e:
                parent.right = BSTNode(e, None, None)
            else:
                parent.left = BSTNode(e, None, None)
        return not found

    def insertArray(self, a, low=0, high=-1) -> None:
        """insert a[low:high+1].
        parameters:
            a: array to be inserted
            low: begin-index of a
            high: end-index of a
        return:
            None"""
        if len(a) == 0:
            return
        if high == -1:
            high = len(a) - 1
        mid = (low + high + 1) // 2
        self.insert(a[mid])
        if mid > low:
            self.insertArray(a, low, mid - 1)
        if high > mid:
            self.insertArray(a, mid + 1, high)

    def search(self, e) -> Union[(BSTNode, None)]:
        """search node with object e.
        parameters:
            e: object to be searched
        return:
            None if e is not present
            node with object e if e is present"""
        current = self
        found = False
        while not found and current:
            if current.element < e:
                current = current.right
            elif current.element > e:
                current = current.left
            else:
                found = True

        if found:
            return current
        else:
            return

    def search2(self, e) -> Union[(BSTNode, None)]:
        """search node with object e.
        parameters:
            e: object to be searched
        return:
            None if e is not present
            node with object e if e is present"""
        if self.element == e:
            return self
        parent = self.getParent(e)
        if parent is None:
            return
        elif parent.element < e:
            return parent.right
        else:
            return parent.left

    def getParent(self, e) -> Union[(BSTNode, None)]:
        """get parent of node with object e.
        parameters:
            e: object of child
        return:
            None if e is not present or e is object or root
            node with node.left or node.right contains e"""
        parent = self
        current = None
        found = False
        if parent.element < e:
            current = parent.right
        else:
            if parent.element > e:
                current = parent.left
            else:
                return
            while not found and current:
                if current.element == e:
                    found = True
                else:
                    parent = current
                    if current.element < e:
                        current = current.right
                    else:
                        current = current.left

            if found:
                return parent
            return

    def parentMinRightTree(self):
        """get parent of node with smallest object e of the right tree of self .
        parameters:
            None
        return:
            parent of node with smallest object e of the right tree of self
        pre-conditie: self.right != None """
        parent = self.right
        current = parent.left
        while 1:
            if current.left:
                parent = current
                current = current.left

        return parent

    def delete(self, e) -> bool:
        """delete object e.
        parameters:
            e: object to be deleted
        return:
            True if e is present
            False if e is not present"""
        parent = self.getParent(e)
        if parent is None:
            return False
        if parent.element < e:
            current = parent.right
            if current.left is None:
                parent.right = parent.right.right
                return True
            if current.right is None:
                parent.right = parent.right.left
                return True
        else:
            current = parent.left
            if current.left is None:
                parent.left = parent.left.right
                return True
            if current.right is None:
                parent.left = parent.left.left
                return True
            if current.right.left is None:
                current.element = current.right.element
                current.right = current.right.right
                return True
            node = current.parentMinRightTree()
            current.element = node.left.element
            node.left = node.left.right
            return True


class BST:

    def __init__(self, a=None):
        if a:
            mid = len(a) // 2
            self.root = BSTNode(a[mid], None, None)
            self.root.insertArray(a[:mid])
            self.root.insertArray(a[mid + 1:])
        else:
            self.root = None

    def __repr__(self) -> str:
        """show tree with self.root as root
        parameters:
            None
        return:
            String"""
        if self.root:
            return str(self.root)
        else:
            return 'null-tree'

    def search(self, e) -> Union[(BSTNode, None)]:
        """search node with object e.
        parameters:
            e: object to be searched
        return:
            None if e is not present
            node with object e if e is present"""
        if self.root:
            if e:
                pass
            return self.root.search(e)
        else:
            return

    def insert(self, e) -> bool:
        """insert e.
        parameters:
            e: object to be inserted
        return:
            True if e is not already present
            False if a is already present"""
        if e:
            if self.root:
                return self.root.insert(e)
            self.root = BSTNode(e, None, None)
            return True
        else:
            return False

    def delete(self, e) -> bool:
        """delete object e.
        parameters:
            e: object to be deleted
        return:
            True if e is present
            False if e is not present"""
        if self.root:
            if e:
                if self.root.element == e:
                    if self.root.left is None:
                        self.root = self.root.right
                    else:
                        if self.root.right is None:
                            self.root = self.root.left
                        else:
                            if self.root.right.left is None:
                                self.root.element = self.root.right.element
                                self.root.right = self.root.right.right
                            else:
                                node = self.root.parentMinRightTree()
                                self.root.element = node.left.element
                                node.left = node.left.right
                    return True
                return self.root.delete(e)
            return False


if __name__ == '__main__':
    b = BST([1, 2, 3])
    print(b)
    print('----------------')
    b = BST([1, 2, 3, 4])
    print(b)
    print('----------------')
    b = BST([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(b)
    print('----------------')
    b = BST([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    print(b)
    node = b.search(3)
    if node is not None:
        print(node.element)
    node = b.search(4)
    if node is not None:
        print(node.element)
    node = b.search(8)
    if node is not None:
        print(node.element)
    node = b.search(11)
    if node is not None:
        print(node.element)
    node = b.search(16)
    if node is not None:
        print(node.element)
    b.insert(17)
    print(b)
    print('----------------')
    b.delete(14)
    print(b)
    print('----------------')
    print(b.insert(10))
    b = BST()
    for i in range(1, 11):
        b.insert(i)

    print(b)
    print('----------------')
    b = BST(None)
    print(b)
    print('----------------')
    b = BST([])
    print(b)
    print('----------------')
    b = BST([0])
    print(b)
    print('----------------')
    b = BST()
    b.insert(3)
    b.insert(2)
    b.insert(10)
    b.insert(11)
    b.insert(9)
    b.insert(6)
    b.insert(7)
    b.insert(8)
    print(b)
    print('----------------')
    b.delete(3)
    print(b)
    print('----------------')