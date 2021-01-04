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
        self._parent = parent
        self._colour = Colour.Red  # Red by default when a new node is created
        self._counter = 1  # Counts how many elements are located here
        self._element = x
        self._left_child = None
        self._right_child = None

    def __find_node_or_insertion_parent(self, x) -> "Node":
        # self.element == x
        if abs(float(self._element) - float(x)) <= Node.EPSILON:
            return self
        elif self._element < x:
            # Go right
            if self._right_child is None:
                return self
            else:
                return self._right_child.__find_node_or_insertion_parent(x)  # Further recursion down
        elif self._element > x:
            # Go left
            if self._left_child is None:
                return self
            else:
                return self._left_child.__find_node_or_insertion_parent(x)

    # def __bst_insert_old(self, x) -> "Node":
    #     # Make the classic insertion!
    #     if self.element < x:
    #         # Go right
    #         if self.right_child is None:
    #             self.right_child = Node(x, self)  # Insert here
    #             return self.right_child
    #         else:
    #             return self.right_child.__bst_insert_old(x)  # Further recursion down
    #     elif self.element > x:
    #         # Go left
    #         if self.left_child is None:
    #             self.left_child = Node(x, self)
    #             return self.left_child
    #         else:
    #             return self.left_child.__bst_insert_old(x)
    #     else:
    #         # Equal elements, just increase the counter
    #         self.counter = self.counter + 1
    #         return self

    def __preorder_traversal(self, display_colours):
        if display_colours:
            print(f"({self._colour.name[0]}){self._element}", end=" ")
        else:
            print(f"{self._element}", end=" ")

        if self._left_child is not None:
            self._left_child.__preorder_traversal(display_colours)

        if self._right_child is not None:
            self._right_child.__preorder_traversal(display_colours)

    def __inorder_traversal(self, display_colours):
        if self._left_child is not None:
            self._left_child.__inorder_traversal(display_colours)

        if display_colours:
            print(f"({self._colour.name[0]}){self._element}", end=" ")
        else:
            print(f"{self._element}", end=" ")

        if self._right_child is not None:
            self._right_child.__inorder_traversal(display_colours)

    def __postorder_traversal(self, display_colours):
        if self._left_child is not None:
            self._left_child.__postorder_traversal(display_colours)

        if self._right_child is not None:
            self._right_child.__postorder_traversal(display_colours)

        if display_colours:
            print(f"({self._colour.name[0]}){self._element}", end=" ")
        else:
            print(f"{self._element}", end=" ")

    def __left_rotate(self):
        # !!!Have to rewire children and parent pointers!!!
        # Remember tmp
        tmp = self._right_child

        # Rewiring
        self._right_child = tmp._left_child
        if tmp._left_child is not None:
            tmp._left_child._parent = self

        tmp._left_child = self
        tmp._parent = self._parent

        # Need to rewire my parent's child from myself to tmp
        if self._parent is not None:
            # Am I left or right child:
            if self._parent._left_child is self:
                self._parent._left_child = tmp
            else:
                self._parent._right_child = tmp
        self._parent = tmp

    def __right_rotate(self):
        # !!!Have to rewire children and parent pointers!!!
        # Remember tmp
        tmp = self._left_child

        # Rewiring
        self._left_child = tmp._right_child
        if tmp._right_child is not None:
            tmp._right_child._parent = self

        tmp._right_child = self
        tmp._parent = self._parent

        # Need to rewire my parent's child from myself to tmp
        if self._parent is not None:
            # Am I left or right child:
            if self._parent._left_child is self:
                self._parent._left_child = tmp
            else:
                self._parent._right_child = tmp
        self._parent = tmp

    def __rb_algorithm_balance(self):
        # 2. Check if root
        if self._parent is None:
            self._colour = Colour.Black
            return

        # 3. Step: X is not root. Check if parent is black - if not go on, if parent is black then here we can finish
        if self._parent._colour == Colour.Black:
            return

        # Grandparent always exists due to the nature of RB trees
        grandparent = self._parent._parent
        uncle = None
        # Which child is our parent - left or right?
        first_way = None
        if self._parent is grandparent._left_child:
            uncle = grandparent._right_child
            first_way = Way.Left
        else:
            uncle = grandparent._left_child
            first_way = Way.Right
        uncle_colour = uncle._colour if uncle is not None else Colour.Black

        # Check if uncle is red
        if uncle_colour == Colour.Red:
            self._parent._colour = Colour.Black
            uncle._colour = Colour.Black
            grandparent._colour = Colour.Red
            grandparent.__rb_algorithm_balance()
        else:
            # Black Uncle - 4 cases

            # Find out second_way here, first_way was already determined above
            second_way = Way.Left if self is self._parent._left_child else Way.Right
            if first_way == Way.Left:
                if second_way == Way.Left:
                    # Left - Left --> Line
                    # Right rotate g
                    # Swap colours of g and p
                    grandparent._Node__right_rotate()  # Right rotate G
                    grandparent._colour, self._parent._colour = self._parent._colour, grandparent._colour
                else:
                    # Left - Right --> Bent
                    # Left rotate p
                    # Apply Left - Left case
                    # (Switch colours of x and g)
                    self._parent._Node__left_rotate()
                    self._parent._Node__right_rotate()
                    self._colour, grandparent._colour = grandparent._colour, self._colour
            else:
                if second_way == Way.Left:
                    # Right - Left --> Bent
                    # Right rotate p
                    # Apply Right-Right case
                    # (Switch colours of x and g)
                    self._parent._Node__right_rotate()
                    self._parent._Node__left_rotate()
                    self._colour, grandparent._colour = grandparent._colour, self._colour
                else:
                    # Right - Right --> Line
                    # Left rotate g
                    # Swap colours of g and p
                    grandparent._Node__left_rotate()
                    grandparent._colour, self._parent._colour = self._parent._colour, grandparent._colour

            # Post rotation we have to do step: change x = x's parent, repeat the balance procedure(steps 2 and 3)
            # self.parent.__rb_algorithm_balance()       # FER NASP slides do not specify this, but geeks for geeks does

    def __str__(self):
        # return self._element
        return self.__repr__()

    def __repr__(self):
        return f"{self._parent._element} <<--- [{self._left_child._element}] - {self._element} - [{self._right_child._element}]"

    @property
    def getElement(self):
        return self._element

    @property
    def getCounter(self):
        return self._counter

    @property
    def getParent(self):
        return self._parent

    @property
    def getColour(self):
        return self._colour

    @property
    def getLeftChild(self):
        return self._left_child

    @property
    def getRightChild(self):
        return self._right_child

    @staticmethod
    def getColourOf(node) -> Colour:
        if node is None:
            return Colour.Black
        else:
            return node._colour


