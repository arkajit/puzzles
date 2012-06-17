import bisect

def get_counter(start=1, by=1):
  def counter():
    cnt = start
    while True:
      yield cnt
      cnt += by
  return counter()

class Line:
  counter = get_counter()
  def __init__(self, x, y, l):
    self.start = x
    self.end = x+l
    self.pos = y
    self.id = Line.counter.next()

class Query:
  counter = get_counter()
  def __init__(self, x, y, l):
    self.start = y
    self.end = y+l
    self.pos = x
    self.id = Query.counter.next()

N = input()
lines = []
for i in range(N):
  x, y, l = [int(i) for i in raw_input().split()]
  lines.append(Line(x, y, l))
lines.sort(key=lambda line: line.pos)

Q = input()
queries = []
for q in range(Q):
  x, y, l = [int(i) for i in raw_input().split()]
  queries.append(Query(x, y, l))
queries.sort(key=lambda q: q.pos)

qpos = [q.pos for q in queries]
matching_queries = []
for l in lines:
  # Find queries whose position is between l.start and l.end
  a = bisect.bisect_left(qpos, l.start)
  b = bisect.bisect_right(qpos, l.end)
  matching_queries.append(set(queries[a:b]))
  #print "Line loop: a = %d, b = %d" % (a, b)

lpos = [l.pos for l in lines]
match_count = []

# Loop over queries in original id order.
for q in sorted(queries, key=lambda q: q.id):
  cnt = 0

  # Find lines between q.start and q.end
  a = bisect.bisect_left(lpos, q.start)
  b = bisect.bisect_right(lpos, q.end)
  #print "Query loop: a = %d, b = %d" % (a, b)
  
  # For each line, check whether query in Dictionary[Line]
  for i in xrange(a,b):
    if q in matching_queries[i]:
      cnt += 1

  match_count.append(cnt)

for mc in match_count:
  print mc
