import random

def median(nums, rank=None):
  print "nums is ", nums, "rank = ", rank

  n = len(nums)
  if n == 0:
    return None
  elif n == 1:
    return nums[0]

  if rank is None:
    rank = n/2

  pivot = nums[0]
  lower = []
  upper = []
  for n in nums:
    if n <= pivot:
      lower.append(n)
    elif n > pivot:
      upper.append(n)

  k = len(lower)  # rank of pivot
  print "lower", lower
  print "upper", upper
  print "pivot", pivot
  #if k == rank:
  #  return pivot
  #elif k < rank:
  #  return median(upper, rank=rank-k)
  #else:
  #  return median(lower, rank=rank)

nums = [2]*3 + [1, 11]
random.shuffle(nums)

print "Median is", median(nums)

