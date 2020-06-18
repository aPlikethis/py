class Node():
    def __init__(self, elem):
        self.elem = elem
        self.next = None
class LinkList():
    def __init__(self):
        node = Node(0)
        node.next = None
        self.head = node
        self.end = node      
    def append(self, elem):
        newnode = Node(elem)
        newnode.next = None
        self.end.next = newnode
        self.end = newnode
        pass
    def printlist(self):
        self.head = self.head.next
        while(self.head != None):
            print(self.head.elem)
            self.head = self.head.next
        pass

linklist = LinkList()

while(1):
    data = {"name":0, "score":0}
    data["name"] = input()
    if(data["score"] == "0"):
        break
    else:
        data["score"] = int(input())
        linklist.append(data)

linklist.printlist()


