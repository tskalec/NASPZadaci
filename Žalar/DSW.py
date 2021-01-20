from binarytree import Node,build # used because of implemented visualisation
import math

def DSW(root):
    return createPerfectTree(createBackbone(root))

# counter specifies the number of nodes to be rotated, the function makes a left rotation for every second node
def rotationHelperFunction(root, counter):
    temp = root
    parent = None
    for i in range(counter):
        if parent:
            rotateLeft(parent, temp)
            parent = parent.right
        else:
            root = rotateLeft(parent, temp)
            parent = root
        temp = parent.right
    return root

#creates a balanced tree out of a backbone
def createPerfectTree(root):
    n = root.max_leaf_depth + 1
    h = math.floor(math.log2(n + 1))
    k = 2 ** h - 1
    rots = n - k
    root = rotationHelperFunction(root, rots)

    while k > 1:
        k = k // 2
        root = rotationHelperFunction(root, k)

    return root

def rotateLeft(parent, child):
    if parent:
        parent.right = child.right
        child.right = parent.right.left
        parent.right.left = child

    else:
        temp = child
        child = child.right
        temp.right = child.left
        child.left = temp
    return child


def rotateRight(parent, child):
    if parent:
        parent.right = child.left
        child.left = parent.right.right
        parent.right.right = child

    else:
        temp = child
        child = child.left
        temp.left = child.right
        child.right = temp
    return child

#creates a backbone from given binary tree
def createBackbone(root):
    tmp = root
    parent = None
    while tmp:
        if tmp.left:
            child = tmp.left
            if parent:
                rotateRight(parent, tmp)
                parent = tmp
            else:
                root = rotateRight(parent, tmp)
            tmp = child
        else:
            parent = tmp
            tmp = tmp.right
    return root


if __name__ == '__main__':
    root = Node(3)
    root.left = Node(1)
    root.left.right = Node(2)
    root.right = Node(4)
    root.right.right = Node(5)
    root.right.right.right = Node(6)
    root.right.right.right.right = Node(8)
    root.right.right.right.right.left = Node(7)
    root.right.right.right.right.right = Node(9)
    root.right.right.right.right.right.right = Node(10)

    print("Pocetno binarno stablo")
    print(root)
    print("Balansirano binarno stablo")
    print(DSW(root))

    #print(build([10,5,12,None,None,None,13])) #primjer kako se moze zadati binarno stablo

