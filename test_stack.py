import unittest

from stack import Node, Stack

class TestMirrorWords(unittest.TestCase):
    def test1(self):
        """
        test popping an empty stack
        """
        mystack = Stack()

        data = mystack.pop()

        self.assertEqual(data, None)

    def test2(self):
        """
        test pushing/popping a single element to the stack
        """
        mystack = Stack()

        list_popped_nodes = []

        mystack.push(1)

        while mystack.num_elements > 0:
            list_popped_nodes.append(mystack.pop())

        self.assertEqual(list_popped_nodes, [1])

    def test4(self):
        """
        test popping once more after a single element stack has been emptied
        """
        mystack = Stack()

        list_popped_nodes = []

        mystack.push(1)

        while mystack.num_elements > 0:
            list_popped_nodes.append(mystack.pop())

        node = mystack.pop()

        self.assertEqual(node, None)

    def test3(self):
        """
        test pushing/popping multiple elements to the stack
        """
        mystack = Stack()

        list_popped_nodes = []

        mystack.push(1)
        mystack.push(2)

        while mystack.num_elements > 0:
            list_popped_nodes.append(mystack.pop())

        self.assertEqual(list_popped_nodes, [2,1])

    def test4(self):
        """
        test popping once more after a multiple element stack has been emptied
        """
        mystack = Stack()

        list_popped_nodes = []

        mystack.push(1)
        mystack.push(2)

        while mystack.num_elements > 0:
            list_popped_nodes.append(mystack.pop())

        node = mystack.pop()

        self.assertEqual(node, None)

    def test5(self):
        """
        real world example; many elements pushing/popping multiple elements
        """
        mystack = Stack()

        list_popped_nodes = []

        mystack.push(1)
        mystack.push(2)
        mystack.push(3)
        mystack.push(4)
        mystack.push(5)

        while mystack.num_elements > 0:
            list_popped_nodes.append(mystack.pop())

        self.assertEqual(list_popped_nodes, [5,4,3,2,1])

unittest.main()

