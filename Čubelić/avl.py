class Node:
	def __init__(self, c):
		self.c = c
		self.l = None
		self.r = None

class AVLTree:
	def __init__(self):
		self.root = None

	def __tree_height(self, node):
		return (max(self.__tree_height(node.l), self.__tree_height(node.r)) + 1) if node else 0

	def __difference(self, node):
		return self.__tree_height(node.l) - self.__tree_height(node.r)

	def __rotate_rr(self, parent):
		node = parent.r
		parent.r = node.l
		node.l = parent

		return node

	def __rotate_ll(self, parent):
		node = parent.l
		parent.l = node.r
		node.r = parent

		return node

	def __rotate_lr(self, parent):
		node = parent.l
		parent.l = self.__rotate_ll(node)
		return self.__rotate_rr(parent)

	def __rotate_rl(self, parent):
		node = parent.r
		parent.r = self.__rotate_ll(node)
		return self.__rotate_rr(parent)

	def __balance(self, node):
		bal_factor = self.__difference(node)

		if bal_factor > 1:
			if self.__difference(node.l) > 0:
				node = self.__rotate_ll(node)
			else:
				node = self.__rotate_lr(node)
		elif bal_factor < -1:
			if self.__difference(node.r) > 0:
				node = self.__rotate_rl(node)
			else:
				node = self.__rotate_rr(node)

		return node

	def __insert(self, root, c):
		if root == None:
			root = Node(c)
			return root

		if c < root.c:
			root.l = self.__insert(root.l, c)
			root = self.__balance(root)
		elif c >= root.c:
			root.r = self.__insert(root.r, c)
			root = self.__balance(root)

		return root

	def __preorder(self, r):
		if r == None:
			return ""
		return r.c + self.__preorder(r.l) + self.__preorder(r.r)

	def __postorder(self, r):
		if r == None:
			return ""
		return self.__postorder(r.l) + self.__postorder(r.r) + r.c

	def __find(self, r, key):
		if r == None or r.c == key:
			return r

		if key < r.c:
			return self.__find(r.l, key)
		if key > r.c:
			return self.__find(r.r, key)

		return r

	def InsertElement(self, key):
		self.root = self.__insert(self.root, key)

	def getChildrenNodesValues(self, key = None):
		node = self.root if not key else self.__find(self.root, key)

		left = node.l.c if node.l else None
		right = node.r.c if node.r else None

		return (left, right)

	def getRootNode(self):
		return self.root.c if self.root else None

	def PreOrderTraversal(self):
		return self.__preorder(self.root)

	def PostOrderTraversal(self):
		return self.__postorder(self.root)

if __name__ == "__main__":
	t = AVLTree()
	t.InsertElement('1')
	t.InsertElement('5')
	t.InsertElement('6')
	t.InsertElement('2')
	t.InsertElement('7')
	t.InsertElement('9')
	t.InsertElement('3')

	assert(t.PreOrderTraversal() == "5213769"), "Invalid PreOrderTraversal"
	assert(t.PostOrderTraversal() == "1326975"), "Invalid PostOrderTraversal"