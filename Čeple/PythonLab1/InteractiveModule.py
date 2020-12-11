from RBTree import RBTree
import sys
from time import sleep


# Function adapted from: https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
def err_print(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


class InteractiveModule:
    __help_string = """
    Available commands are:
    ADD X
    REMOVE X
    CLEAR_TREE
    CONTAINS X
    SIZE
    PRINT
    TOGGLE_NULL_DISPLAY
    TOGGLE_COLOUR_DISPLAY
    PREORDER
    INORDER
    POSTORDER
    BFS
    HELP
    QUIT
    """

    __DELAY_SECONDS = 0.025     # 25 ms delay in order to prevent stdout and stderr mixing

    def __init__(self):
        print("Interactive mode on!")
        self.rbtree = RBTree()
        self.user_input_handlers_map = {
            "ADD": self.add_handler,
            "REMOVE": self.remove_handler,
            "CLEAR_TREE": self.clear_tree_handler,
            "CONTAINS": self.contains_handler,
            "SIZE": self.size_handler,
            "PRINT": self.print_handler,
            "TOGGLE_NULL_DISPLAY": self.toggle_null_display_handler,
            "TOGGLE_COLOUR_DISPLAY": self.toggle_colour_display_handler,
            "PREORDER": self.preorder_handler,
            "INORDER": self.inorder_handler,
            "POSTORDER": self.postorder_handler,
            "BFS": self.bfs_handler,
            "HELP": InteractiveModule.help_handler,
            "QUIT": InteractiveModule.quit_handler
        }

    def run(self):
        print("Welcome to RB Trees interactive mode!")
        print(InteractiveModule.__help_string)
        print("Please enter your query >", end="")
        while True:
            quit_bool = self.parse_input()
            if quit_bool:
                return
            else:
                sleep(InteractiveModule.__DELAY_SECONDS)
                print(">", end="")

    def parse_input(self):
        user_input = input().strip()
        input_parts = user_input.split(" ")
        operation = input_parts[0].upper()
        func_to_exec = self.user_input_handlers_map.get(operation, InteractiveModule.default_handler)
        return func_to_exec(input_parts[1:])

    def add_handler(self, args):
        if len(args) != 1:
            err_print("Exactly 1 argument required!")
            return False

        operand = float(args[0])
        self.rbtree.add_node(operand)
        print("Addition done!")
        return False

    def remove_handler(self, args):
        if len(args) != 1:
            err_print("Exactly 1 argument required!")
            return False

        print("RB Tree removal is not implemented!")
        return False

    def clear_tree_handler(self, args):
        if len(args) != 0:
            err_print("No arguments should be present for this operation!")
            return False

        self.rbtree = RBTree()
        print("The tree has been cleared!")
        return False

    def contains_handler(self, args):
        if len(args) != 1:
            err_print("Exactly 1 argument required!")
            return False

        operand = float(args[0])
        res = self.rbtree.find_node(operand)
        if res:
            print("Tree contains that node!")
        else:
            print("Tree does not contain that node!")
        return False

    def size_handler(self, args):
        if len(args) != 0:
            err_print("No arguments should be present for this operation!")
            return False

        print(f"Tree size is: {self.rbtree.get_size()}")
        return False

    def print_handler(self, args):
        if len(args) != 0:
            err_print("No arguments should be present for this operation!")
            return False

        print("Printing the tree!")
        print(self.rbtree)
        return False

    def toggle_null_display_handler(self, args):
        if len(args) != 0:
            err_print("No arguments should be present for this operation!")
            return False

        if self.rbtree.display_null_leaves:
            self.rbtree.display_null_leaves = False
            print("Turning off NULL leaves display!")
        else:
            self.rbtree.display_null_leaves = True
            print("Turning on NULL leaves display!")
        return False

    def toggle_colour_display_handler(self, args):
        if len(args) != 0:
            err_print("No arguments should be present for this operation!")
            return False

        if self.rbtree.display_colours:
            self.rbtree.display_colours = False
            print("Turning off colour display!")
        else:
            self.rbtree.display_colours = True
            print("Turning on colour display!")
        return False

    def preorder_handler(self, args):
        if len(args) != 0:
            err_print("No arguments should be present for this operation!")
            return False

        self.rbtree.preorder_traversal()
        return False

    def inorder_handler(self, args):
        if len(args) != 0:
            err_print("No arguments should be present for this operation!")
            return False

        self.rbtree.inorder_traversal()
        return False

    def postorder_handler(self, args):
        if len(args) != 0:
            err_print("No arguments should be present for this operation!")
            return False

        self.rbtree.postorder_traversal()
        return False

    def bfs_handler(self, args):
        if len(args) != 0:
            err_print("No arguments should be present for this operation!")
            return False

        self.rbtree.bfs_traversal()
        return False

    @staticmethod
    def quit_handler(args):
        if len(args) != 0:
            err_print("No arguments should be present for this operation!")
            return False

        return True     # Returning True signals that we should exit!

    @staticmethod
    def help_handler(args):
        if len(args) != 0:
            err_print("No arguments should be present for this operation!")
            return False

        print(InteractiveModule.__help_string)
        return False

    @staticmethod
    def default_handler(args):
        err_print("Unrecognised operation!")
        return False
