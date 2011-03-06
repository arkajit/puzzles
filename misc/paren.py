def f(s):
  lvl = 0
  for c in s:
    if c == '(':
      lvl += 1
    elif c == ')':
      lvl -= 1
    elif lvl < 0:
      return False
  return (lvl == 0)

print f('((()))')
