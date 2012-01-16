myLast [] = error "Empty list has no last element"
myLast [x] = x
myLast (_:xs) = myLast xs

myButLast [] = error "Empty list"
myButLast [x] = error "Singleton list"
myButLast [x,y] = x
myButLast (_:xs) = myButLast xs

elementAt :: (Integral b) => [a] -> b -> a
elementAt [] k = error "Index out of bounds."
elementAt (x:_) 0 = x
elementAt (_:xs) k = elementAt xs (k-1)

myLength [] = 0
myLength (_:xs) = 1 + myLength xs

reverse' [] = []
reverse' (x:xs) = (reverse' xs) ++ [x]

isPalindrome xs = xs == (reverse' xs)

compress [] = []
compress [x] = [x]
compress (x:ys@(y:_)) = if x == y
                      then compress ys
                      else x:(compress ys)

pack [] = []
pack (x:xs) = [a] ++ pack b
  where (a, b) = comb [x] xs
        comb a [] = (a, [])
        comb a@(x:xs) b@(y:ys)
          | x == y    = comb (a ++ [y]) ys
          | otherwise = (a, b)

encode xs = [(length run, head run) | run <- pack xs]
