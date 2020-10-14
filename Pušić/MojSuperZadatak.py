from __future__ import annotations

from enum import Enum
from sys import argv
from typing import List


class Node:
    class Colors(Enum):
        BLACK = 0
        RED = 1

    def __init__(self, value, color=None, parent=None, left=None, right=None):
        self.value = value
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return '{0} ({1})'.format(self.value, self.color)

    def grandparent(self):
        return self.parent.parent if self.parent is not None else None

    def sibling(self):
        if self.parent is not None:
            return self.parent.left if self.value >= self.parent.value else self.parent.right


class RedBlackTree:
    root = None

    class Rotations(Enum):
        LEFT = 0
        RIGHT = 1

    def __init__(self):
        pass

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return '\n'.join(self.preorder())

    def preorder(self, node: Node = None, level: int = 0) -> List[str]:
        node = self.root if node is None else node

        if node is None:
            return []
        else:
            nodes_in_tree = ['|{0}{1}\tL = {2}\tD = {3}'.format('-' * level, node, node.left, node.right)]

            if node.left is not None:
                next_level = level + 1
                nodes_in_tree += self.preorder(node.left, next_level)

            if node.right is not None:
                next_level = level + 1
                nodes_in_tree += self.preorder(node.right, next_level)

            return nodes_in_tree

    def right_rotation(self, q: Node):
        p = q.left

        q.left = p.right
        if q.left is not None:
            q.left.parent = q

        p.right = q

        p.parent = q.parent
        if p.parent is None:
            self.root = p
            p.color = Node.Colors.BLACK
        else:
            if q.parent.left == q:
                q.parent.left = p
            elif q.parent.right == q:
                q.parent.right = p

        q.parent = p

    def left_rotation(self, p: Node):
        q = p.right

        p.right = q.left
        if p.right is not None:
            p.right.parent = p

        q.left = p

        q.parent = p.parent
        if p.parent is None:
            self.root = q
            q.color = Node.Colors.BLACK
        else:
            if p.parent.left == p:
                p.parent.left = q
            elif p.parent.right == p:
                p.parent.right = q

        p.parent = q

    def insert(self, value: int):
        if self.root is None:
            new = Node(value=value, color=Node.Colors.RED, parent=None)
            self.root = new
        else:
            current = self.root

            while True:
                if value < current.value:
                    if current.left is None:
                        new = Node(value=value, color=Node.Colors.RED, parent=current)
                        current.left = new
                        break
                    else:
                        current = current.left
                elif value >= current.value:
                    if current.right is None:
                        new = Node(value=value, color=Node.Colors.RED, parent=current)
                        current.right = new
                        break
                    else:
                        current = current.right

        self.repair(new)
        return

    def repair(self, new: Node):
        parent = new.parent
        grandparent = new.grandparent()
        uncle = parent.sibling() if parent is not None else None

        # First case
        if parent is None:
            new.color = Node.Colors.BLACK
            return

        # Second case
        elif parent.color == Node.Colors.BLACK:
            return

        # Third case
        elif uncle is not None and uncle.color == Node.Colors.RED:
            parent.color = Node.Colors.BLACK
            uncle.color = Node.Colors.BLACK
            grandparent.color = Node.Colors.RED

            self.repair(grandparent)

        # Fourth case
        # elif uncle is not None and uncle.color == Node.Colors.BLACK:
        else:
            if new == parent.left and parent == grandparent.left:
                self.right_rotation(grandparent)
                parent.color = Node.Colors.BLACK
                grandparent.color = Node.Colors.RED
            elif new == parent.left and parent == grandparent.right:
                self.right_rotation(parent)
                self.left_rotation(grandparent)
                new.color = Node.Colors.BLACK
                grandparent.color = Node.Colors.RED
            elif new == parent.right and parent == grandparent.left:
                self.left_rotation(parent)
                self.right_rotation(grandparent)
                new.color = Node.Colors.BLACK
                grandparent.color = Node.Colors.RED
            elif new == parent.right and parent == grandparent.right:
                self.left_rotation(grandparent)
                parent.color = Node.Colors.BLACK
                grandparent.color = Node.Colors.RED

    def delete(self, value: int):
        if self.root is None:
            return False

        current = self.root
        while True:
            if value < current.value:
                if current.left is not None:
                    current = current.left
                else:
                    return False
            elif value == current.value:
                break
            elif value > current.value:
                if current.right is not None:
                    current = current.right
                else:
                    return False

        # BST deletion

        if current.left is None and current.right is None:
            deleted_color = current.color
            replacement_color = None

            x = None
            x_parent = current.parent

            if self.root == current:
                self.root = x
            elif current == current.parent.left:
                current.parent.left = x
            elif current == current.parent.right:
                current.parent.right = x

        elif current.left is not None and current.right is None:
            deleted_color = current.color
            replacement_color = current.left.color

            current.value = current.left.value
            current.color = current.left.color

            current.left = None

            x = current

        elif current.left is None and current.right is not None:
            deleted_color = current.color
            replacement_color = current.right.color

            current.value = current.right.value
            current.color = current.right.color

            current.right = None

            x = current

        else:
            predecessor = current.left
            while predecessor.right is not None:
                predecessor = predecessor.right
            x = predecessor.left
            if x is None:
                x_parent = predecessor.parent
            else:
                x.parent = predecessor.parent

            deleted_color = current.color
            replacement_color = predecessor.color

            current.value = predecessor.value
            current.color = predecessor.color

            if predecessor == current.left:
                current.left = predecessor.left
            else:
                predecessor.parent.right = None

        # Adjustments #1
        if deleted_color == Node.Colors.RED and replacement_color in (Node.Colors.RED, None):
            return True

        elif deleted_color == Node.Colors.RED and replacement_color == Node.Colors.BLACK:
            current.color = Node.Colors.RED

        elif deleted_color == Node.Colors.BLACK and replacement_color == Node.Colors.RED:
            current.color = Node.Colors.BLACK
            return True

        else:
            pass

        # Adjustments #2
        while True:
            if x is None:
                sibling = x_parent.left if x_parent.right is None else x_parent.right
            else:
                sibling = x.parent.left if x == x.parent.right else x.parent.right

            # First case
            if x is not None and x.color == Node.Colors.RED:
                x.color = Node.Colors.BLACK
                return True

            # Second case
            left_child = x_parent.left is None if x is None else x.parent.left == x
            if (x is None or x.color == Node.Colors.BLACK) and sibling.color == Node.Colors.RED:
                sibling.color = Node.Colors.BLACK
                sibling.parent.color = Node.Colors.RED

                if left_child:
                    self.left_rotation(sibling.parent)
                else:
                    self.right_rotation(sibling.parent)

                if left_child:
                    sibling = x_parent.right if x is None else x.parent.right
                else:
                    sibling = x_parent.left if x is None else x.parent.left

            # Third case
            if (x is None or x.color == Node.Colors.BLACK) and sibling.color == Node.Colors.BLACK\
                    and (sibling.left is None or sibling.left.color == Node.Colors.BLACK)\
                    and (sibling.right is None or sibling.right.color == Node.Colors.BLACK):
                sibling.color = Node.Colors.RED
                if x is None:
                    x = x_parent
                else:
                    x = x.parent

                if x.color == Node.Colors.RED:
                    x.color = Node.Colors.BLACK
                    return True
                else:
                    continue

            # Fourth case
            left_child = x_parent.left is None if x is None else x.parent.left == x
            other_side_cousin = sibling.left if left_child else sibling.right
            same_side_cousin = sibling.right if left_child else sibling.left
            other_side_cousin_red = False if other_side_cousin is None or other_side_cousin.color == Node.Colors.BLACK\
                else True
            same_side_cousin_black = True if same_side_cousin is None or same_side_cousin.color == Node.Colors.BLACK\
                else False
            if (x is None or x.color == Node.Colors.BLACK) and sibling.color == Node.Colors.BLACK\
                    and other_side_cousin_red and same_side_cousin_black:
                other_side_cousin.color = Node.Colors.BLACK
                sibling.color = Node.Colors.RED

                if left_child:
                    self.right_rotation(sibling)
                else:
                    self.left_rotation(sibling)

                if left_child:
                    sibling = x_parent.right if x is None else x.parent.right
                else:
                    sibling = x_parent.left if x is None else x.parent.left

            # Fifth case
            left_child = x_parent.left is None if x is None else x.parent.left == x
            mirror_cousin = sibling.right if left_child else sibling.left
            mirror_cousin_red = False if mirror_cousin is None or mirror_cousin.color == Node.Colors.BLACK else True
            if (x is None or x.color == Node.Colors.BLACK) and sibling.color == Node.Colors.BLACK and mirror_cousin_red:
                sibling.color = sibling.parent.color
                sibling.parent.color = Node.Colors.BLACK
                mirror_cousin.color = Node.Colors.BLACK

                if left_child:
                    self.left_rotation(sibling.parent)
                else:
                    self.right_rotation(sibling.parent)
                return True


if __name__ == '__main__':
    path = argv[1]

    red_black_tree = RedBlackTree()

    with open(path, mode='r') as number_sequence_source:
        for line in number_sequence_source:
            for number in line.split(' '):
                red_black_tree.insert(int(number))

    print(red_black_tree)

    end = False
    while not end:
        command = input('Upišite "+ N" za dodati ili "- N" za obrisati čvor s vrijedosti N: ')
        try:
            operation = command.split(' ')[0]
            argument = command.split(' ')[1]

            try:
                argument = int(argument)
            except ValueError:
                raise TypeError('Vrijednost čvora mora biti prirodan broj!')

            if argument <= 0:
                raise TypeError('Vrijednost čvora mora biti prirodan broj!')

            if operation not in {'+', '-'}:
                raise ValueError('Naredba nije definirana!')

        except IndexError:
            print('Izraz je nepotpun!')
            continue
        except TypeError or ValueError as error:
            print(error)
            continue

        if operation == '+':
            red_black_tree.insert(value=argument)
            print(red_black_tree)
        elif operation == '-':
            red_black_tree.delete(value=argument)
            print(red_black_tree)

        end = True if input('Gotovi? Upišite Y za izlaz: ') == 'Y' else False
