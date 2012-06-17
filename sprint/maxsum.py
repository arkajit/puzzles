def maxsumprod(N):
  odds = range(1, N, 2)
  evens = range(2, N, 2)
  perm = []
  if N % 2 == 0:  # even
    evens.reverse()
    perm = odds + [N] + evens
  else:  # odd
    odds.reverse()
    perm = evens + [N] + odds
  if N == 1:
    return perm[0]
  else:
    return sum([perm[i] * perm[i+1] for i in xrange(N-1)])

T = input()
cases = []
for i in xrange(T):
  cases.append(input())

for c in cases:
  print maxsumprod(c)
