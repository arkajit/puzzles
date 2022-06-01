class MyHashMap(object):
  def __init__(self):
    self.state = {}

  def insert(self, x, y):
    self.state[x] = y

  # Return None if x is not in map
  def get(self, x):
    return self.state[x]

  def addToKey(self, x):
    newState = dict([(k+x, v) for (k,v) in self.state.iteritems()])
    self.state = newState

  def addToValue(self, y):
    newState = dict([(k, v+y) for (k,v) in self.state.iteritems()])
    self.state = newState

def applyOp(hm, op, args):
  if op == "insert":
    hm.insert(args[0], args[1])
  elif op == "get":
    return hm.get(args[0])
  elif op == "addToKey":
    hm.addToKey(args[0])
  elif op == "addToValue":
    hm.addToValue(args[0])

  return None


def hashMap(queryType, query):
  myMap = MyHashMap()
  n = len(queryType)
  getOpSum = 0
  for i in xrange(n):
    op = queryType[i]
    args = query[i]
    retVal = applyOp(myMap, op, args)
    # print "apply(%s, %s) = %s" % (op, args, retVal)
    if op == "get" and retVal is not None:
      getOpSum += retVal
  
  return getOpSum
