fin = open('lineup.in', 'r')
fout = open('lineup.out', 'w')

N = int(f.readline())
cows = {}
unseen = set([])
for i in xrange(N):
  (x, breed) = f.readline().split()
  cows[x] = breed
  counts[breed] = 0
  unseen.add(breed)
fin.close()

start = end = 0
keys = sorted(cows.iterkeys())
best = 1e9

