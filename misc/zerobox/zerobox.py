import sys

# Return the dimensions of the largest square of zeros in a
# grid of zeroes and ones.
def zerobox(grid):
  n = len(grid)-1
  # T[i][j] = largest square of zeros with bottom right corner in (i,j)
  T = [[0 for i in range(n+1)] for i in range(n+1)]
  if grid[1][1] == 0:
    T[1][1] = 1

  for i in range(1,n+1):
    for j in range(1,n+1):
      if i == j == 1:
        continue

      if grid[i][j]:
        T[i][j] = 0
      else:
        a = T[i-1][j-1]
        b = T[i][j-1]
        c = T[i-1][j]
        T[i][j] = min(a,b,c) + 1

  return max([max(T[i]) for i in range(n+1)])

def readbox(fn):
  f = open(fn, 'r')
  n = int(f.readline())
  grid = [[1 for i in range(n+1)] for i in range(n+1)]
  for i in range(1,n+1):
    strs = f.readline().split()
    grid[i] = [1] + [int(s) for s in strs]

  return grid

def main(argv):
  if len(argv) != 1:
    print "Usage: python zerobox.py <filename>"
    return 1
  
  grid = readbox(argv[0])
  print grid
  print "Score ", zerobox(grid) 
  return 0

if __name__ == "__main__":
  sys.exit(main(sys.argv[1:]))
  
