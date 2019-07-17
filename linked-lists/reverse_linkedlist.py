class Node(object):

    def __init__(self,value):

        self.value = value
        self.nextnode = None


#Reverse a linked list in-place
def reverse(head):

    current = head
    previous = None
    next_ =  None

    while current:
        next_ = current.nextnode

        current.nextnode = previous

        previous = current
        current = next_

    #return new head
    return previous
