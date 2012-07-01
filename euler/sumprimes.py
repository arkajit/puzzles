# Project Euler Problem 10: Sum of primes < 2M.
import collections

max_prime = 2000000
total = 0
nums = collections.deque(range(2, max_prime))
it = 0

while len(nums) > 0:
  next_prime = nums.popleft()
  if it % 100 == 0:
    print "Next Prime: %d" % next_prime
  total += next_prime
  it += 1
  nums = collections.deque(filter(lambda x: x % next_prime != 0, nums))

print total
