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
    self.stories = {}
    self.counter = get_counter()
    self.window = window
    self.height = height

  # Add a story to list of possible stories if story's height can fit
  # within available height.
  def add_story(self, ts, score, height):
    id = self.counter.next()  # Always increment the counter
    if height <= self.height:
      self.stories[ts] = Story(id, score, height)

  # Perform a reload at the given timestep.
  def reload(self, ts):
    (score, ids) = self._show_stories(ts - self.window)
    if score == 0:
      return "0 0"
    else:
      return "%d %d %s" % (score, len(ids), " ".join(map(str, ids))) 

  # Shows list of stories that occurred after given time and fit in
  # available height. Picks stories to optimize sum of story scores.
  # Returns tuple of best score and list of story ids chosen.
  def _show_stories(self, after):
    # Drop all stories before current start_time. Won't need them again.
    self.stories = dict(filter(lambda (k,v): k >= after, self.stories.items()))
    story_list = self.stories.values()
    story_list.sort(key=lambda s:s.id)
    num_stories = len(story_list)
    num_heights = self.height + 1  # 0 to self.height inclusive

    if num_stories == 0:
      return (0, [])

    # Tables that store solutions to subproblems.
    # scores[i][h] = Best score using only stories with index at most i and
    #                height at most h.
    # choices[i][h] = List of booleans stating whether given story is part of
    #                 of the optimal solution to the subproblem.
    scores = [ [0 for i in xrange(num_heights)] for j in xrange(num_stories) ]
    choices = [ [[] for i in xrange(num_heights)] for j in xrange(num_stories) ]

    # Find the best score for using stories of index at most i to fill height h.
    def pick_best(i, h):
      story = story_list[i]
      if i == 0:
        if story.height > h:
          return (0, [False])
        else:
          return (story.score, [True])

      rem_height = h - story.height
      if rem_height < 0:
        return (scores[i-1][h], choices[i-1][h] + [False])

      (a, b) = (scores[i-1][h], scores[i-1][rem_height] + story.score)
      (c, d) = (choices[i-1][h] + [False], choices[i-1][rem_height] + [True])
      if a > b:
        return (a, c)
      elif b > a: 
        return (b, d)
      else:
        score = a
        # Break tie by shorter stories.
        if sum(c) < sum(d):
          choice = c
        elif sum(c) > sum(d):
          choice = d
        else:
          # If still tied, break by which has more Trues earlier.
          choice = max(c, d)
        return (score, choice)

    # Fill tables from bottom up using dynamic programming.
    for i in xrange(num_stories):
      for h in xrange(num_heights):
        (scores[i][h], choices[i][h]) = pick_best(i, h)

    # Backtrack to get the chosen stories.
    chosen = []
    (best_score, best_choices) = (scores[-1][-1], choices[-1][-1])
    for i in xrange(num_stories):
      if best_choices[i]:
        chosen.append(story_list[i].id)
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