class RBTree:
    def __init__(self, *args):
        self.root: Node = None
        self.__size = 0
        self.display_null_leaves = False
        self.display_colours = True
        self.rb_balance = True

        if len(args) >= 1:
            for x in args:
                self.add_node(x)

    def add_node(self, x):
        # First implement classic BST insertion
        if self.root is None:
            self.root = Node(x, None)
            self.__size = 1
            self.root._colour = Colour.Black
            return

        insertion_parent = self.root._Node__find_node_or_insertion_parent(x)
        inserted_node = None
        # insertion_parent.element == x
        if abs(float(insertion_parent._element) - float(x)) <= Node.EPSILON:
            # Node with element: x is already located in the tree - increase its counter by 1
            insertion_parent._counter += 1
            return  # No need to increment size or check or do anything else!
        elif x > insertion_parent._element:
            # Insert as right child
            insertion_parent._right_child = Node(x, insertion_parent)
            inserted_node = insertion_parent._right_child
        else:
            # Insert as left child
            insertion_parent._left_child = Node(x, insertion_parent)
            inserted_node = insertion_parent._left_child

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
        if self.root._parent is not None:
            self.root = self.root._parent

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
                        print(f"({node._colour.name[0]}){node._element}", end=" ")
                    else:
                        print(f"{node._element}", end=" ")

                bfs_tmp.append(node._left_child)
                bfs_tmp.append(node._right_child)

            bfs_queue = bfs_tmp[:]
            bfs_tmp.clear()
            print()  # Tree level separator

    def find_node(self, x) -> Node:
        res = self.root._Node__find_node_or_insertion_parent(x)
        if abs(float(x) - float(res._element)) <= Node.EPSILON:
            return res
        else:
            return None

    def get_counter(self, x):
        res = self.find_node(x)
        if res is None:
            return 0
        else:
            return res._counter

    def get_size(self):
        return self.__size

    def __printTree(self, tree_string: list, p: str, node: Node, is_left: bool):
        """
        Adapted from NASP Lab1 lab1.hpp file put on the intranet
        :return: A tree string
        """
        tree_string += p
        tree_string += "├──" if not is_left else "└──"
        if node is not None:
            if self.display_colours:
                tree_string += f"({node._colour.name}){str(node._element)}\n"
            else:
                tree_string += f"{str(node._element)}\n"
            p_add = ("│   " if not is_left else "    ")

            if self.display_null_leaves or node._right_child or node._left_child:
                self.__printTree(tree_string, p + p_add, node._right_child, False)
                self.__printTree(tree_string, p + p_add, node._left_child, True)
        else:
            if self.display_colours:
                tree_string += "(Black)NULL\n" if self.display_null_leaves else "\n"
            else:
                tree_string += "NULL\n" if self.display_null_leaves else "\n"

    def __str__(self):
        tree_string = []
        self.__printTree(tree_string, "", self.root, True)
        return "".join(tree_string)

    # def print_try(self):
    #     """
    #     This method was my attempt to make a top-to-bottom string of the tree.
    #     It was unsuccessful however, and in the end I've just decided to use the NASP print function
    #
    #     :return: String of the tree
    #     """
    #     if self.root is None:
    #         return "NULL"
    #
    #     # Implement BFS search here - use a queue and add chilren to the end of it, but have to print bottom up
    #     # List of lists - nodes by level, ordered chronologically
    #     # First put the lowest into the string, and then reverse it
    #     tree = ""
    #     levels = [[self.root], []]
    #     nodes = [self.root]     # Level that is currently being iterated over - BFS
    #     tmp_nodes = []          # Next level that will be iterated over - BFS
    #
    #     curr_level = 1
    #     while True:
    #         if len(nodes) == 0:
    #             break
    #
    #         for node in nodes:
    #             if node is None:
    #                 continue
    #
    #             tmp_nodes.append(node.left_child)
    #             tmp_nodes.append(node.right_child)
    #
    #         levels[curr_level].extend(tmp_nodes)
    #         curr_level += 1
    #         levels.append([])       # Append a new level
    #
    #         nodes = tmp_nodes[:]        # Have to copy instead of just rewire reference
    #         tmp_nodes.clear()
    #
    #     # Time to print the tree
    #     half_indent = int(2**(len(levels)-1))
    #     for level in levels:
    #         # Print whitespace at the beginning
    #         for j in range(half_indent):
    #             tree += "  "
    #
    #         # Print values, and then whitespace in between
    #         for node in level:
    #             tree += "NULL" if node is None else f"{node.element:4.2f}"
    #             for j in range(2*half_indent):
    #                 tree += "  "
    #         tree += "\n"
    #         half_indent = int(half_indent/2)
    #     return tree
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
