from RBTree import RBTree


class TestBinaryTree:
    def test_one(self, capsys):
        test_tree = RBTree()
        test_tree.display_colours = False
        test_tree.rb_balance = False

        test_tree.add_node(25)
        test_tree.add_node(16)
        test_tree.add_node(32)
        test_tree.add_node(7)
        test_tree.add_node(17)
        test_tree.add_node(27)
        test_tree.add_node(37)

        test_tree.inorder_traversal()
        out, err = capsys.readouterr()
        assert out == "7 16 17 25 27 32 37 \n"

        test_tree.preorder_traversal()
        out, err = capsys.readouterr()
        assert out == "25 16 7 17 32 27 37 \n"

        test_tree.postorder_traversal()
        out, err = capsys.readouterr()
        assert out == "7 17 16 27 37 32 25 \n"

    def test_two(self, capsys):
        test_tree = RBTree()
        test_tree.display_colours = False
        test_tree.rb_balance = False

        test_tree.add_node(55)
        test_tree.add_node(20)
        test_tree.add_node(15)
        test_tree.add_node(27)
        test_tree.add_node(30)
        test_tree.add_node(29)
        test_tree.add_node(35)
        test_tree.add_node(77)
        test_tree.add_node(76)
        test_tree.add_node(78)
        test_tree.add_node(79)
        test_tree.add_node(90)

        test_tree.inorder_traversal()
        out, err = capsys.readouterr()
        assert out == "15 20 27 29 30 35 55 76 77 78 79 90 \n"

        test_tree.preorder_traversal()
        out, err = capsys.readouterr()
        assert out == "55 20 15 27 30 29 35 77 76 78 79 90 \n"

        test_tree.postorder_traversal()
        out, err = capsys.readouterr()
        assert out == "15 29 35 30 27 20 76 90 79 78 77 55 \n"


class TestRB:
    def test_zero(self, capsys):
        """
        This test tests some base features, empty tree, leaves, and edge cases
        :return:
        """

        test_tree = RBTree()
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

        def test_one(self, capsys):
            test_tree = RBTree()
            test_tree.display_null_leaves = True
            assert test_tree.get_size() == 0

