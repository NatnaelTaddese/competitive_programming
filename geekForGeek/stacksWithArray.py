class Stack:
    def __init__(self):
      self.size = 0
      self.stack = []
    
    def is_empty(self):
        return self.size == 0
        
    def push(self, element):
       self.stack.append(element)
       self.size += 1
    
    def peek(self):
       if self.is_empty:
          return None
       else:
          return self.stack[self.size - 1]
           
    def pop(self):
       if self.is_empty():
           return None
       else:
          self.size -= 1
          return self.stack[self.size - 1]


# Using Linked Lists

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None
        self.n = 0

    def is_empty(self):
        return self.top == None
   
    def push(self, data):
        node = Node(data)
        node.next = self.top
        node.prev = None
        if self.is_empty():
            self.top = node
        else:
            self.top.prev = node
        self.top = node
        self.n += 1
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.top
    
    def pop(self):
        if self.is_empty():
            return None
        else:
            top = self.top
            self.top = self.top.prev
            if self.is_empty():
                self.top = None
            self.n -= 1
            return top.data


