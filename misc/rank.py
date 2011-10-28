def median(a, b) :
  """
  @param: a - sorted list of integers
  @param: b - sorted list of integers

  @return: the median element among the combined list of integers 
  """
  n = len(a) + len(b)
  if n % 2 == 1:
    return rank(a, b, n/2)
  else:
    return (rank(a, b, n/2-1) + rank(a, b, n/2)) / 2

def order(nums, n):
  """
  @param: nums - a sorted list of integers
  @param: n - an integer 

  @return: the order of n if it were to be inserted in sorted order
    in the list (i.e. how many numbers in the list are smaller than n?)
  """
  if len(nums) == 0:
    return 0
  else:
    i = len(nums)/2
    m = nums[i]
    if n == m:
      return i + 1
    elif n < m:
      return order(nums[:i], n)
    else:
      return order(nums[i+1:], n) + i + 1

def rank(a, b, k) :
  """
  @param: a - sorted list of integers
  @param: b - sorted list of integers
  @param: k - integer < len(a) + len(b)

  @return: the element of rank k among the elements in both a and b.
  """
  if k == 0:
    if len(a) == 0:
      return b[0]
    else:
      return a[0]
  else:
    r = min(k, len(a)-1)
    g = a[r]
    s = order(b, g)
    t = r + s  # how many numbers less than g in both a and b?
    if t == k:
      return g
    elif t < k:
      return rank(a[r+1:], b[s:], k - (t+1))
    else:
      return rank(a[:r], b[:s], k)  

aNums = [1, 5, 7, 10, 15, 17, 21, 31, 35, 42]
bNums = [5, 10, 13, 13, 26, 43, 52]

print median(aNums, bNums)  # expect 15

cNums = [1, 5, 7, 10, 15, 17, 21, 31, 35, 42]
dNums = [5, 10, 13, 13, 26, 43, 52, 55]

print median(cNums, dNums)  # expect 16
