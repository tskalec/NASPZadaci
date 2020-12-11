# Author: Kristijan Ceple
# RB Trees featuring insertion

import enum

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Colour(enum.Enum):
    Red = 0
    Black = 1


class Way(enum.Enum):
    Left = 0
    Right = 1
    Up = 2
    Down = 3


class Node:
    way_stack = []
    EPSILON = 1e-6

    def __init__(self, x, parent):
        self.parent = parent
        self.colour = Colour.Red        # Red by default when a new node is created
        self.counter = 1                # Counts how many elements are located here
        self.element = x
        self.left_child = None
        self.right_child = None

    def __find_node_or_insertion_parent(self, x) -> "Node":
        if self.element < x:
            # Go right
            if self.right_child is None:
                return self
            else:
                return self.right_child.__find_node_or_insertion_parent(x)  # Further recursion down
        elif self.element > x:
            # Go left
            if self.left_child is None:
                return self
            else:
                return self.left_child.__find_node_or_insertion_parent(x)
        elif abs(self.element - x) <= Node.EPSILON:
            return self

    def __bst_insert_old(self, x) -> "Node":
        # Make the classic insertion!
        if self.element < x:
            # Go right
            if self.right_child is None:
                self.right_child = Node(x, self)  # Insert here
                return self.right_child
            else:
                return self.right_child.__bst_insert_old(x)  # Further recursion down
        elif self.element > x:
            # Go left
            if self.left_child is None:
                self.left_child = Node(x, self)
                return self.left_child
            else:
                return self.left_child.__bst_insert_old(x)
        else:
            # Equal elements, just increase the counter
            self.counter = self.counter + 1
            return self

    def __preorder_traversal(self, display_colours):
        if display_colours:
            print(f"({self.colour.name[0]}){self.element}", end=" ")
        else:
            print(f"{self.element}", end=" ")

        if self.left_child is not None:
            self.left_child.__preorder_traversal(display_colours)

        if self.right_child is not None:
            self.right_child.__preorder_traversal(display_colours)

    def __inorder_traversal(self, display_colours):
        if self.left_child is not None:
            self.left_child.__inorder_traversal(display_colours)

        if display_colours:
            print(f"({self.colour.name[0]}){self.element}", end=" ")
        else:
            print(f"{self.element}", end=" ")

        if self.right_child is not None:
            self.right_child.__inorder_traversal(display_colours)

    def __postorder_traversal(self, display_colours):
        if self.left_child is not None:
            self.left_child.__postorder_traversal(display_colours)

        if self.right_child is not None:
            self.right_child.__postorder_traversal(display_colours)

        if display_colours:
            print(f"({self.colour.name[0]}){self.element}", end=" ")
        else:
            print(f"{self.element}", end=" ")

    def __left_rotate(self):
        # Have to rewire children and parent pointers!
        tmp = self.right_child
        self.right_child = tmp.left_child
        tmp.left_child = self
        tmp.parent = self.parent

        # Need to rewire my parent's child from myself to tmp
        if self.parent is not None:
            # Am I left or right child:
            if self.parent.left_child is self:
                self.parent.left_child = tmp
            else:
                self.parent.right_child = tmp
        self.parent = tmp

    def __right_rotate(self):
        # Have to rewire children and parent pointers!
        tmp = self.left_child
        self.left_child = tmp.right_child
        tmp.right_child = self
        tmp.parent = self.parent

        # Need to rewire my parent's child from myself to tmp
        if self.parent is not None:
            # Am I left or right child:
            if self.parent.left_child is self:
                self.parent.left_child = tmp
            else:
                self.parent.right_child = tmp
        self.parent = tmp

    def __rb_algorithm_balance(self):
        # 2. Check if root
        if self.parent is None:
            self.colour = Colour.Black
            return

        # 3. Step: X is not root. Check if parent is black - if not go on, if parent is black then here we can finish
        if self.parent.colour == Colour.Black:
            return

        # Grandparent always exists due to the nature of RB trees
        grandparent = self.parent.parent
        uncle = None
        # Which child is our parent - left or right?
        first_way = None
        if self.parent is grandparent.left_child:
            uncle = grandparent.right_child
            first_way = Way.Left
        else:
            uncle = grandparent.left_child
            first_way = Way.Right
        uncle_colour = uncle.colour if uncle is not None else Colour.Black

        # Check if uncle is red
        if uncle_colour == Colour.Red:
            self.parent.colour = Colour.Black
            uncle.colour = Colour.Black
            grandparent.colour = Colour.Red
            grandparent.__rb_algorithm_balance()
        else:
            # Black Uncle - 4 cases

            # Find out second_way here, first_way was already determined above
            second_way = Way.Left if self is self.parent.left_child else Way.Right
            if first_way == Way.Left:
                if second_way == Way.Left:
                    # Left - Left --> Line
                    # Right rotate g
                    # Swap colours of g and p
                    grandparent._Node__right_rotate()           # Right rotate G
                    grandparent.colour, self.parent.colour = self.parent.colour, grandparent.colour
                else:
                    # Left - Right --> Bent
                    # Left rotate p
                    # Apply Left - Left case
                    # (Switch colours of x and g)
                    self.parent._Node__left_rotate()
                    self.parent._Node__right_rotate()
                    self.colour, grandparent.colour = grandparent.colour, self.colour
            else:
                if second_way == Way.Left:
                    # Right - Left --> Bent
                    # Right rotate p
                    # Apply Right-Right case
                    # (Switch colours of x and g)
                    self.parent._Node__right_rotate()
                    self.parent._Node__left_rotate()
                    self.colour, grandparent.colour = grandparent.colour, self.colour
                else:
                    # Right - Right --> Line
                    # Left rotate g
                    # Swap colours of g and p
                    grandparent._Node__left_rotate()
                    grandparent.colour, self.parent.colour = self.parent.colour, grandparent.colour

            # Post rotation we have to do step: change x = x's parent, repeat the balance procedure(steps 2 and 3)
            # self.parent.__rb_algorithm_balance()              # FER NASP slides do not specify this, but geeks for geeks does

    @staticmethod
    def getColourOf(node) -> Colour:
        if node is None:
            return Colour.Black
        else:
            return node.colour


