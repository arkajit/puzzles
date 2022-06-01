class MyHashMap(object):
  def __init__(self):
    self.state = {}
    self.keyOffset = 0
    self.valueOffset = 0

  def insert(self, x, y):
    self.state[x] = y

  # Return None if x is not in map
  def get(self, x):
    k = x - self.keyOffset
    if k not in self.state:
      return None
    else:
      return self.state[k] + self.valueOffset

  def addToKey(self, x):
    self.keyOffset += x
    # newState = dict([(k+x, v) for (k,v) in self.state.iteritems()])
    # self.state = newState

  def addToValue(self, y):
    self.valueOffset += y
    # for (k,v) in self.state.iteritems():
    #  self.state[k] = v+y

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
    print "apply(%s, %s) = %s" % (op, args, retVal)
    if op == "get" and retVal is not None:
      getOpSum += retVal
  
  return getOpSum

if __name__ == "__main__":
    result = hashMap(
            ["insert", "addToKey", "addToValue", "get"],
            [[0,1], [1], [1], [1]])
    print "Result: ", result
