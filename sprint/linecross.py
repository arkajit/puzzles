import bisect
import functools

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
    self.id = Line.counter.next()
    self.start = x
    self.end = x+l
    self.pos = y

class Query:
  counter = get_counter()
  def __init__(self, x, y, l):
    self.id = Query.counter.next()
    self.start = y
    self.end = y+l
    self.pos = x

  def __str__(self):
    return 'Query(start=%d, end=%d, pos=%d)' % (self.start, self.end, self.pos)

class LineSet:
  def __init__(self):
    self.lines = []

  def AddLine(self, x, y, l):
    self.lines.append(Line(x, y, l))

  # All lines have been added. Prepare for executing queries.
  def Prepare(self):
    self.lines_by_pos = sorted(self.lines, key=lambda l: l.pos)
    self.pos_ids = map(lambda l: l.id, self.lines_by_pos)
    self.lpos = map(lambda l: l.pos, self.lines_by_pos)

    self.lines_by_start = sorted(self.lines, key=lambda l: l.start)
    self.start_ids = map(lambda l: l.id, self.lines_by_start)
    self.lstart = map(lambda l: l.start, self.lines_by_start)

    self.lines_by_end = sorted(self.lines, key=lambda l: l.end)
    self.end_ids = map(lambda l: l.id, self.lines_by_end)
    self.lend = map(lambda l: l.end, self.lines_by_end)

  # Following functions return set of line ids.
  def GetLinesBetween(self, y1, y2):
    a = bisect.bisect_left(self.lpos, y1)
    b = bisect.bisect_right(self.lpos, y2)
    return set(self.pos_ids[a:b])

  def GetLinesStartingBefore(self, x1):
    a = bisect.bisect_right(self.lstart, x1)
    return set(self.start_ids[:a])

  def GetLinesEndingAfter(self, x2):
    b = bisect.bisect_left(self.lend, x2)
    return set(self.end_ids[b:])

  # Returns the number of lines that match the query.
  def ExecuteQuery(self, q):
    filters = [
      functools.partial(self.GetLinesBetween, q.start, q.end),
      functools.partial(self.GetLinesStartingBefore, q.pos),
      functools.partial(self.GetLinesEndingAfter, q.pos)
    ]

    matches = filters[0]()
    for f in filters[1:]:
      if len(matches) == 0:
        return 0
      else:
        matches.intersection_update(f())

    return len(matches)

line_set = LineSet()
N = input()
for i in range(N):
  x, y, l = [int(i) for i in raw_input().split()]
  line_set.AddLine(x, y, l)

Q = input()
queries = []
for q in range(Q):
  x, y, l = [int(i) for i in raw_input().split()]
  queries.append(Query(x, y, l))

line_set.Prepare()
results = []
for q in queries:
  results.append(line_set.ExecuteQuery(q))

for r in results:
  print r
