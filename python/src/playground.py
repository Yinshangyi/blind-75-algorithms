from test.trees.utils import buildTree, printTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)


def breadth_first_search(root):
    queue = []
    queue.append(root)
    # queue = [1]
    while len(queue) > 0:
        current_element = queue.pop(0)
        if current_element:
            print(current_element.val)
            queue.append(current_element.left)
            queue.append(current_element.right)


root = buildTree([1, 2, 3, 4, 5, 6, 7])
printTree(root)
print("Breadth First Search Traversal")
breadth_first_search(root)
