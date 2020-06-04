class Node():
    def __init__(self, elem):
        self.elem = elem
        self.next = None
class Linklist():
    def __init__(self):
        self.head = None
    def add(self, elem):
        node = Node(elem)
        node.next = self.head
        self.head = node

linklist = Linklist()
linklist.add(1)
linklist.add(2)
linklist.add(3)
linklist.add(4)
while(linklist.head != None):
    print(linklist.head.elem)
    linklist.head = linklist.head.next