# int k = 15
# int a[] { 5, 13, 7, 0, 2, 15, 0, 4, 10, 8 }

# output
# 5, 10
# 15, 0
# 7, 8
# 13, 2

# (a, b) a < b

def find_pairs(a, k):
  seen = set()
  pairs = []
  for n in a:
    y = n
    x = k-n
    if x in seen:  
      pairs.append((x,y))
      seen.discard(x)
    seen.add(n) 
    
  return pairs
    
def find_triplets(a, k):
  triplets = []
  for i in xrange(len(a)):
    n = a[i]
    rest = a[0:i] + a[i+1:]
    target = k-n
    pairs = find_pairs(rest, target)
    triplets.extend([(n, x, y) for (x,y) in pairs])
  return triplets
    
# Possible Issues:
# Solved: 14 - 7 = 7 (might have two of the same)
# Solved: duplicates should be solved

test_cases = [
  {'a': [5, 13, 7, 0, 2, 15, 0, 4, 10, 8], 'k': 15},
  {'a': [5, 13, 7, 0, 2, 15, 0, 4, 10, 8], 'k': 14},
  {'a': [5, 13, 7, 0, 2, 15, 0, 4, 10, 8], 'k': 24},
]

for i, test_case in enumerate(test_cases):
  print "Test case %d" % i
  triplets = find_triplets(test_case['a'], test_case['k'])
  print "Triplets", triplet
