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
    Tests for the Red-Black Tree were done using the site: https://www.cs.usfca.edu/~galles/visualization/RedBlack.html
    """

    def test_zero(self, capsys, test_tree):
        """
        This test tests some base features, empty tree, leaves, and edge cases

        :param capsys: Used for capturing and testing stdout
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
        This test tests a concrete red-black tree!

        :param capsys: Used for capturing and testing stdout
        :return:  nothing, this is a test method
        """
        test_tree.display_null_leaves = True

        assert test_tree.get_size() == 0
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)NULL\n"

        test_tree.add_node(25)
        assert test_tree.get_size() == 1
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)25 \n(B)NULL (B)NULL \n\n"

        test_tree.add_node(25)
        assert test_tree.get_size() == 1
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)25 \n(B)NULL (B)NULL \n\n"

        test_tree.add_node(4)
        assert test_tree.get_size() == 2
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)25 \n(R)4 (B)NULL \n(B)NULL (B)NULL \n\n"

        test_tree.add_node(25)
        assert test_tree.get_size() == 2
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)25 \n(R)4 (B)NULL \n(B)NULL (B)NULL \n\n"

        test_tree.add_node(4)
        assert test_tree.get_size() == 2
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)25 \n(R)4 (B)NULL \n(B)NULL (B)NULL \n\n"

        test_tree.add_node(4)
        assert test_tree.get_size() == 2
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)25 \n(R)4 (B)NULL \n(B)NULL (B)NULL \n\n"

        test_tree.add_node(3)
        assert test_tree.get_size() == 3
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)4 \n(R)3 (B)25 \n(B)NULL (B)NULL (B)NULL (B)NULL\n"

        test_tree.add_node(3)
        assert test_tree.get_size() == 3
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)4 \n(R)3 (B)25 \n(B)NULL (B)NULL (B)NULL (B)NULL\n"

        test_tree.add_node(4)
        assert test_tree.get_size() == 3
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)4 \n(R)3 (B)25 \n(B)NULL (B)NULL (B)NULL (B)NULL\n"

        test_tree.add_node(25)
        assert test_tree.get_size() == 3
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)4 \n(R)3 (B)25 \n(B)NULL (B)NULL (B)NULL (B)NULL\n"

        test_tree.add_node(3)
        assert test_tree.get_size() == 3
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)4 \n(R)3 (B)25 \n(B)NULL (B)NULL (B)NULL (B)NULL\n"

        test_tree.add_node(3)
        assert test_tree.get_size() == 3
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)4 \n(R)3 (B)25 \n(B)NULL (B)NULL (B)NULL (B)NULL\n"

        test_tree.add_node(4)
        assert test_tree.get_size() == 3
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)4 \n(R)3 (B)25 \n(B)NULL (B)NULL (B)NULL (B)NULL\n"

        test_tree.add_node(25)
        assert test_tree.get_size() == 3
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)4 \n(R)3 (B)25 \n(B)NULL (B)NULL (B)NULL (B)NULL\n"

        test_tree.add_node(3)
        assert test_tree.get_size() == 3
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)4 \n(R)3 (B)25 \n(B)NULL (B)NULL (B)NULL (B)NULL\n"

        test_tree.add_node(3)
        assert test_tree.get_size() == 3
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)4 \n(R)3 (B)25 \n(B)NULL (B)NULL (B)NULL (B)NULL\n"

        test_tree.add_node(4)
        assert test_tree.get_size() == 3
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)4 \n(R)3 (B)25 \n(B)NULL (B)NULL (B)NULL (B)NULL\n"

        test_tree.add_node(10)
        assert test_tree.get_size() == 4
        test_tree.bfs_traversal()
        out, err = capsys.readouterr()
        assert out == "(B)4 \n(B)3 (B)25 \n(B)NULL (B)NULL (R)10 (B)NULL\n"