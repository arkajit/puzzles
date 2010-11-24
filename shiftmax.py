def rcshift(nums, k):
  n = len(nums)
  k = k % n
  first = nums[:n-k]
  last = nums[-k:]
  return last + first

def shiftmax(shifted):
  n = len(shifted)
  if n == 0:
    return None 
  elif n == 1:
    return shifted[0]
  else:
    k = n / 2
    if shifted[k] > shifted[(k+1) % n]:
      return shifted[k]
    else:
      first = shifted[0]
      last = shifted[-1]
      if shifted[k] > last:
        return shiftmax(shifted[k+1:])
      elif last > first:
        return last
      else:
        return shiftmax(shifted[:k])

s = rcshift(range(1000), 467)
t = rcshift([1, 1, 2, 2, 3, 3], 4)
r = rcshift([1] * 100 + [2] * 100 + [3] * 100, 143)
print shiftmax(s)
print shiftmax(t)
print shiftmax(r)
  
