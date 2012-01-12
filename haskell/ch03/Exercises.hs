-- file: ch03/Exercises.hs

-- 1. length of a list
myLength :: [a] -> Int
myLength []     = 0
myLength (_:xs) = 1 + myLength xs

-- 3. mean of a list
mean xs = sum xs / (fromIntegral (length xs))

-- 4. make a palindrome
palindromize xs = xs ++ reverse xs

-- 5. is a palindrome
isPalindrome []  = True
isPalindrome [x] = True
isPalindrome xs  = ((head xs) == (last xs)) && isPalindrome (tail (init xs))

-- 6. sort list of lists by length
--listCmp xs ys = compare (length xs) (length ys)
--sortLists lists = sortBy listCmp lists

isEmpty :: [a] -> Bool
isEmpty []  = True
isEmpty _   = False

myHead :: [a] -> a
myHead []     = error "List empty"
myHead (x:_)  = x

myTail :: [a] -> [a]
myTail []     = error "List empty"

-- this matches the : constructor for a list which joins first with rest
myTail (_:xs) = xs

myLast :: [a] -> a
myLast []     = error "List empty"
myLast [x]    = x
myLast (_:xs) = myLast xs

myInit :: [a] -> [a]
myInit []       = error "List empty"
myInit [x]      = []
--myInit ((xs):x) = xs

-- a can't be any type, it must be an Ord to support < and >= operators
qsort :: Ord a => [a] -> [a]
qsort []      = []
qsort (x:xs)  =   qsort [y | y <- xs, y < x]
              ++  [x]
              ++  qsort [y | y <- xs, y >= x]

myMap           :: (a->b) -> [a] -> [b]
myMap f []      = []
myMap f (x:xs)  = f x : map f xs

-- infinite lists because of lazy evaluation
numsFrom n = n : numsFrom (n+1)
squares = map (^2) (numsFrom 0)  -- ^2 is a "section", a partially applied infix op

-- using boolean guards in pattern matching function definitions
sign x | x > 0    = 1
       | x == 0   = 0
       | x < 0    = -1

-- can also use case expressions
myTake m ys   = case (m,ys) of
                  (0,_)     ->  []
                  (_,[])    ->  []
                  (n,x:xs)  ->  x : myTake (n-1) xs

