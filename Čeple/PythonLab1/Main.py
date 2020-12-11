from InteractiveModule import InteractiveModule
from RBTree import RBTree


def main():
    print("RB Trees!")
    test_tree_1 = RBTree(25, 16, 32, 7, 17, 27, 37)
    test_tree_2 = RBTree(25)
    print(test_tree_2)
    print(test_tree_1)

    int_mod = InteractiveModule()
    int_mod.run()


if __name__ == "__main__":
    main()
