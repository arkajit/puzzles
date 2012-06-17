import bisect
import sys

# Returns a counter generator object.
def get_counter(start=1, by=1):
  def counter():
    cnt = start
    while True:
      yield cnt
      cnt += by
  return counter()

class Story:
  def __init__(self, id, score, height):
    self.id = id
    self.score = score
    self.height = height

class Feed:
  def __init__(self, window, height):
    self.stories = []
    self.timestamps = []
    self.counter = get_counter()
    self.window = window
    self.height = height

  # Add a story to list of possible stories if story's height can fit
  # within available height.
  def add_story(self, ts, score, height):
    id = self.counter.next()  # Always increment the counter
    if height <= self.height:
      self.timestamps.append(ts)
      self.stories.append(Story(id, score, height))

  # Perform a reload at the given timestep.
  def reload(self, ts):
    (score, ids) = self._show_stories(ts - self.window)
    if score == 0:
      return "0 0"
    else:
      return "%d %d %s" % (score, len(ids), " ".join(map(str, ids))) 

  # Drops stories before the given start time.
  def _drop_stories(self, before):
    i = bisect.bisect_left(self.timestamps, before)
    self.timestamps = self.timestamps[i:]
    self.stories = self.stories[i:]

  # Shows list of stories that occurred after given time and fit in
  # available height. Picks stories to optimize sum of story scores.
  # Returns tuple of best score and list of story ids chosen.
  def _show_stories(self, after):
    self._drop_stories(after)
    num_stories = len(self.stories)
    num_heights = self.height + 1  # 0 to self.height inclusive

    if num_stories == 0:
      return (0, [])

    # Tables that store solutions to subproblems.
    # scores[i][h] = Best score using only stories with index at most i and
    #                height at most h.
    # choices[i][h] = Bit vector stating which stories are part of the optimal
    #                 solution to the subproblem. MSB is first story.
    scores = [ [0 for i in xrange(num_heights)] for j in xrange(num_stories) ]
    choices = [ [0 for i in xrange(num_heights)] for j in xrange(num_stories) ]
    filled = [ [False for i in xrange(num_heights)] for j in xrange(num_stories) ]

    # Find the best score for using stories of index at most i to fill height h.
    # Memoize answers to recursive subproblems by storing in tables.
    def pick_best(i, h):
      story = self.stories[i]
      if i == 0:
        if story.height > h:
          return (0, 0)
        else:
          return (story.score, 1)
      elif h == 0:
        return (0, 0)

      if not filled[i][h]:
        (scores[i][h], choices[i][h]) = fill_table(i, h)
        filled[i][h] = True
      return (scores[i][h], choices[i][h])
      
    # Compute entry (i, h) of table. 
    def fill_table(i, h): 
      story = self.stories[i]
      # Try omitting story i.
      (score1, choice1) = pick_best(i-1, h)
      if story.height > h:  # Don't consider story i if it won't fit.
        return (score1, choice1 << 1)

      # Try choosing story i.
      (score2, choice2) = pick_best(i-1, h - story.height)

      # Update scores and choices for each option.
      (a, b) = (score1, score2 + story.score)
      (c, d) = (choice1 << 1, (choice2 << 1) + 1)

      if a > b:
        return (a, c)
      elif b > a: 
        return (b, d)
      else:
        score = a
        # Break tie by choosing vector with fewer set bits.
        e, f = bin(c).count('1'), bin(d).count('1')
        if e < f:
          choice = c
        elif e > f:
          choice = d
        else:
          # If still tied, break by which vector has more significant bits set.
          choice = max(c, d)
        return (score, choice)

    # Compute best score and the choice recursively. Speed up using memoization.
    (best_score, best_choices) = pick_best(num_stories-1, self.height)

    # Backtrack to get the chosen stories.
    chosen = []
    for i in xrange(num_stories-1, -1, -1):
      if best_choices % 2 == 1:
        chosen.append(self.stories[i].id)
      best_choices >>= 1
    chosen.reverse()  # Since we added last story first.
    return (best_score, chosen)

def main():
  N, W, H = map(int, sys.stdin.readline().split())
  feed = Feed(W, H)
  output = []

  def parse_event(evt_str):
    toks = evt_str.split()
    if toks[0] == 'S':
      t, s, h = map(int, toks[1:])
      feed.add_story(t, s, h) 
    elif toks[0] == 'R':
      return feed.reload(int(toks[1]))
     
  for i in xrange(N):
    result = parse_event(sys.stdin.readline())
    if result is not None:
      output.append(result)

  print "\n".join(output)
    
if __name__ == "__main__":
  main()
