#tree = Node(27)
class Node:   #code for implementing a binary tree
    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item
class binaryInsert(Node):
    def __init__(self, item):
        Node.__init__(self, item)

    def insert(self, item):
        if self.item:
            if item < self.item:
                if self.left is None:
                    self.left = Node(item)
                else:
                    self.left.insert(item)
            elif item > self.item:
                if self.right is None:
                    self.right = Node(item)
                else:
                    self.right.insert(item)
        else:
            self.item = item
class binarySearch(Node):
    def __init__(self, item):
        Node.__init__(self, item)

    def search(self, item):
        while self.item != item:
            if item < self.item:
                self.item = self.left
            else:
                self.item = self.right
            if self.item is None:
                return None
        return self.item

tree = Node(27)
tree = Node(1).insert(19)
tree = Node(2).insert(10)
tree = Node(4).insert(18)
#Node1.insert(10)
#Node1.insert(19)
#Node1.insert(20)
#Node1.insert(39)
#Node1.search(39)
