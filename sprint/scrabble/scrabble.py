from collections import deque
import itertools
import sys

scrabble_score = {
  'A': 1, 'B': 3,  'C': 3, 'D': 2, 'E': 1,
  'F': 4, 'G': 2,  'H': 4, 'I': 1, 'J': 8,
  'K': 5, 'L': 1,  'M': 3, 'N': 1, 'O': 1,
  'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
  'U': 1, 'V': 4,  'W': 4, 'X': 8, 'Y': 4,
  'Z': 10
}

# map from words in dictionary to their scrabble scores
scores = {}

# map from stems like _AT to set of words that complete it
# (e.g. CAT, BAT, TAT) 
stems = {}

class Ladder:
  def __init__(self, words, left, right):
    self.words = words.union(set([left, right]))  # ensure left, right in set
    self.left = left
    self.right = right

  def score(self):
    return sum(map(word_score, self.words))

  def neighbors(self):
    left_score = word_score(self.left)
    left_nbrs = set(filter(lambda n: word_score(n) < left_score,
                           get_neighbors(self.left) - self.words))
    right_score = word_score(self.right)
    right_nbrs = set(filter(lambda n: word_score(n) < right_score,
                            get_neighbors(self.right) - self.words))
    
    ladders = []
    for (l, r) in itertools.product(left_nbrs, right_nbrs):
        if l < r:
          ladders.append(Ladder(self.words, l, r))
    return ladders
   
def word_score(word):
  return sum(scrabble_score[letter] for letter in word)

def get_stems(word):
  for i in xrange(len(word)):
    yield word[:i] + '_' + word[i+1:]

def add_stems(word):
  for stem in get_stems(word):
    stems.setdefault(stem, set()).add(word)

def get_neighbors(word):
  nbrs = set()
  for stem in get_stems(word):
    nbrs.update(stems[stem])
  nbrs.discard(word)  # Do not count self as a neighbor 
  return nbrs

# visit all ladders centered at center_word
def best_ladders(center_word):
  best_score = 0
  Q = deque([Ladder(set([center_word]), center_word, center_word)])
  while len(Q):
    next_ladder = Q.popleft() 
    next_score = next_ladder.score()
    best_score = max(best_score, next_score)
    # Unscientific heuristic to prune down search tree.
    if next_score > 0.9 * best_score:
      Q.extend(next_ladder.neighbors())

  return best_score

def main():
  K = int(sys.stdin.readline())
  N = int(sys.stdin.readline())
  for i in xrange(N):
    word = sys.stdin.readline().strip()
    if len(word) == K:
      scores[word] = word_score(word)
      add_stems(word)
  # Best score is 0 or best ladders centered at any of the K-length words
  best_scores = map(best_ladders, scores.keys())
  best_score = max([0] + best_scores)
  print best_score

if __name__ == "__main__":
  main()
