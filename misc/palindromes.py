class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def printList(l):
  while l is not None:
    print l.value
    l = l.next

def toArr(l):
  nums = []
  while l is not None:
    nums.append(l.value)
    l = l.next
  return nums

def fromArr(arr):
  nodes = [ListNode(n) for n in arr]
  for i in xrange(1, len(nodes)):
    nodes[i-1].next = nodes[i]
  return nodes[0]

def reverse(l):
  if l is None or l.next is None:
    return l

  prev = None
  curr = l 
  while curr.next is not None:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt

  return curr

printList(reverse(fromArr([1,2,3])))
