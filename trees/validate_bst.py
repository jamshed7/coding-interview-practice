
# Array to store key values from traversal
tree_vals = []

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        tree_vals.append(tree.getRootVal())
        inorder(tree.getRightChild())

def sort_check(tree_vals):
    return tree_vals == sorted(tree_vals)

# pass in root to in order to populate tree_vals[]
inorder(tree)
# Returns true if inorder traversal of tree results in a sorted array
sort_check(tree_vals)
