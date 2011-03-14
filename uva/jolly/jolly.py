# Problem 2.8.1 Jolly Jumpers (p.42)
# author: arkajit

import sys

def jolly(nums):
  n = len(nums)
  s = set(range(1,n))
  for i in range(n-1):
    d = abs(nums[i+1]-nums[i])
    if d in s:
      s.remove(d)
    else:
      return False
  return len(s) == 0

def main(argv):
  if len(argv) != 1:
    print "Usage: jolly.py <filename>"
    return -1

  f = open(argv[0], 'r')
  for line in f:
    toks = line.split()
    nums = [int(t) for t in toks[1:]]
    if jolly(nums):
      print "Jolly"
    else:
      print "Not jolly"
  return 0

if __name__ == "__main__":
  main(sys.argv[1:])
