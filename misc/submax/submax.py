def submax(x):
  n = len(x)

  # compute prefixes
  p = [0] * (n+1)
  for i in range(n):
    p[i+1] = p[i] + x[i]

  d = (0,0) # maintain actual best solution
  s = x[0] # maintain score of best solution

  for i in range(1,n):
    (a,b) = d
    scores = {s: (a,b),
              p[i+1] -p[a]: (a, i),
              x[i]: (i, i)}
    s = max(scores.keys())
    d = scores[s]

  return s, d

def maxsubarray(a):
  best = best_here = 0
  for x in a:
    best_here = max(0, best_here + x)
    best = max(best, best_here)
  return best

x = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
s, d = submax(x)
(a,b) = d
print "best score is %d" % s
print "max best is %d" % maxsubarray(x)
print x[a:b+1]
