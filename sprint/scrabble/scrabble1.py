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

# score of the best ladder centered at the given word
def best_ladder(center_word):
  best_score = word_score(center_word)
  used_words = set([center_word])
  left = right = center_word
  while left and right:
    (left, right) = extend_ladder(used_words, left, right)
    if not left or not right:
      break
    best_score += scores.get(left, 0) + scores.get(right, 0)
    used_words.add(left)
    used_words.add(right)
  return best_score
   
# add words to left and right end of a ladder 
def extend_ladder(current_words, left_word, right_word):
  new_left_word, new_right_word = ('', '')

  # Get possible neighbors which are
  #   1) NOT already used AND
  #   2) and have a word score less than the previous word
  left_score = word_score(left_word)
  left_nbrs = set(filter(lambda n: word_score(n) < left_score,
                         get_neighbors(left_word) - current_words))
  right_score = word_score(right_word)
  right_nbrs = set(filter(lambda n: word_score(n) < right_score,
                          get_neighbors(right_word) - current_words))
  if left_nbrs:
    new_left_word = max(left_nbrs, key=scores.get)
    right_nbrs.discard(new_left_word)  # Don't reuse the new left word on right
  if right_nbrs:
    new_right_word = max(right_nbrs, key=scores.get)
  return (new_left_word, new_right_word)

def main():
  K = int(sys.stdin.readline())
  N = int(sys.stdin.readline())
  for i in xrange(N):
    word = sys.stdin.readline().strip()
    if len(word) == K:
      scores[word] = word_score(word)
      add_stems(word)
  # Best score is 0 or best ladders centered at any of the K-length words
  best_scores = map(best_ladder, scores.keys())
  best_score = max([0] + best_scores)
  print best_score

if __name__ == "__main__":
  main()
