class Node:
    def __init__(self, val:int, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if index + 1 > self.size or index < 0:
            return -1
        
        currentNode = self.head

        if index == 0:
            return self.head.val

        for i in range(index):
            currentNode = currentNode.next

        return currentNode.val

        

    def addAtHead(self, val: int) -> None:
        if self.head == None:
            new_node = Node(val)
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = Node(val, self.head)
            self.head = self.head.prev
            
        self.size += 1

        

    def addAtTail(self, val: int) -> None:
        if self.tail == None:
            new_node = Node(val)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = Node(val, None, self.tail)
            self.tail = self.tail.next
            
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:


        if self.tail == None and index == 0:
            new_node = Node(val)
            self.head = new_node
            self.tail = new_node
            self.size += 1
        elif index == 0:
            self.head.prev = Node(val, self.head)
            self.head = self.head.prev
            self.size += 1
        elif index < self.size:
            currentNode = self.head
            for i in range(index):
                currentNode = currentNode.next
            a = currentNode.prev
            currentNode.prev = Node(val, currentNode, a)
            currentNode.prev.prev.next = currentNode.prev
            self.size += 1
        elif index == self.size:
            self.tail.next = Node(val, None, self.tail)
            self.tail = self.tail.next
            self.size += 1


        

    def deleteAtIndex(self, index: int) -> None:
        if self.size != 0 and index < self.size:
            currentNode = self.head


            if index == 0:
                if currentNode.next:
                    currentNode = currentNode.next
                    currentNode.prev = None
                    self.head = currentNode
                else:
                    self.head = None
                    self.tail = None

            elif self.size - 1 == index:
                for i in range(index):
                    currentNode = currentNode.next
                currentNode.prev.next = None
                self.tail = currentNode.prev
                




            else:
                for i in range(index):
                    currentNode = currentNode.next

                currentNode.next.prev = currentNode.prev
                currentNode = currentNode.prev
                currentNode.next = currentNode.next.next
            
            self.size -= 1


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)