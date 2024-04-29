class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        if index >= self.size or index < 0:
            return -1

        cursor = self.head
        # while index > 0:
        #     cursor = cursor.next
        #     index -= 1

        for _ in range(index):
            cursor = cursor.next

        return cursor.val
            
    def addAtHead(self, val):
        temp = Node(val)
        # if not self.head:
        #     self.head = temp
        #     self.tail = temp
        # else:
        #     temp.next = self.head
        #     self.head = temp

        temp.next = self.head
        self.head = temp

        self.size += 1

    def addAtTail(self, val) :
        temp = Node(val)

        # if not self.tail:
        #     self.head = temp
        #     self.tail = temp
        # else:
        #     self.tail.next = temp
        #     self.tail = temp
        if not self.head:
            self.head = temp
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = temp
        
        self.size += 1
        
    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
            return
        
        if index > self.size or index < 0:
            return
        # 1 -> 2 -> 3 -> 4 -> 5
        # add 6 at index 3
        temp = Node(val)
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        
        temp.next = curr.next
        curr.next = temp

        self.size += 1



        # dummy = Node(0)
        # dummy.next = self.head
        # curr_idx = 0
        # prev = dummy
        # while curr_idx < index:
        #     prev = prev.next
        #     curr_idx += 1
        # curr = prev.next
        # temp = Node(val)
        # prev.next = temp
        # temp.next = curr
        # self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        
        if index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            self.size -= 1
            return
        
        prev = None
        curr = self.head
        curr_idx = 0
        while curr_idx < index:
            prev = curr
            curr = curr.next
            curr_idx += 1
        prev.next = curr.next
        if not curr.next:
            self.tail = prev
        self.size -= 1
