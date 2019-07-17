class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None


#Function to return the nth to last node in a linked list
def nth_to_last_node(n, head):

    left_pointer = head
    right_pointer = head

    for i in range(n):
        if not right_pointer.nextnode:
            return -1

        right_pointer = right_pointer.nextnode

    while right_pointer:
        right_pointer = right_pointer.nextnode
        left_pointer = left_pointer.nextnode

    return left_pointer


#Testing
class Test(object):

    def test(self,sol):

        assert_equal(sol(2,a),d)
        print ('ALL TEST CASES PASSED')

from nose.tools import assert_equal

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

# Run tests
t = Test()
t.test(nth_to_last_node)