class RBTree:
    def __init__(self, *args):
        self.root: Node = None
        self.__size = 0
        self.display_null_leaves = False
        self.display_colours = True
        self.rb_balance = True

        if len(args) >= 1:
            [self.add_node(x) for x in args]

    def add_node(self, x):
        # First implement classic BST insertion
        if self.root is None:
            self.root = Node(x, None)
            self.__size = 1
            self.root.colour = Colour.Black
            return

        insertion_parent = self.root._Node__find_node_or_insertion_parent(x)
        inserted_node = None
        if abs(insertion_parent.element - x) <= Node.EPSILON:
            # Node with element: x is already located in the tree - increase its counter by 1
            insertion_parent.counter += 1
            return          # No need to increment size or check or do anything else!
        elif x > insertion_parent.element:
            # Insert as right child
            insertion_parent.right_child = Node(x, insertion_parent)
            inserted_node = insertion_parent.right_child
        else:
            # Insert as left child
            insertion_parent.left_child = Node(x, insertion_parent)
            inserted_node = insertion_parent.left_child

        self.__size += 1
        if self.rb_balance:
            inserted_node._Node__rb_algorithm_balance()
        else:
            return

        # Post-rotation fix root
        # if inserted_node.parent is None:
        #     self.root = inserted_node
        # elif inserted_node.parent.parent is None:
        #     self.root = inserted_node.parent

        # Post-rotation fix root
        if self.root.parent is not None:
           self.root = self.root.parent

    def preorder_traversal(self):
        # Parent - Left child - Right child
        self.root._Node__preorder_traversal(self.display_colours)
        print()

    def inorder_traversal(self):
        # Left child - Parent - Right child
        self.root._Node__inorder_traversal(self.display_colours)
        print()

    def postorder_traversal(self):
        # Left child - Right child - Parent
        self.root._Node__postorder_traversal(self.display_colours)
        print()

    def bfs_traversal(self):
        if self.root is None:
            if self.display_colours:
                print("(B)NULL")
            else:
                print("NULL")
            return

        bfs_queue = [self.root]
        bfs_tmp = []

        while len(bfs_queue) > 0:
            for node in bfs_queue:
                # Print the node, add its children to the end of the queue
                if node is None:
                    if self.display_null_leaves:
                        print("(B)NULL", end=" ") if self.display_colours else print("NULL", end=" ")
                    continue
                else:
                    if self.display_colours:
                        print(f"({node.colour.name[0]}){node.element}", end=" ")
                    else:
                        print(f"{node.element}", end=" ")

                bfs_tmp.append(node.left_child)
                bfs_tmp.append(node.right_child)

            bfs_queue = bfs_tmp[:]
            bfs_tmp.clear()
            print()          # Tree level separator

    def find_node(self, x):
        res = self.root._Node__find_node_or_insertion_parent()
        if abs(x - res.element) <= Node.EPSILON:
            return res
        else:
            return None

    def get_size(self):
        return self.__size

    def __printTree(self, tree_string:list, p:str, node:Node, is_left:bool):
        """
        Adapted from NASP Lab1 lab1.hpp file put on the intranet
        :return: A tree string
        """
        tree_string += p
        tree_string += "├──" if not is_left else "└──"
        if node is not None:
            if self.display_colours:
                tree_string += f"({node.colour.name}){str(node.element)}\n"
            else:
                tree_string += f"{str(node.element)}\n"
            p_add = ("│   " if not is_left else "    ")

            if self.display_null_leaves or node.right_child or node.left_child:
                self.__printTree(tree_string, p + p_add, node.right_child, False)
                self.__printTree(tree_string, p + p_add, node.left_child, True)
        else:
            if self.display_colours:
                tree_string += "(Black)NULL\n" if self.display_null_leaves else "\n"
            else:
                tree_string += "NULL\n" if self.display_null_leaves else "\n"

    def __str__(self):
        tree_string = []
        self.__printTree(tree_string, "", self.root, True)
        return "".join(tree_string)

    def print_try(self):
        if self.root is None:
            return "NULL"

        # Implement BFS search here - use a queue and add chilren to the end of it, but have to print bottom up
        # List of lists - nodes by level, ordered chronologically
        # First put the lowest into the string, and then reverse it
        tree = ""
        levels = [[self.root], []]
        nodes = [self.root]     # Level that is currently being iterated over - BFS
        tmp_nodes = []          # Next level that will be iterated over - BFS

        curr_level = 1
        while True:
            if len(nodes) == 0:
                break

            for node in nodes:
                if node is None:
                    continue

                tmp_nodes.append(node.left_child)
                tmp_nodes.append(node.right_child)

            levels[curr_level].extend(tmp_nodes)
            curr_level += 1
            levels.append([])       # Append a new level

            nodes = tmp_nodes[:]        # Have to copy instead of just rewire reference
            tmp_nodes.clear()

        # Time to print the tree
        half_indent = int(2**(len(levels)-1))
        for level in levels:
            # Print whitespace at the beginning
            for j in range(half_indent):
                tree += "  "

            # Print values, and then whitespace in between
            for node in level:
                tree += "NULL" if node is None else f"{node.element:4.2f}"
                for j in range(2*half_indent):
                    tree += "  "
            tree += "\n"
            half_indent = int(half_indent/2)
        return tree
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
