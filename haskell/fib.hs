fibNextTuple (x, y) = (y, x+y)

fibNth 1 = (1, 1)
fibNth n = fibNextTuple (fibNth (n-1))

fib :: Integer -> Integer
fib = fst . fibNth
