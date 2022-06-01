# k sorted linked lists 5->10->20, 10, 5->19
# merge into one sorted linked lists 5->5->10->10->19->20

import heapq

class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
    
    def __str__(self):
        if self.next == None:
            return "Node(%d, None)" % self.val
        else:
            return "Node(%d,_)" % self.val
        
    def __repr__(self):
        return str(self)
        
def listToNode(nums):
    if len(nums) == 0:
        return None
    return Node(nums[0], listToNode(nums[1:]))

def nodeToList(node):
    l = []
    while node != None:
        l.append(node.val)
        node = node.next
    return l

def printNode(node):
    print str(nodeToList(node))
        
# class Heap(object):
#   def __init__(self):
#      self.size = 0
#       pass
#   def add(self, val):
#       self.size += 1
#       pass
    
    # Return min key in the heap and pop it
#    def minKey(self):
#        self.size -= 1
#        pass
    
#    def size(self):
#        return self.size

def mergeLists(nodes):
    mergedHead, mergedTail = None, None
    
    # Init Heap with list heads.
    # heap = Heap()
    heap = []
    for n in nodes:
        heap.append((n.val, n.next))
        # n = n.next  # TODO: will this change the right object?
        
    heapq.heapify(heap)
    print "Heap", heap

    while len(heap) > 0:
        (v, nextNode) = heapq.heappop(heap)
        if nextNode is not None:
            heapq.heappush(heap, (nextNode.val, nextNode.next))
        
        # Insert val to list
        node = Node(v, None)
        # TODO: extract this as a function
        if mergedHead is None:
            mergedHead = node
            mergedTail = node
        else:
            mergedTail.next = node
            mergedTail = node
    
    return mergedHead

nodes = [
    listToNode([5, 10, 20]),
    listToNode([10]),
    listToNode([5, 19]),
]

print "Input nodes"
for n in nodes:
    printNode(n)

print "Output node"
mergedResult = mergeLists(nodes)
printNode(mergedResult)

