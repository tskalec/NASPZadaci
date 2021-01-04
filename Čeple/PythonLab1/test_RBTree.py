import pytest

from RBTree import RBTree


@pytest.fixture
def test_tree():
    return RBTree()


class TestBinaryTree:
    def test_one(self, capsys, test_tree):
        """
        Tests a simple binary tree that is balanced.

        :param capsys: Used for capturing and testing stdout
        :param test_tree: Fixture that returns an empty RB Tree object that can then be used for testing and data manipulation
        :return: nothing, this is a test method
        """
        test_tree.display_colours = False
        test_tree.rb_balance = False

        assert test_tree.get_size() == 0

        test_tree.add_node(25)
        assert test_tree.get_size() == 1
        test_tree.add_node(16)
        assert test_tree.get_size() == 2
        test_tree.add_node(32)
        assert test_tree.get_size() == 3
        test_tree.add_node(7)
        assert test_tree.get_size() == 4
        test_tree.add_node(17)
        assert test_tree.get_size() == 5
        test_tree.add_node(27)
        assert test_tree.get_size() == 6
        test_tree.add_node(37)
        assert test_tree.get_size() == 7

        test_tree.inorder_traversal()
        out, err = capsys.readouterr()
        assert out == "7 16 17 25 27 32 37 \n"

        test_tree.preorder_traversal()
        out, err = capsys.readouterr()
        assert out == "25 16 7 17 32 27 37 \n"

        test_tree.postorder_traversal()
        out, err = capsys.readouterr()
        assert out == "7 17 16 27 37 32 25 \n"

        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "25 \n16 32 \n7 17 27 37 \n\n"

    def test_two(self, capsys, test_tree):
        """
        Tests a non-balanced binary tree that has more elements!

        :param capsys: Used for capturing and testing stdout
        :param test_tree: Fixture that returns an empty RB Tree object that can then be used for testing and data manipulation
        :return: nothing, this is a test method
        """
        test_tree.display_colours = False
        test_tree.rb_balance = False

        assert test_tree.get_size() == 0

        test_tree.add_node(55)
        assert test_tree.get_size() == 1
        test_tree.add_node(20)
        assert test_tree.get_size() == 2
        test_tree.add_node(77)
        assert test_tree.get_size() == 3
        test_tree.add_node(15)
        assert test_tree.get_size() == 4
        test_tree.add_node(27)
        assert test_tree.get_size() == 5
        test_tree.add_node(76)
        assert test_tree.get_size() == 6
        test_tree.add_node(78)
        assert test_tree.get_size() == 7
        test_tree.add_node(30)
        assert test_tree.get_size() == 8
        test_tree.add_node(79)
        assert test_tree.get_size() == 9
        test_tree.add_node(29)
        assert test_tree.get_size() == 10
        test_tree.add_node(35)
        assert test_tree.get_size() == 11
        test_tree.add_node(90)
        assert test_tree.get_size() == 12

        test_tree.inorder_traversal()
        out, err = capsys.readouterr()
        assert out == "15 20 27 29 30 35 55 76 77 78 79 90 \n"

        test_tree.preorder_traversal()
        out, err = capsys.readouterr()
        assert out == "55 20 15 27 30 29 35 77 76 78 79 90 \n"

        test_tree.postorder_traversal()
        out, err = capsys.readouterr()
        assert out == "15 29 35 30 27 20 76 90 79 78 77 55 \n"

        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "55 \n20 77 \n15 27 76 78 \n30 79 \n29 35 90 \n\n"

    def test_three(self, capsys, test_tree):
        """
        Tests a fully skewed binary tree.

        :param capsys: Used for capturing and testing stdout
        :param test_tree: Fixture that returns an empty RB Tree object that can then be used for testing and data manipulation
        :return: nothing, this is a test method
        """
        test_tree.display_colours = False
        test_tree.rb_balance = False

        assert test_tree.get_size() == 0

        test_tree.add_node(1)
        assert test_tree.get_size() == 1
        test_tree.add_node(2)
        assert test_tree.get_size() == 2
        test_tree.add_node(3)
        assert test_tree.get_size() == 3
        test_tree.add_node(4)
        assert test_tree.get_size() == 4
        test_tree.add_node(5)
        assert test_tree.get_size() == 5
        test_tree.add_node(6)
        assert test_tree.get_size() == 6
        test_tree.add_node(7)
        assert test_tree.get_size() == 7
        test_tree.add_node(8)
        assert test_tree.get_size() == 8
        test_tree.add_node(9)
        assert test_tree.get_size() == 9
        test_tree.add_node(10)
        assert test_tree.get_size() == 10
        test_tree.add_node(11)
        assert test_tree.get_size() == 11
        test_tree.add_node(12)
        assert test_tree.get_size() == 12

        test_tree.inorder_traversal()
        out, err = capsys.readouterr()
        assert out == "1 2 3 4 5 6 7 8 9 10 11 12 \n"

        test_tree.preorder_traversal()
        out, err = capsys.readouterr()
        assert out == "1 2 3 4 5 6 7 8 9 10 11 12 \n"

        test_tree.postorder_traversal()
        out, err = capsys.readouterr()
        assert out == "12 11 10 9 8 7 6 5 4 3 2 1 \n"

        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "1 \n2 \n3 \n4 \n5 \n6 \n7 \n8 \n9 \n10 \n11 \n12 \n\n"

    def test_four(self, capsys, test_tree):
        """
        Tests a V-shaped binary tree.

        :param capsys: Used for capturing and testing stdout
        :param test_tree: Fixture that returns an empty RB Tree object that can then be used for testing and data manipulation
        :return: nothing, this is a test method
        """
        test_tree.display_colours = False
        test_tree.rb_balance = False

        assert test_tree.get_size() == 0

        test_tree.add_node(3)
        assert test_tree.get_size() == 1
        test_tree.add_node(2)
        assert test_tree.get_size() == 2
        test_tree.add_node(4)
        assert test_tree.get_size() == 3
        test_tree.add_node(1)
        assert test_tree.get_size() == 4
        test_tree.add_node(5)
        assert test_tree.get_size() == 5
        test_tree.add_node(6)
        assert test_tree.get_size() == 6

        test_tree.inorder_traversal()
        out, err = capsys.readouterr()
        assert out == "1 2 3 4 5 6 \n"

        test_tree.preorder_traversal()
        out, err = capsys.readouterr()
        assert out == "3 2 1 4 5 6 \n"

        test_tree.postorder_traversal()
        out, err = capsys.readouterr()
        assert out == "1 2 6 5 4 3 \n"

        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "3 \n2 4 \n1 5 \n6 \n\n"

    def test_five(self, capsys, test_tree):
        """
        The most comprehensive test. Tests negative and floating-point numbers, as well as the addition of zero.
        Also contains and tests duplicates.

        :param capsys: Used for capturing and testing stdout
        :param test_tree: Fixture that returns an empty RB Tree object that can then be used for testing and data manipulation
        :return: nothing, this is a test method
        """
        test_tree.display_colours = False
        test_tree.rb_balance = False

        assert test_tree.get_size() == 0

        test_tree.add_node(-21.21)
        assert test_tree.get_size() == 1
        test_tree.add_node(-40.22222)
        assert test_tree.get_size() == 2
        test_tree.add_node(500)
        assert test_tree.get_size() == 3
        test_tree.add_node(-57.0)
        assert test_tree.get_size() == 4
        test_tree.add_node(-35.74)
        assert test_tree.get_size() == 5
        test_tree.add_node(400)
        assert test_tree.get_size() == 6
        test_tree.add_node(501.0)
        assert test_tree.get_size() == 7
        test_tree.add_node(501.0)
        assert test_tree.get_size() == 7
        test_tree.add_node(-57.0)
        assert test_tree.get_size() == 7
        test_tree.add_node(-66)
        assert test_tree.get_size() == 8
        test_tree.add_node(-50.11111111111111)
        assert test_tree.get_size() == 9
        test_tree.add_node(-50.11111111111111)
        assert test_tree.get_size() == 9
        test_tree.add_node(-50.11111111111111)
        assert test_tree.get_size() == 9
        test_tree.add_node(-32.0)
        assert test_tree.get_size() == 10
        test_tree.add_node(501.0)
        assert test_tree.get_size() == 10
        test_tree.add_node(380.22)
        assert test_tree.get_size() == 11
        test_tree.add_node(474.443)
        assert test_tree.get_size() == 12
        test_tree.add_node(510)
        assert test_tree.get_size() == 13
        test_tree.add_node(-50.11111111111111)
        assert test_tree.get_size() == 13
        test_tree.add_node(-50.11111111111111)
        assert test_tree.get_size() == 13
        test_tree.add_node(0)
        assert test_tree.get_size() == 14
        test_tree.add_node(0.00)
        assert test_tree.get_size() == 14
        test_tree.add_node(0)
        assert test_tree.get_size() == 14
        test_tree.add_node(-50.11111111111111)
        assert test_tree.get_size() == 14
        test_tree.add_node(-50.11111111111111)
        assert test_tree.get_size() == 14
        test_tree.add_node(0.00000)
        assert test_tree.get_size() == 14
        test_tree.add_node(509.5)
        assert test_tree.get_size() == 15
        test_tree.add_node(0)
        assert test_tree.get_size() == 15
        test_tree.add_node(0.00000)
        assert test_tree.get_size() == 15
        test_tree.add_node(600.999)
        assert test_tree.get_size() == 16
        test_tree.add_node(0)
        assert test_tree.get_size() == 16
        test_tree.add_node(0.00000)
        assert test_tree.get_size() == 16

        test_tree.inorder_traversal()
        out, err = capsys.readouterr()
        assert out == "-66 -57.0 -50.11111111111111 -40.22222 -35.74 -32.0 -21.21 0 380.22 400 474.443" \
                      " 500 501.0 509.5 510 600.999 \n"

        test_tree.preorder_traversal()
        out, err = capsys.readouterr()
        assert out == "-21.21 -40.22222 -57.0 -66 -50.11111111111111 -35.74 -32.0 500 400 380.22 0 " \
                      "474.443 501.0 510 509.5 600.999 \n"

        test_tree.postorder_traversal()
        out, err = capsys.readouterr()
        assert out == "-66 -50.11111111111111 -57.0 -32.0 -35.74 -40.22222 0 380.22 474.443 400 509.5" \
                      " 600.999 510 501.0 500 -21.21 \n"

        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "-21.21 \n-40.22222 500 \n-57.0 -35.74 400 501.0" \
                      " \n-66 -50.11111111111111 -32.0 380.22 474.443 510 \n0 509.5 600.999 \n\n"


