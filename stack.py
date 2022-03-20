# /bin/env python
# coding: utf-8

class Node:
    """
    a Node for insertion into the Stack.  Contains a 'data' element, and 'previous' pointer to the previous element
    within the stack
    """
    def __init__(self, data, previous):
        self.data = data
        self.previous = previous

class Stack():
    """
    a stack (LIFO) implemented with a singly linked list.  defines 'push' and 'pop' functions.
    """
    def __init__(self):
        self._num_elements = 0
        self.head = None

    def push(self, data):
        """
        pushes data to the head of the stack

        input:
            'data': data to be pushed into the stack
        output:
            N/A
        """
        if self._num_elements == 0:
            #there's no 'previous', so pass in 'None'
            new_node = Node(data,None)
            self.head = new_node
        else:
            #the new node's 'previous' is the current tail
            new_node = Node(data, self.head)
            #update the tail pointer to the new node
            self.head = new_node
        self._num_elements += 1

    def pop(self):
        """
        pops data from the head of the stack

        input:
            N/A
        output:
            data that is popped from the stack
        """
        pop_node_data = None

        if self._num_elements == 0:
            pop_node_data = None
        else:
            #make sure to store the tail before updating the pointer
            pop_node_data = self.head.data

            #update the tail pointer
            self.head = self.head.previous
            self._num_elements -= 1

        return pop_node_data

    @property
    def num_elements(self):
        return self._num_elements

if __name__ == "__main__":
    mystack = Stack()

    data = mystack.pop()
    if data:
        print(data)
    else:
        print("stack empty")

    mystack = Stack()
    mystack.push(1)

    while mystack.num_elements > 0:
        print(mystack.pop())

    data = mystack.pop()
    if data:
        print(data)
    else:
        print("stack empty")

    mystack = Stack()
    mystack.push(1)
    mystack.push(2)

    while mystack.num_elements > 0:
        print(mystack.pop())

    data = mystack.pop()
    if data:
        print(data)
    else:
        print("stack empty")

    mystack = Stack()

    mystack.push(1)
    mystack.push(2)
    mystack.push(3)
    mystack.push(4)
    mystack.push(5)

    while mystack.num_elements > 0:
        print(mystack.pop())
