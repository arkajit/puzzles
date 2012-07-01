# Project Euler Problem 10: Sum of primes < 2M.
import collections

max_prime = 2000000
total = 0
nums = set(xrange(2, max_prime))
it = 0

while len(nums) > 0:
  next_prime = nums.pop()
  if it % 100 == 0:
    print "Next Prime: %d" % next_prime
  total += next_prime
  it += 1
  nums.difference_update(set([n for n in nums if n % next_prime == 0]))

print total
