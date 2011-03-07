# The Huffman Coding algorithm

import heapq

class Node :
	def __init__(self, name, left=None, right=None) :
		self.name = name
		self.left = left
		self.right = right

def huff(freqs) :
	heap = []
	for key in freqs :
		node = Node(key)
		heapq.heappush(heap, (freqs[key], node))
	
	while len(heap) >= 2 :
		(a, x) = heapq.heappop(heap)
		(b, y) = heapq.heappop(heap)
		z = Node(x.name + y.name, x, y)
		heapq.heappush(heap, (a+b, z))

	(tot, node) = heap[0]
	return node

def dfs(tree) :
	code = {}
	Q = [('', tree)]
	while len(Q) > 0 :
		(path, node) = Q.pop(0)
		if node.left :
			Q.append((path+'0', node.left))
		if node.right :
			Q.append((path+'1', node.right))
		if not node.left and not node.right : # a leaf
			code[node.name] = path
	return code
			

freqs = {'a' : 0.4, 'b' : 0.2, 'c' : 0.2, 'd' : 0.1, 'e' : 0.1}
root = huff(freqs)
code = dfs(root)
print code
