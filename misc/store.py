from collections import defaultdict
import time

class Store():
  def __init__(self):
    self.cache = defaultdict(list)

  def set(self, key, val):
    self.cache[key].append((time.time(), val)) 

  def get(self, key, time=None):
    history = self.cache[key]
    if len(history) == 0:
      return None
    else:
      if time is None:
        (_, val) = history[-1]
        return val
      else:
        return findVal(history, time)

def findVal(history, time):
  currentVal = None
  for (t, val) in history:
    if t < time:
      currentVal = val
      continue
    else:
      return currentVal
  return currentVal

kv = Store()
kv.set('x', 3)
print kv.get('x')

t = time.time()
kv.set('x', 5)
print kv.get('x')
print kv.get('x', t)

# 1) get after set returns the value you set
# 2) get old value returns correct value
# 3) get non-existent value => raise KeyError
# 4) get value for timestamp before set => raise KeyError
# 5) set key to existing value => NOP 
