class Node(object):

    def __init__(self,value):

        self.value = value
        self.nextnode = None


#Determine if a linked list contains a cycle
def cycle_check(node):

    runner1 = node
    runner2 = node

    while runner2.nextnode != None:
        runner1 = runner1.nextnode
        runner2 = runner2.nextnode.nextnode

        if runner1 == runner2:
            return True

    return False