class TestRBAlgorithm:
    """
    Tests for the Red-Black Trees were done using the site: https://www.cs.usfca.edu/~galles/visualization/RedBlack.html
    """

    def test_zero(self, capsys, test_tree):
        """
        This test tests some base features, empty tree, leaves, and edge cases

        :param capsys: Used for capturing and testing stdout
        :param test_tree: Fixture that returns an empty RB Tree object that can then be used for testing and data manipulation
        :return:  nothing, this is a test method
        """
        test_tree.display_null_leaves = True
        assert test_tree.get_size() == 0

        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)NULL\n"

        test_tree.add_node(0)
        assert test_tree.get_size() == 1
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0 \n(B)NULL (B)NULL \n"

        test_tree.add_node(-5)
        assert test_tree.get_size() == 2
        test_tree.add_node(7)
        assert test_tree.get_size() == 3

        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0 \n(R)-5 (R)7 \n(B)NULL (B)NULL (B)NULL (B)NULL \n"

    def test_one(self, capsys, test_tree):
        """
        This test tests a concrete red-black tree scenario!

        :param capsys: Used for capturing and testing stdout
        :param test_tree: Fixture that returns an empty RB Tree object that can then be used for testing and data manipulation
        :return:  nothing, this is a test method
        """
        test_tree.display_null_leaves = True

        assert test_tree.get_size() == 0
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)NULL\n"

        test_tree.add_node("0025")
        assert test_tree.get_size() == 1
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0025 \n(B)NULL (B)NULL \n"

        test_tree.add_node("0025")
        assert test_tree.get_size() == 1
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0025 \n(B)NULL (B)NULL \n"

        test_tree.add_node("0004")
        assert test_tree.get_size() == 2
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0025 \n(R)0004 (B)NULL \n(B)NULL (B)NULL \n"

        test_tree.add_node("0025")
        assert test_tree.get_size() == 2
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0025 \n(R)0004 (B)NULL \n(B)NULL (B)NULL \n"

        test_tree.add_node("0004")
        assert test_tree.get_size() == 2
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0025 \n(R)0004 (B)NULL \n(B)NULL (B)NULL \n"

        test_tree.add_node("0004")
        assert test_tree.get_size() == 2
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0025 \n(R)0004 (B)NULL \n(B)NULL (B)NULL \n"

        test_tree.add_node("0003")
        assert test_tree.get_size() == 3
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0004 \n(R)0003 (R)0025 \n(B)NULL (B)NULL (B)NULL (B)NULL \n"

        test_tree.add_node("0003")
        assert test_tree.get_size() == 3
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0004 \n(R)0003 (R)0025 \n(B)NULL (B)NULL (B)NULL (B)NULL \n"

        test_tree.add_node("0004")
        assert test_tree.get_size() == 3
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0004 \n(R)0003 (R)0025 \n(B)NULL (B)NULL (B)NULL (B)NULL \n"

        test_tree.add_node("0025")
        assert test_tree.get_size() == 3
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0004 \n(R)0003 (R)0025 \n(B)NULL (B)NULL (B)NULL (B)NULL \n"

        test_tree.add_node("0003")
        assert test_tree.get_size() == 3
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0004 \n(R)0003 (R)0025 \n(B)NULL (B)NULL (B)NULL (B)NULL \n"

        test_tree.add_node("0003")
        assert test_tree.get_size() == 3
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0004 \n(R)0003 (R)0025 \n(B)NULL (B)NULL (B)NULL (B)NULL \n"

        test_tree.add_node("0004")
        assert test_tree.get_size() == 3
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0004 \n(R)0003 (R)0025 \n(B)NULL (B)NULL (B)NULL (B)NULL \n"

        test_tree.add_node("0025")
        assert test_tree.get_size() == 3
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0004 \n(R)0003 (R)0025 \n(B)NULL (B)NULL (B)NULL (B)NULL \n"

        test_tree.add_node("0003")
        assert test_tree.get_size() == 3
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0004 \n(R)0003 (R)0025 \n(B)NULL (B)NULL (B)NULL (B)NULL \n"

        test_tree.add_node("0003")
        assert test_tree.get_size() == 3
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0004 \n(R)0003 (R)0025 \n(B)NULL (B)NULL (B)NULL (B)NULL \n"

        test_tree.add_node("0004")
        assert test_tree.get_size() == 3
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0004 \n(R)0003 (R)0025 \n(B)NULL (B)NULL (B)NULL (B)NULL \n"

        test_tree.add_node("0010")
        assert test_tree.get_size() == 4
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0004 \n(B)0003 (B)0025 \n(B)NULL (B)NULL (R)0010 (B)NULL \n" \
                      "(B)NULL (B)NULL \n"

        test_tree.add_node("0015")
        assert test_tree.get_size() == 5
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0004 \n(B)0003 (B)0015 \n(B)NULL (B)NULL (R)0010 (R)0025 \n" \
                      "(B)NULL (B)NULL (B)NULL (B)NULL \n"

        test_tree.add_node("0030")
        assert test_tree.get_size() == 6
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0004 \n(B)0003 (R)0015 \n(B)NULL (B)NULL (B)0010 (B)0025 \n" \
                      "(B)NULL (B)NULL (B)NULL (R)0030 \n" \
                      "(B)NULL (B)NULL \n"

        test_tree.add_node("0035")
        assert test_tree.get_size() == 7
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0004 \n(B)0003 (R)0015 \n(B)NULL (B)NULL (B)0010 (B)0030 \n" \
                      "(B)NULL (B)NULL (R)0025 (R)0035 \n" \
                      "(B)NULL (B)NULL (B)NULL (B)NULL \n"

        test_tree.add_node("0045")
        assert test_tree.get_size() == 8
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0015 \n(R)0004 (R)0030 \n(B)0003 (B)0010 (B)0025 (B)0035 \n" \
                      "(B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL " \
                      "(B)NULL (R)0045 \n(B)NULL (B)NULL \n"

        test_tree.add_node("0037")
        assert test_tree.get_size() == 9
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0015 \n(R)0004 (R)0030 \n(B)0003 (B)0010 (B)0025 (B)0037 \n" \
                      "(B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL " \
                      "(R)0035 (R)0045 \n(B)NULL (B)NULL (B)NULL (B)NULL \n"

        # Time for some duplicates testing
        test_tree.add_node("0037")
        assert test_tree.get_size() == 9
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0015 \n(R)0004 (R)0030 \n(B)0003 (B)0010 (B)0025 (B)0037 \n" \
                      "(B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL " \
                      "(R)0035 (R)0045 \n(B)NULL (B)NULL (B)NULL (B)NULL \n"

        test_tree.add_node("0025")
        assert test_tree.get_size() == 9
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0015 \n(R)0004 (R)0030 \n(B)0003 (B)0010 (B)0025 (B)0037 \n" \
                      "(B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL " \
                      "(R)0035 (R)0045 \n(B)NULL (B)NULL (B)NULL (B)NULL \n"

        test_tree.add_node("0015")
        assert test_tree.get_size() == 9
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0015 \n(R)0004 (R)0030 \n(B)0003 (B)0010 (B)0025 (B)0037 \n" \
                      "(B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL " \
                      "(R)0035 (R)0045 \n(B)NULL (B)NULL (B)NULL (B)NULL \n"

        test_tree.add_node("0004")
        assert test_tree.get_size() == 9
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0015 \n(R)0004 (R)0030 \n(B)0003 (B)0010 (B)0025 (B)0037 \n" \
                      "(B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL " \
                      "(R)0035 (R)0045 \n(B)NULL (B)NULL (B)NULL (B)NULL \n"

        test_tree.add_node("0037")
        assert test_tree.get_size() == 9
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0015 \n(R)0004 (R)0030 \n(B)0003 (B)0010 (B)0025 (B)0037 \n" \
                      "(B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL " \
                      "(R)0035 (R)0045 \n(B)NULL (B)NULL (B)NULL (B)NULL \n"

        # Continue adding!
        test_tree.add_node("0038")
        assert test_tree.get_size() == 10
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0015 \n(B)0004 (B)0030 \n(B)0003 (B)0010 (B)0025 (R)0037 \n" \
                      "(B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL " \
                      "(B)0035 (B)0045 \n(B)NULL (B)NULL (R)0038 (B)NULL \n(B)NULL (B)NULL \n"

        test_tree.add_node("-22")
        assert test_tree.get_size() == 11
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0015 \n(B)0004 (B)0030 \n(B)0003 (B)0010 (B)0025 (R)0037 \n" \
                      "(R)-22 (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL " \
                      "(B)0035 (B)0045 \n(B)NULL (B)NULL (B)NULL (B)NULL (R)0038 (B)NULL \n(B)NULL (B)NULL \n"

        test_tree.add_node("-1")
        assert test_tree.get_size() == 12
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0015 \n(B)0004 (B)0030 \n(B)-22 (B)0010 (B)0025 (R)0037 \n" \
                      "(R)-1 (R)0003 (B)NULL (B)NULL (B)NULL (B)NULL " \
                      "(B)0035 (B)0045 \n(B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (R)0038 (B)NULL \n" \
                      "(B)NULL (B)NULL \n"

        test_tree.add_node("0000")
        assert test_tree.get_size() == 13
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0015 \n(B)0004 (B)0030 \n(R)-22 (B)0010 (B)0025 (R)0037 \n" \
                      "(B)-1 (B)0003 (B)NULL (B)NULL (B)NULL (B)NULL " \
                      "(B)0035 (B)0045 \n(B)NULL (B)NULL (R)0000 (B)NULL (B)NULL (B)NULL (R)0038 (B)NULL \n" \
                      "(B)NULL (B)NULL (B)NULL (B)NULL \n"

        test_tree.add_node("0002")
        assert test_tree.get_size() == 14
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0015 \n(B)0004 (B)0030 \n(R)-22 (B)0010 (B)0025 (R)0037 \n" \
                      "(B)-1 (B)0002 (B)NULL (B)NULL (B)NULL (B)NULL " \
                      "(B)0035 (B)0045 \n(B)NULL (B)NULL (R)0000 (R)0003 (B)NULL (B)NULL (R)0038 (B)NULL \n" \
                      "(B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL \n"

        # Duplicates testing
        test_tree.add_node("0025")
        assert test_tree.get_size() == 14
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0015 \n(B)0004 (B)0030 \n(R)-22 (B)0010 (B)0025 (R)0037 \n" \
                      "(B)-1 (B)0002 (B)NULL (B)NULL (B)NULL (B)NULL " \
                      "(B)0035 (B)0045 \n(B)NULL (B)NULL (R)0000 (R)0003 (B)NULL (B)NULL (R)0038 (B)NULL \n" \
                      "(B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL \n"

        test_tree.add_node("0003")
        assert test_tree.get_size() == 14
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0015 \n(B)0004 (B)0030 \n(R)-22 (B)0010 (B)0025 (R)0037 \n" \
                      "(B)-1 (B)0002 (B)NULL (B)NULL (B)NULL (B)NULL " \
                      "(B)0035 (B)0045 \n(B)NULL (B)NULL (R)0000 (R)0003 (B)NULL (B)NULL (R)0038 (B)NULL \n" \
                      "(B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL \n"

        test_tree.add_node("-288")
        assert test_tree.get_size() == 15
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0015 \n(B)0002 (B)0030 \n(R)-22 (R)0004 (B)0025 (R)0037 \n" \
                      "(B)-1 (B)0000 (B)0003 (B)0010 (B)NULL (B)NULL " \
                      "(B)0035 (B)0045 \n" \
                      "(B)NULL (B)NULL (R)-288 (B)NULL (B)NULL (B)NULL " \
                      "(B)NULL (B)NULL (B)NULL (B)NULL (R)0038 (B)NULL \n" \
                      "(B)NULL (B)NULL (B)NULL (B)NULL \n"

        test_tree.display_null_leaves = False
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0015 \n(B)0002 (B)0030 \n(R)-22 (R)0004 (B)0025 (R)0037 \n" \
                      "(B)-1 (B)0000 (B)0003 (B)0010 (B)0035 (B)0045 \n" \
                      "(R)-288 (R)0038 \n\n"

        test_tree.add_node("-303")
        assert test_tree.get_size() == 16
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0015 \n(B)0002 (B)0030 \n(R)-22 (R)0004 (B)0025 (R)0037 \n" \
                      "(B)-1 (B)-303 (B)0003 (B)0010 (B)0035 (B)0045 \n" \
                      "(R)-288 (R)0000 (R)0038 \n\n"

        test_tree.add_node("0404")
        assert test_tree.get_size() == 17
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0015 \n(B)0002 (B)0030 \n(R)-22 (R)0004 (B)0025 (R)0037 \n" \
                      "(B)-1 (B)-303 (B)0003 (B)0010 (B)0035 (B)0045 \n" \
                      "(R)-288 (R)0000 (R)0038 (R)0404 \n\n"

        test_tree.add_node("0676")
        assert test_tree.get_size() == 18
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0015 \n(B)0002 (B)0037 \n(R)-22 (R)0004 (R)0030 (R)0045 \n" \
                      "(B)-1 (B)-303 (B)0003 (B)0010 (B)0025 (B)0035 (B)0038 (B)0404 \n" \
                      "(R)-288 (R)0000 (R)0676 \n\n"

        test_tree.add_node("0474")
        assert test_tree.get_size() == 19
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0015 \n(B)0002 (B)0037 \n(R)-22 (R)0004 (R)0030 (R)0045 \n" \
                      "(B)-1 (B)-303 (B)0003 (B)0010 (B)0025 (B)0035 (B)0038 (B)0474 \n" \
                      "(R)-288 (R)0000 (R)0404 (R)0676 \n\n"

        test_tree.add_node("-7")
        test_tree.add_node("-5")
        test_tree.add_node("-21")
        test_tree.add_node("-25")
        test_tree.add_node("-37")
        test_tree.add_node("-23")
        assert test_tree.get_size() == 25

        # Test in, pre, post and bfs
        test_tree.inorder_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)-1 (R)-21 (R)-22 (R)-23 (B)-25 (R)-288 (B)-303 (R)-37 (B)-5 (R)-7 (B)0000 (R)0002 (B)0003 " \
                      "(B)0004 (B)0010 (B)0015 (B)0025 (R)0030 (B)0035 (B)0037 (B)0038 (R)0045 (R)0404 (B)0474 " \
                      "(R)0676 \n"

        test_tree.preorder_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0015 (R)0002 (B)-303 (R)-22 (B)-1 (R)-21 (B)-25 (R)-23 (R)-288 (R)-7 (B)-5 (R)-37 (B)0000 " \
                      "(B)0004 (B)0003 (B)0010 (B)0037 (R)0030 (B)0025 (B)0035 (R)0045 (B)0038 (B)0474 (R)0404" \
                      " (R)0676 \n"

        test_tree.postorder_traversal()
        out, err = capsys.readouterr()
        assert out == "(R)-21 (B)-1 (R)-23 (R)-288 (B)-25 (R)-22 (R)-37 (B)-5 (B)0000 (R)-7 (B)-303 (B)0003 (B)0010" \
                      " (B)0004 (R)0002 (B)0025 (B)0035 (R)0030 (B)0038 (R)0404 (R)0676 (B)0474 (R)0045 (B)0037" \
                      " (B)0015 \n"

        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0015 \n(R)0002 (B)0037 \n(B)-303 (B)0004 (R)0030 (R)0045 \n" \
                      "(R)-22 (R)-7 (B)0003 (B)0010 (B)0025 (B)0035 (B)0038 (B)0474 \n" \
                      "(B)-1 (B)-25 (B)-5 (B)0000 (R)0404 (R)0676 \n" \
                      "(R)-21 (R)-23 (R)-288 (R)-37 \n\n"

        test_tree.display_null_leaves = True
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)0015 \n(R)0002 (B)0037 \n(B)-303 (B)0004 (R)0030 (R)0045 \n" \
                      "(R)-22 (R)-7 (B)0003 (B)0010 (B)0025 (B)0035 (B)0038 (B)0474 \n" \
                      "(B)-1 (B)-25 (B)-5 (B)0000 (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (R)0404 (R)0676 \n" \
                      "(B)NULL (R)-21 (R)-23 (R)-288 (R)-37 (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL \n" \
                      "(B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL \n"

    def test_two(self, capsys):
        """
        Scenario 2. This test tests some way-side class methods and fields.

        :param capsys: Used for capturing and testing stdout
        :return:  nothing, this is a test method
        """

        test_tree = RBTree(500, 225, 777, 639, 1231, 566, 25, 1, 5, 7, 6, 778, 821, 325, 267, 298, 340, 344, 404)
        test_tree.display_null_leaves = True

        # Time to add the duplicates
        test_tree.add_node(7)
        test_tree.add_node(1231)

        test_tree.add_node(500)
        test_tree.add_node(778)

        test_tree.add_node(1231)
        test_tree.add_node(566)
        test_tree.add_node(340)
        test_tree.add_node(500)
        test_tree.add_node(1231)
        test_tree.add_node(639)
        test_tree.add_node(5)
        test_tree.add_node(340)

        test_tree.add_node(6)
        test_tree.add_node(566)
        test_tree.add_node(566)
        test_tree.add_node(566)

        test_tree.add_node(340)
        test_tree.add_node(1231)

        test_tree.add_node(340)
        test_tree.add_node(566)
        test_tree.add_node(344)
        test_tree.add_node(6)
        test_tree.add_node(1231)

        # Assert structure
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)500 \n(R)25 (B)777 \n(B)5 (B)267 (B)639 (B)821 \n" \
                      "(B)1 (B)7 (B)225 (R)325 (R)566 (B)NULL (R)778 (R)1231 \n(B)NULL (B)NULL (R)6 (B)NULL (B)NULL (B)NULL " \
                      "(B)298 (B)344 (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL \n" \
                      "(B)NULL (B)NULL (B)NULL (B)NULL (R)340 (R)404 \n(B)NULL (B)NULL (B)NULL (B)NULL \n"

        # Assert duplicates counter
        out = test_tree.get_counter(500)
        assert out == 3

        out = test_tree.get_counter(225)
        assert out == 1

        out = test_tree.get_counter(777)
        assert out == 1

        out = test_tree.get_counter(639)
        assert out == 2

        out = test_tree.get_counter(1231)
        assert out == 6
        
        out = test_tree.get_counter(566)
        assert out == 6
        
        out = test_tree.get_counter(25)
        assert out == 1
        
        out = test_tree.get_counter(1)
        assert out == 1
        
        out = test_tree.get_counter(5)
        assert out == 2
        
        out = test_tree.get_counter(7)
        assert out == 2
        
        out = test_tree.get_counter(6)
        assert out == 3
        
        out = test_tree.get_counter(778)
        assert out == 2
        
        out = test_tree.get_counter(821)
        assert out == 1
        
        out = test_tree.get_counter(325)
        assert out == 1
        
        out = test_tree.get_counter(267)
        assert out == 1
        
        out = test_tree.get_counter(298)
        assert out == 1
        
        out = test_tree.get_counter(340)
        assert out == 5
        
        out = test_tree.get_counter(344)
        assert out == 2
        
        out = test_tree.get_counter(404)
        assert out == 1
        
        # Assert some nodes not inside!

        out = test_tree.get_counter(-56)
        assert out == 0

        out = test_tree.get_counter(0)
        assert out == 0

        out = test_tree.get_counter(14)
        assert out == 0

        out = test_tree.get_counter(1000000)
        assert out == 0

        out = test_tree.get_counter(640)
        assert out == 0

        out = test_tree.get_counter(638)
        assert out == 0

        out = test_tree.get_counter(299)
        assert out == 0

        # Assert find node
        res = test_tree.find_node(500)
        assert res is not None
        assert res.getElement == 500

        res = test_tree.find_node(777)
        assert res is not None
        assert res.getElement == 777

        res = test_tree.find_node(325)
        assert res is not None
        assert res.getElement == 325

        res = test_tree.find_node(7)
        assert res is not None
        assert res.getElement == 7

        res = test_tree.find_node(404)
        assert res is not None
        assert res.getElement == 404
        
        # Time for some nodes not inside
        res = test_tree.find_node(-64)
        assert res is None

        res = test_tree.find_node(-64)
        assert res is None

        res = test_tree.find_node(341)
        assert res is None

        res = test_tree.find_node(345)
        assert res is None

        res = test_tree.find_node(9999)
        assert res is None

        res = test_tree.find_node(0)
        assert res is None

        # Inorder, preorder and postorder
        test_tree.inorder_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)1 (B)5 (R)6 (B)7 (R)25 (B)225 (B)267 (B)298 (R)325 (R)340 (B)344 (R)404 (B)500 (R)566 " \
                      "(B)639 (B)777 (R)778 (B)821 (R)1231 \n"

        test_tree.preorder_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)500 (R)25 (B)5 (B)1 (B)7 (R)6 (B)267 (B)225 (R)325 (B)298 (B)344 (R)340 (R)404 " \
                      "(B)777 (B)639 (R)566 (B)821 (R)778 (R)1231 \n"

        test_tree.postorder_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)1 (R)6 (B)7 (B)5 (B)225 (B)298 (R)340 (R)404 (B)344 (R)325 (B)267 (R)25 (R)566 " \
                      "(B)639 (R)778 (R)1231 (B)821 (B)777 (B)500 \n"

        # Non-null display bfs
        test_tree.display_null_leaves = False
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)500 \n(R)25 (B)777 \n(B)5 (B)267 (B)639 (B)821 \n" \
                      "(B)1 (B)7 (B)225 (R)325 (R)566 (R)778 (R)1231 \n(R)6 (B)298 (B)344 \n(R)340 (R)404 \n\n"

        # Display null leaves bfs
        test_tree.display_null_leaves = True
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)500 \n(R)25 (B)777 \n(B)5 (B)267 (B)639 (B)821 \n" \
                      "(B)1 (B)7 (B)225 (R)325 (R)566 (B)NULL (R)778 (R)1231 \n(B)NULL (B)NULL (R)6 (B)NULL (B)NULL " \
                      "(B)NULL (B)298 (B)344 (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL (B)NULL \n" \
                      "(B)NULL (B)NULL (B)NULL (B)NULL (R)340 (R)404 \n" \
                      "(B)NULL (B)NULL (B)NULL (B)NULL \n"

    def test_print(self, capsys):
        """
        Testing print function

        :param capsys: Used for capturing and testing stdout
        :return:  nothing, this is a test method
        """
        test_tree = RBTree(500, 225, 777, 639, 1231, 566, 25, 1, 5, 7, 6, 778, 821, 325, 267, 298, 340, 344, 404)
        test_tree.display_null_leaves = True

        print(test_tree)
        out, err = capsys.readouterr()
        assert out == """└──(Black)500
    ├──(Black)777
    │   ├──(Black)821
    │   │   ├──(Red)1231
    │   │   │   ├──(Black)NULL
    │   │   │   └──(Black)NULL
    │   │   └──(Red)778
    │   │       ├──(Black)NULL
    │   │       └──(Black)NULL
    │   └──(Black)639
    │       ├──(Black)NULL
    │       └──(Red)566
    │           ├──(Black)NULL
    │           └──(Black)NULL
    └──(Red)25
        ├──(Black)267
        │   ├──(Red)325
        │   │   ├──(Black)344
        │   │   │   ├──(Red)404
        │   │   │   │   ├──(Black)NULL
        │   │   │   │   └──(Black)NULL
        │   │   │   └──(Red)340
        │   │   │       ├──(Black)NULL
        │   │   │       └──(Black)NULL
        │   │   └──(Black)298
        │   │       ├──(Black)NULL
        │   │       └──(Black)NULL
        │   └──(Black)225
        │       ├──(Black)NULL
        │       └──(Black)NULL
        └──(Black)5
            ├──(Black)7
            │   ├──(Black)NULL
            │   └──(Red)6
            │       ├──(Black)NULL
            │       └──(Black)NULL
            └──(Black)1
                ├──(Black)NULL
                └──(Black)NULL

"""

        test_tree = RBTree("0025", "0004", "0003", "0010", "0015", "0030", "0035", "0045", "0037", "0038", "-22", "-1",
                           "0000", "0002", "0025", "0003", "-288", "-303", "0404", "0676", "0474", "0003", "0003",
                           "0025", "0025", "0025", "0000", "-7", "-5", "0000", "-21", "-25", "-37", "-23")
        test_tree.display_null_leaves = True

        print(test_tree)
        out, err = capsys.readouterr()
        assert out == """└──(Black)0015
    ├──(Black)0037
    │   ├──(Red)0045
    │   │   ├──(Black)0474
    │   │   │   ├──(Red)0676
    │   │   │   │   ├──(Black)NULL
    │   │   │   │   └──(Black)NULL
    │   │   │   └──(Red)0404
    │   │   │       ├──(Black)NULL
    │   │   │       └──(Black)NULL
    │   │   └──(Black)0038
    │   │       ├──(Black)NULL
    │   │       └──(Black)NULL
    │   └──(Red)0030
    │       ├──(Black)0035
    │       │   ├──(Black)NULL
    │       │   └──(Black)NULL
    │       └──(Black)0025
    │           ├──(Black)NULL
    │           └──(Black)NULL
    └──(Red)0002
        ├──(Black)0004
        │   ├──(Black)0010
        │   │   ├──(Black)NULL
        │   │   └──(Black)NULL
        │   └──(Black)0003
        │       ├──(Black)NULL
        │       └──(Black)NULL
        └──(Black)-303
            ├──(Red)-7
            │   ├──(Black)0000
            │   │   ├──(Black)NULL
            │   │   └──(Black)NULL
            │   └──(Black)-5
            │       ├──(Black)NULL
            │       └──(Red)-37
            │           ├──(Black)NULL
            │           └──(Black)NULL
            └──(Red)-22
                ├──(Black)-25
                │   ├──(Red)-288
                │   │   ├──(Black)NULL
                │   │   └──(Black)NULL
                │   └──(Red)-23
                │       ├──(Black)NULL
                │       └──(Black)NULL
                └──(Black)-1
                    ├──(Red)-21
                    │   ├──(Black)NULL
                    │   └──(Black)NULL
                    └──(Black)NULL

"""
