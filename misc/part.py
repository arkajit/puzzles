def part(S,n,k):
  infty = sum(S) + 1
  T = [([infty] * k) for i in range(n)]
  B = [([-1] * k) for i in range(n)]

  p = S[:]
  for j in range(1,n):
    p[j] += p[j-1]

  T[0] = [S[0] for i in range(k)]
  for j in range(n):
    T[j][0] = p[j]

  for i in range(1,n):
    for j in range(1,k):
      for x in range(i):
        y = max(T[x][j-1], p[i] - p[x])
        if T[i][j] > y:
          T[i][j] = y
          B[i][j] = x

  return (B, T[n-1][k-1])

def partition(S,k):
  n = len(S)
  B, best = part(S,n,k)
  parts = [[] for i in range(k)]
  while k > 1:
    n = B[n-1][k-1]+1
    parts[k-1] = S[n:]
    S = S[:n]
    k -= 1
  parts[0] = S
  return parts, best
    
   

S = range(1,10)
parts, best = partition(S,3)
print "S is ", S
print "Best score is %d" % best
print "Partition is ", parts
