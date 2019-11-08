class Node():
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BST():
	def __init__(self):
		self.root = None
	
	def addNode(self, value):
		return Node(value) #returns a Node, see class
	
	def addBST(self, node, number): #node = current node, number is what you wish to add
		if node is None:
			return self.addNode(number)
		#go left
		elif number < node.value:	
			node.left = self.addBST(node.left, number)
			
		#go right
		elif number > node.value:
			node.right = self.addBST(node.right, number)
			
		return node

	def printBST(self, node):
		#Print values from root
		#In order
		if node.left is not None:
			self.printBST(node.left)
			
		print(node.value)
		
		if node.right is not None:
			self.printBST(node.right)
			
		return
		
	
	

if __name__ == "__main__":
	bst = BST()
	root = Node(50)
	bst.root = root
	
	bst.addBST(bst.root, 15)
	bst.addBST(bst.root, 99)
	bst.addBST(bst.root, 25)
	bst.addBST(bst.root, 56)
	bst.addBST(bst.root, 78)
		
	bst.printBST(bst.root)