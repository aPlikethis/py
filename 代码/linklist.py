class Node():
    def __init__(self, elem):
        self.elem = elem
        self.next = None
class LinkList():
    def __init__(self):
        self.head = None
    def add(self, elem):
        node = Node(elem)
        node.next = self.head
        self.head = node

linklist = LinkList()

while(linklist.head != None):
    print(linklist.head.elem)
    linklist.head = linklist.head.next