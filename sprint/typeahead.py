import sys

class Type:
  User, Topic, Question, Board = range(4)
  AllTypes = {
    'user':     User,
    'topic':    Topic,
    'question': Question,
    'board':    Board
  }
  Names = {
    User: 'User',
    Topic: 'Topic',
    Question: 'Question',
    Board: 'Board'
  }

class Item:
  def __init__(self, type, uid, score, data, num):
    self.type = Type.AllTypes[type]
    self.uid = uid
    self.score = score
    self.data = data
    self.num = num  # order of addition

  def __str__(self):
    return "%s(%s, %f) = %s" % (Type.Names(self.type), self.uid,
                                self.score, self.data)

class TypeaheadService:
  def __init__(self):
    self.items = {}     # map from uid to Item objects
    self.counter = 0    # number of ADDs handled by service
    self.prefixes = {}  # map from prefixes to item uids that contain it

  def exec_cmd(self, cmd_str):
    (command, cmd_data) = cmd_str.split(' ', 1)
    if command == 'ADD':
      (type, uid, score, data) = cmd_data.split(' ', 3)
      self.add(type.strip(), uid.strip(), float(score), data.strip().lower())
    elif command == 'DEL':
      uid = cmd_data.strip()
      self.delete(uid)
    elif command == 'QUERY':
      (num_results, query_string) = cmd_data.split(' ', 1)
      return self.query(int(num_results), query_string.strip().lower())
    elif command == 'WQUERY':
      (num_results, num_boosts, rest) = cmd_data.split(' ', 2)
      boosts_and_query = rest.split(' ', int(num_boosts))
      query_string = boosts_and_query[-1]
      boosts_keyval = [b.split(':') for b in boosts_and_query[:-1]]
      boosts = dict([(Type.AllTypes.get(k, k), float(v))
                      for (k, v) in boosts_keyval])
      return self.wquery(int(num_results), boosts, query_string.strip().lower())

  def add(self, type, uid, score, data):
    self.items[uid] = Item(type, uid, score, data, self.counter)
    self.counter += 1
    for word in data.split():
      self.add_prefixes(uid, word)

  def delete(self, uid):
    item = self.items.pop(str(uid), None)
    if item:
      for word in item.data.split():
        self.remove_prefixes(uid, word)

  def query(self, num_results, query_string):
    candidates = self.get_candidates(query_string)
    candidates.sort(reverse=True, key=lambda uid:self.items[uid].score)
    return " ".join(candidates[:num_results])

  def wquery(self, num_results, boosts, query_string):
    candidates = self.get_candidates(query_string)
    candidates.sort(reverse=True,
                       key=lambda uid:self.items[uid].score *
                                      boosts.get(uid, 1) *
                                      boosts.get(self.items[uid].type, 1))
    return " ".join(candidates[:num_results])

  # Returns a generator with all the prefixes for the given word.
  @staticmethod
  def get_prefixes(word):
    for i in xrange(1, len(word)+1):
      yield word[:i]

  def add_prefixes(self, id, word):
    for prefix in TypeaheadService.get_prefixes(word):
      self.prefixes.setdefault(prefix, set()).add(id)

  def remove_prefixes(self, id, word):
    for prefix in TypeaheadService.get_prefixes(word):
      self.prefixes.get(prefix, set()).discard(id)

  # Return list of candidate ids with most recent additions first
  def get_candidates(self, query):
    words = query.split()
    candidates = []
    if len(words) > 0:
      candidates = self.prefixes.get(words[0], set()).copy()
      for word in words[1:]:
        candidates.intersection_update(self.prefixes.get(word, set()))
      candidates = list(candidates)
      candidates.sort(reverse=True, key=lambda uid:self.items[uid].num)
    return candidates

def main():
  service = TypeaheadService()
  N = int(sys.stdin.readline())
  output = []
  for i in xrange(N):
    result = service.exec_cmd(sys.stdin.readline())
    if result is not None:
      output.append(result)
  print "\n".join(output)

if __name__ == "__main__":
  main()
